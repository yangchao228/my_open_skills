#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo"

fail=0

note() {
  printf '%s\n' "$*"
}

error() {
  printf 'error: %s\n' "$*" >&2
  fail=1
}

profile_file="config/clawhub-profile.json"
publisher_handle=""
wechat_official_account=""
x_handle=""
x_url=""
github_url=""
description_suffix=""

if [ ! -f "$profile_file" ]; then
  error "missing $profile_file"
elif ! jq . "$profile_file" >/dev/null; then
  error "$profile_file is not valid JSON"
else
  publisher_handle="$(jq -r '.publisher_handle // empty' "$profile_file")"
  wechat_official_account="$(jq -r '.wechat_official_account // empty' "$profile_file")"
  x_handle="$(jq -r '.x_handle // empty' "$profile_file")"
  x_url="$(jq -r '.x_url // empty' "$profile_file")"
  github_url="$(jq -r '.github_url // empty' "$profile_file")"
  description_suffix="$(jq -r '.description_suffix // empty' "$profile_file")"

  if [ "$publisher_handle" != "yangchao228" ]; then
    error "$profile_file publisher_handle must be yangchao228"
  fi

  for value in "$wechat_official_account" "$x_handle" "$x_url" "$github_url" "$description_suffix"; do
    if [ -z "$value" ]; then
      error "$profile_file contains an empty required creator field"
    fi
  done
fi

skill_json_files=()
source_dirs=()

validate_skill() {
  local skill_md="$1"
  local dir slug source_dir status description description_length version homepage
  local expected_homepage suffix_count bundle_bytes file_bytes
  dir="$(dirname "$skill_md")"
  slug="$(basename "$dir")"

  if ! sed -n '1p' "$skill_md" | grep -q '^---$'; then
    error "$skill_md missing opening frontmatter marker"
  fi

  if ! sed -n '1,20p' "$skill_md" | grep -q '^name:'; then
    error "$skill_md missing frontmatter name"
  fi

  if ! sed -n '1,20p' "$skill_md" | grep -q '^description:'; then
    error "$skill_md missing frontmatter description"
  fi

  if [ ! -f "$dir/skill.json" ]; then
    error "$dir missing skill.json"
    return
  fi

  if ! jq . "$dir/skill.json" >/dev/null; then
    error "$dir/skill.json is not valid JSON"
  fi

  source_dir="$(jq -r '.source_dir // empty' "$dir/skill.json")"
  if [ "$source_dir" != "$dir" ]; then
    error "$dir/skill.json source_dir '$source_dir' does not match '$dir'"
  fi

  if [ "$(jq -r '.slug // empty' "$dir/skill.json")" != "$slug" ]; then
    error "$dir/skill.json slug does not match folder '$slug'"
  fi

  status="$(jq -r '.status // empty' "$dir/skill.json")"
  case "$status" in
    ready|draft|incubating|private-source|deprecated) ;;
    *) error "$dir/skill.json has unsupported status '$status'" ;;
  esac

  if [ "$status" = "ready" ]; then
    if [ ! -f "$dir/examples/minimal-input.md" ]; then
      error "$dir missing examples/minimal-input.md"
    fi

    if [ ! -f "$dir/examples/expected-output-notes.md" ]; then
      error "$dir missing examples/expected-output-notes.md"
    fi

    description="$(sed -n 's/^description:[[:space:]]*//p' "$skill_md" | head -n 1)"
    description_length="$(DESCRIPTION="$description" python3 -c 'import os; print(len(os.environ["DESCRIPTION"]))')"
    if [ "$description_length" -gt 1024 ]; then
      error "$skill_md description is $description_length characters; maximum is 1024"
    fi

    if [[ "$description" != *"$description_suffix" ]]; then
      error "$skill_md description must end with the canonical ClawHub creator suffix"
    fi

    suffix_count="$(rg -o --fixed-strings "$description_suffix" "$skill_md" 2>/dev/null | wc -l | tr -d ' ' || true)"
    if [ "${suffix_count:-0}" != "1" ]; then
      error "$skill_md must contain the canonical creator suffix exactly once"
    fi

    version="$(sed -n 's/^version:[[:space:]]*//p' "$skill_md" | head -n 1)"
    if ! [[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+([+-][0-9A-Za-z.-]+)?$ ]]; then
      error "$skill_md has invalid or missing semver version '$version'"
    fi

    homepage="$(sed -n 's/^[[:space:]]*homepage:[[:space:]]*//p' "$skill_md" | head -n 1)"
    expected_homepage="https://github.com/yangchao228/my_open_skills/tree/main/$dir"
    if [ "$homepage" != "$expected_homepage" ]; then
      error "$skill_md homepage '$homepage' does not match '$expected_homepage'"
    fi

    if ! grep -Fqx -- "- 微信公众号：\`$wechat_official_account\`" "$skill_md"; then
      error "$skill_md missing canonical WeChat creator footer"
    fi
    if ! grep -Fqx -- "- X：[$x_handle]($x_url)" "$skill_md"; then
      error "$skill_md missing canonical X creator footer"
    fi
    if ! grep -Fqx -- "- GitHub：[yangchao228]($github_url)" "$skill_md"; then
      error "$skill_md missing canonical GitHub creator footer"
    fi

    if sed -n '2,/^---$/p' "$skill_md" | grep -q '^license:'; then
      error "$skill_md declares a per-skill license; ClawHub releases use MIT-0"
    fi
    if find "$dir" -maxdepth 1 -type f -iname 'LICENSE*' -print -quit | grep -q .; then
      error "$dir bundles a license file; review it before ClawHub MIT-0 publication"
    fi

    bundle_bytes=0
    while IFS= read -r -d '' file; do
      file_bytes="$(wc -c < "$file" | tr -d ' ')"
      bundle_bytes=$((bundle_bytes + file_bytes))
    done < <(find "$dir" -type f -not -path '*/.clawhub/*' -print0)
    if [ "$bundle_bytes" -gt 52428800 ]; then
      error "$dir bundle is $bundle_bytes bytes; ClawHub maximum is 52428800"
    fi
  fi

  skill_json_files+=("$dir/skill.json")
  source_dirs+=("$source_dir")
}

while IFS= read -r skill_md; do
  validate_skill "$skill_md"
done < <(find skills -name SKILL.md -not -path '*/deprecated/*' -not -path '*/tmp/*' | sort)

if [ "${#source_dirs[@]}" -gt 0 ]; then
  duplicates="$(printf '%s\n' "${source_dirs[@]}" | sort | uniq -d)"
  if [ -n "$duplicates" ]; then
    error "duplicate skill.json source_dir values: $duplicates"
  fi
fi

while IFS= read -r readme; do
  zh_readme="$(dirname "$readme")/README.zh-CN.md"
  if [ ! -f "$zh_readme" ]; then
    error "$readme missing sibling README.zh-CN.md"
  fi
done < <(find . -name README.md -not -path './.git/*' | sort)

while IFS= read -r catalog_target; do
  [ -z "$catalog_target" ] && continue
  if [ ! -e "docs/$catalog_target" ]; then
    error "docs/catalog.md links to missing path: $catalog_target"
  fi
done < <(sed -nE 's/.*\]\((\.\.\/skills\/[^)#]+).*/\1/p' docs/catalog.md)

validate_markdown_links() {
  local md="$1"
  local base target clean_target
  base="$(dirname "$md")"

  while IFS= read -r target; do
    [ -z "$target" ] && continue
    case "$target" in
      http://*|https://*|mailto:*|\#*) continue ;;
    esac

    clean_target="${target%%#*}"
    [ -z "$clean_target" ] && continue

    if [ ! -e "$base/$clean_target" ]; then
      error "$md links to missing path: $target"
    fi
  done < <(sed -nE 's/.*\[[^]]+\]\(([^)]+)\).*/\1/p' "$md")
}

while IFS= read -r md; do
  validate_markdown_links "$md"
done < <(find README.md README.zh-CN.md CONTEXT.md docs skills -name '*.md' -not -path '*/examples/*' | sort)

scan_targets=(README.md README.zh-CN.md CONTEXT.md docs/catalog.md skills)
for pattern in \
  '/Users/yangchao/' \
  '.env' \
  'CF_R2_SECRET_ACCESS_KEY' \
  'token' \
  'password' \
  '超哥' \
  'r2-config' \
  'content/outputs/'
do
  if rg -n --fixed-strings "$pattern" "${scan_targets[@]}" >/tmp/my-open-skills-validate-rg.txt 2>/dev/null; then
    note "Forbidden marker found for pattern: $pattern"
    cat /tmp/my-open-skills-validate-rg.txt >&2
    fail=1
  fi
done

if rg -n --hidden --glob '!*.png' --glob '!*.jpg' --glob '!*.jpeg' \
  '(clh_[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}|BEGIN (RSA|OPENSSH|EC) PRIVATE KEY)' \
  README.md README.zh-CN.md CONTEXT.md docs/catalog.md config skills >/tmp/my-open-skills-validate-rg.txt 2>/dev/null; then
  note "Forbidden credential-like marker found"
  cat /tmp/my-open-skills-validate-rg.txt >&2
  fail=1
fi

if find skills -path '*/.clawhub/*' -print -quit | grep -q .; then
  error "ClawHub local origin or lock state must not be committed inside public skill folders"
fi

for path in README.md CONTEXT.md docs/catalog.md docs/clawhub-releases.md docs/examples/wenchang-end-to-end-smoke.md skills/content/README.md skills/work/README.md skills/engineering/README.md skills/publishing/README.md; do
  if [ ! -f "$path" ]; then
    error "missing documented file $path"
  fi
done

if [ "$fail" -ne 0 ]; then
  exit 1
fi

note "validation passed"

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

skill_json_files=()
source_dirs=()

validate_skill() {
  local skill_md="$1"
  local dir slug source_dir
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

  if [ "$(jq -r '.status // empty' "$dir/skill.json")" = "ready" ]; then
    if [ ! -f "$dir/examples/minimal-input.md" ]; then
      error "$dir missing examples/minimal-input.md"
    fi

    if [ ! -f "$dir/examples/expected-output-notes.md" ]; then
      error "$dir missing examples/expected-output-notes.md"
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
done < <(find README.md CONTEXT.md docs skills -name '*.md' -not -path '*/examples/*' | sort)

scan_targets=(README.md CONTEXT.md docs/catalog.md skills)
for pattern in \
  '/Users/yangchao/' \
  '.env' \
  'CF_R2_SECRET_ACCESS_KEY' \
  'token' \
  'password' \
  'AI生命克劳德' \
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

for path in README.md CONTEXT.md docs/catalog.md docs/examples/wenchang-end-to-end-smoke.md skills/content/README.md skills/work/README.md skills/engineering/README.md skills/publishing/README.md; do
  if [ ! -f "$path" ]; then
    error "missing documented file $path"
  fi
done

if [ "$fail" -ne 0 ]; then
  exit 1
fi

note "validation passed"

#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo"

plan_file="config/clawhub-release-plan.json"
profile_file="config/clawhub-profile.json"
slug=""
run_once=0
finalize_release=0
push_release=0
confirmed=0
until_stage="verified"
poll_seconds=""
timeout_minutes=""

usage() {
  cat <<'EOF'
Usage:
  scripts/clawhub-watch-release.sh <slug> [--until public|verified]
  scripts/clawhub-watch-release.sh <slug> --once [--until public|verified]
  scripts/clawhub-watch-release.sh <slug> --finalize [--push --yes]

The watcher prints only state changes. The public milestone validates latest
metadata, categories, Topics, creator hooks, and an exact-version install. The
verified milestone additionally checks registry hashes, security workers, and
the generated Skill Card. --finalize promotes the plan and ledger to the
highest milestone reached.
EOF
}

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

need_command() {
  command -v "$1" >/dev/null 2>&1 || die "missing required command: $1"
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --once) run_once=1 ;;
    --finalize) finalize_release=1 ;;
    --push) push_release=1 ;;
    --yes) confirmed=1 ;;
    --until)
      shift
      [ "$#" -gt 0 ] || die "--until requires public or verified"
      until_stage="$1"
      ;;
    --poll-seconds)
      shift
      [ "$#" -gt 0 ] || die "--poll-seconds requires a value"
      poll_seconds="$1"
      ;;
    --timeout-minutes)
      shift
      [ "$#" -gt 0 ] || die "--timeout-minutes requires a value"
      timeout_minutes="$1"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    -*)
      die "unknown option: $1"
      ;;
    *)
      if [ -n "$slug" ]; then
        die "only one slug may be watched at a time"
      fi
      slug="$1"
      ;;
  esac
  shift
done

[ -n "$slug" ] || {
  usage >&2
  exit 1
}
[ -f "$plan_file" ] || die "missing $plan_file"
[ -f "$profile_file" ] || die "missing $profile_file"
[ "$until_stage" = "public" ] || [ "$until_stage" = "verified" ] ||
  die "--until must be public or verified"

for command_name in jq git clawhub curl shasum diff awk find sed sort uniq; do
  need_command "$command_name"
done

if [ "$push_release" -eq 1 ] && [ "$finalize_release" -ne 1 ]; then
  die "--push requires --finalize"
fi
if [ "$push_release" -eq 1 ] && [ "$confirmed" -ne 1 ]; then
  die "automatic commit and push require --push --yes"
fi
if [ "$finalize_release" -eq 1 ] && [ -n "$(git status --porcelain=v1 --untracked-files=all)" ]; then
  git status --short >&2
  die "cannot finalize with unrelated worktree changes"
fi

release_json="$(jq -ce --arg slug "$slug" '.releases[] | select(.slug == $slug)' "$plan_file" 2>/dev/null || true)"
[ -n "$release_json" ] || die "slug '$slug' is not present in $plan_file"

publisher_handle="$(jq -r '.publisher_handle' "$plan_file")"
source_ref="$(jq -r '.source_ref' "$plan_file")"
state_root="$(jq -r '.state_dir' "$plan_file")"
[ -n "$poll_seconds" ] || poll_seconds="$(jq -r '.poll_interval_seconds' "$plan_file")"
[ -n "$timeout_minutes" ] || timeout_minutes="$(jq -r '.timeout_minutes' "$plan_file")"

[[ "$poll_seconds" =~ ^[1-9][0-9]*$ ]] || die "poll interval must be a positive integer"
[[ "$timeout_minutes" =~ ^[1-9][0-9]*$ ]] || die "timeout must be a positive integer"

skill_path="$(jq -r '.path' <<<"$release_json")"
target_version="$(jq -r '.target_version' <<<"$release_json")"
order="$(jq -r '.order' <<<"$release_json")"
risk="$(jq -r '.risk' <<<"$release_json")"
categories_csv="$(jq -r '.categories | join(",")' <<<"$release_json")"
topics_csv="$(jq -r '.topics | join(",")' <<<"$release_json")"
description_suffix="$(jq -r '.description_suffix' "$profile_file")"
wechat_account="$(jq -r '.wechat_official_account' "$profile_file")"
x_url="$(jq -r '.x_url' "$profile_file")"
github_url="$(jq -r '.github_url' "$profile_file")"

[ -d "$skill_path" ] || die "missing skill path: $skill_path"

receipt_dir="$repo/$state_root/$slug/$target_version"
install_workdir="$receipt_dir/install"
installed_path="$install_workdir/skills/@$publisher_handle/$slug"
mkdir -p "$receipt_dir" "$install_workdir"

last_stage_file="$receipt_dir/last-stage.txt"
start_epoch="$(date +%s)"
deadline_epoch=$((start_epoch + timeout_minutes * 60))

emit_stage() {
  local stage="$1"
  local detail="$2"
  local previous=""
  [ -f "$last_stage_file" ] && previous="$(cat "$last_stage_file")"
  if [ "$stage|$detail" != "$previous" ]; then
    printf '%s\t%s\t%s\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" "$stage" "$detail"
    printf '%s' "$stage|$detail" >"$last_stage_file"
    jq -n \
      --arg schema "my-open-skills.clawhub-watch-status.v1" \
      --arg slug "$slug" \
      --arg version "$target_version" \
      --arg stage "$stage" \
      --arg detail "$detail" \
      --arg checked_at "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
      '{schema:$schema,slug:$slug,version:$version,stage:$stage,detail:$detail,checked_at:$checked_at}' \
      >"$receipt_dir/status.json"
  fi
}

wait_for_next_poll() {
  if [ "$run_once" -eq 1 ]; then
    exit 2
  fi
  if [ "$(date +%s)" -ge "$deadline_epoch" ]; then
    emit_stage "timeout" "verification did not complete within $timeout_minutes minutes"
    exit 3
  fi
  sleep "$poll_seconds"
}

format_epoch_ms_cst() {
  local epoch_ms="$1"
  local epoch_seconds="${epoch_ms%???}"
  if TZ=Asia/Shanghai date -r "$epoch_seconds" '+%Y-%m-%d %H:%M:%S CST' >/dev/null 2>&1; then
    TZ=Asia/Shanghai date -r "$epoch_seconds" '+%Y-%m-%d %H:%M:%S CST'
  else
    TZ=Asia/Shanghai date -d "@$epoch_seconds" '+%Y-%m-%d %H:%M:%S CST'
  fi
}

verify_registry_hashes() {
  local verify_json="$1"
  local hash_list="$receipt_dir/registry-hashes.tsv"
  local relative_path expected_hash actual_hash

  jq -r '.artifact.files[] | [.path, .sha256] | @tsv' "$verify_json" >"$hash_list"
  while IFS=$'\t' read -r relative_path expected_hash; do
    [ -f "$skill_path/$relative_path" ] || die "registry file is missing locally: $relative_path"
    actual_hash="$(shasum -a 256 "$skill_path/$relative_path" | awk '{print $1}')"
    [ "$actual_hash" = "$expected_hash" ] || die "registry hash mismatch for $relative_path"
  done <"$hash_list"
}

verify_public_page() {
  local public_html="$1"
  local category topic

  while IFS= read -r category; do
    grep -Fq "category=$category" "$public_html" || die "public page is missing category '$category'"
  done < <(jq -r --arg slug "$slug" '.releases[] | select(.slug == $slug) | .categories[]' "$plan_file")

  # ClawHub currently renders only the first four of up to five stored Topics.
  while IFS= read -r topic; do
    grep -Fq "topic=$topic" "$public_html" || die "public page is missing topic '$topic'"
  done < <(jq -r --arg slug "$slug" '.releases[] | select(.slug == $slug) | .topics[:4][]' "$plan_file")

  grep -Fq "$wechat_account" "$public_html" || die "public page is missing the WeChat creator hook"
  grep -Fq "$publisher_handle" "$public_html" || die "public page is missing the publisher handle"
  grep -Fq "github.com/$publisher_handle" "$public_html" || die "public page is missing the GitHub creator hook"
}

verify_installed_source() {
  local inspect_json="$1"
  local source_files="$receipt_dir/source-files.tsv"
  local expected_paths="$receipt_dir/source-paths.expected.txt"
  local installed_paths="$receipt_dir/source-paths.installed.txt"
  local relative_path expected_hash repository_hash installed_hash duplicate_paths

  jq -e '.version.files | type == "array"' "$inspect_json" >/dev/null ||
    die "inspect response is missing the version file manifest"
  jq -r '
    .version.files[]
    | select(
        .path != "skill-card.md"
        and .path != "_meta.json"
        and .path != ".clawhub"
        and (.path | startswith(".clawhub/") | not)
      )
    | [.path, .sha256]
    | @tsv
  ' "$inspect_json" >"$source_files"
  [ -s "$source_files" ] || die "version file manifest contains no installable source files"

  clawhub --workdir "$install_workdir" --dir skills --no-input install \
    "@$publisher_handle/$slug" --version "$target_version" --force >/dev/null

  : >"$expected_paths"
  while IFS=$'\t' read -r relative_path expected_hash; do
    case "$relative_path" in
      ""|/*|..|../*|*/..|*/../*) die "unsafe path in version file manifest: $relative_path" ;;
    esac
    [[ "$expected_hash" =~ ^[0-9a-f]{64}$ ]] ||
      die "invalid SHA-256 in version file manifest for $relative_path"

    [ -f "$skill_path/$relative_path" ] ||
      die "registry source file is missing from the repository: $relative_path"
    [ -f "$installed_path/$relative_path" ] ||
      die "registry source file is missing from the exact-version install: $relative_path"

    repository_hash="$(shasum -a 256 "$skill_path/$relative_path" | awk '{print $1}')"
    installed_hash="$(shasum -a 256 "$installed_path/$relative_path" | awk '{print $1}')"
    [ "$repository_hash" = "$expected_hash" ] ||
      die "repository hash differs from the registry for $relative_path"
    [ "$installed_hash" = "$expected_hash" ] ||
      die "installed hash differs from the registry for $relative_path"

    printf '%s\n' "$relative_path" >>"$expected_paths"
  done <"$source_files"

  duplicate_paths="$(LC_ALL=C sort "$expected_paths" | uniq -d)"
  [ -z "$duplicate_paths" ] || {
    printf '%s\n' "$duplicate_paths" >&2
    die "version file manifest contains duplicate source paths"
  }
  LC_ALL=C sort -u "$expected_paths" -o "$expected_paths"

  (
    cd "$installed_path"
    find . -type f \
      ! -path './skill-card.md' \
      ! -path './_meta.json' \
      ! -path './.clawhub/*' \
      -print |
      sed 's#^\./##' |
      LC_ALL=C sort
  ) >"$installed_paths"

  diff -u "$expected_paths" "$installed_paths" >"$receipt_dir/source-diff.txt" ||
    {
      cat "$receipt_dir/source-diff.txt" >&2
      die "installed source paths differ from the registry manifest"
    }

  grep -Fq "$description_suffix" "$installed_path/SKILL.md" || die "installed SKILL.md is missing the canonical description hook"
  grep -Fq "$wechat_account" "$installed_path/SKILL.md" || die "installed SKILL.md is missing the WeChat footer"
  grep -Fq "$x_url" "$installed_path/SKILL.md" || die "installed SKILL.md is missing the X footer"
  grep -Fq "$github_url" "$installed_path/SKILL.md" || die "installed SKILL.md is missing the GitHub footer"
  grep -Fq "github.com/$publisher_handle/my_open_skills/tree/main/$skill_path" "$installed_path/SKILL.md" ||
    die "installed SKILL.md is missing the source homepage"
}

replace_ledger_row() {
  local replacement="$1"
  local ledger_tmp
  ledger_tmp="$(mktemp)"
  awk -v target_slug="$slug" -v replacement="$replacement" '
    /^## Release Ledger$/ { in_ledger = 1 }
    /^Status values:/ { in_ledger = 0 }
    in_ledger && $0 ~ /^\| [0-9]+ \|/ && index($0, "`" target_slug "`") {
      print replacement
      replaced = 1
      next
    }
    { print }
    END {
      if (!replaced) {
        exit 42
      }
    }
  ' docs/clawhub-releases.md >"$ledger_tmp" || {
    rm -f "$ledger_tmp"
    die "could not update the release ledger row for $slug"
  }
  mv "$ledger_tmp" docs/clawhub-releases.md
}

commit_release_state() {
  local message="$1"
  "$repo/scripts/validate-skills.sh"
  git diff --check

  if [ "$push_release" -eq 1 ]; then
    current_branch="$(git branch --show-current)"
    [ "$current_branch" = "$source_ref" ] || die "current branch '$current_branch' does not match '$source_ref'"
    git add "$plan_file" docs/clawhub-releases.md
    git diff --cached --quiet && return 0
    git commit -m "$message"
    git push origin "$source_ref"
  fi
}

finalize_public() {
  local catalog_json="$1"
  local current_status public_at public_at_display published_at page_url replacement plan_tmp

  current_status="$(jq -r --arg slug "$slug" '.releases[] | select(.slug == $slug) | .status' "$plan_file")"
  case "$current_status" in
    public|verified) return 0 ;;
    submitted) ;;
    *) die "cannot promote $slug from '$current_status' to public" ;;
  esac

  public_at="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  public_at_display="$(TZ=Asia/Shanghai date '+%Y-%m-%d %H:%M CST')"
  published_at="$(format_epoch_ms_cst "$(jq -r '.latestVersion.createdAt' "$catalog_json")")"
  page_url="https://clawhub.ai/$publisher_handle/skills/$slug"
  replacement="| $order | \`$slug\` | \`$skill_path\` | $risk | \`$target_version\` | public ($public_at_display) | pending | $published_at | [page]($page_url) |"
  replace_ledger_row "$replacement"

  plan_tmp="$(mktemp)"
  jq \
    --arg slug "$slug" \
    --arg version "$target_version" \
    --arg public_at "$public_at" \
    '
      (.releases[] | select(.slug == $slug) | .status) = "public"
      | (.releases[] | select(.slug == $slug) | .remote_latest_version) = $version
      | (.releases[] | select(.slug == $slug) | .public_at) = $public_at
    ' "$plan_file" >"$plan_tmp"
  mv "$plan_tmp" "$plan_file"

  commit_release_state "Mark $slug $target_version public on ClawHub"
}

finalize_verified() {
  local verify_json="$1"
  local current_status verified_at verified_at_display published_at issue_count severity recommendation scan_text page_url
  local replacement plan_tmp

  current_status="$(jq -r --arg slug "$slug" '.releases[] | select(.slug == $slug) | .status' "$plan_file")"
  case "$current_status" in
    verified) return 0 ;;
    public) ;;
    *) die "cannot promote $slug from '$current_status' to verified" ;;
  esac

  verified_at="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  verified_at_display="$(TZ=Asia/Shanghai date '+%Y-%m-%d %H:%M CST')"
  published_at="$(format_epoch_ms_cst "$(jq -r '.createdAt' "$verify_json")")"
  issue_count="$(jq -r '.security.signals.skillSpector.issueCount // 0' "$verify_json")"
  severity="$(jq -r '.security.signals.skillSpector.severity // "UNKNOWN"' "$verify_json")"
  recommendation="$(jq -r '.security.signals.skillSpector.recommendation // "UNKNOWN"' "$verify_json")"
  page_url="$(jq -r '.pageUrl' "$verify_json")"
  scan_text="pass; static, VirusTotal, and SkillSpector clean; $recommendation/$severity ($issue_count notes)"
  [ "$issue_count" = "1" ] && scan_text="pass; static, VirusTotal, and SkillSpector clean; $recommendation/$severity (1 note)"

  replacement="| $order | \`$slug\` | \`$skill_path\` | $risk | \`$target_version\` | verified ($verified_at_display) | $scan_text | $published_at | [page]($page_url) |"
  replace_ledger_row "$replacement"

  plan_tmp="$(mktemp)"
  jq \
    --arg slug "$slug" \
    --arg version "$target_version" \
    --arg verified_at "$verified_at" \
    '
      (.releases[] | select(.slug == $slug) | .status) = "verified"
      | (.releases[] | select(.slug == $slug) | .remote_latest_version) = $version
      | (.releases[] | select(.slug == $slug) | .verified_at) = $verified_at
    ' "$plan_file" >"$plan_tmp"
  mv "$plan_tmp" "$plan_file"

  commit_release_state "Verify $slug $target_version on ClawHub"
}

while :; do
  inspect_tmp="$receipt_dir/inspect.tmp.json"
  inspect_json="$receipt_dir/inspect.json"
  inspect_error="$receipt_dir/inspect.error.txt"

  if clawhub inspect "@$publisher_handle/$slug" --version "$target_version" --files --json >"$inspect_tmp" 2>"$inspect_error"; then
    :
  else
    if grep -Eqi 'not found|404|pending[ ._-]*publication' "$inspect_error"; then
      emit_stage "pending-publication" "exact version is not inspectable yet"
      wait_for_next_poll
      continue
    fi
    cat "$inspect_error" >&2
    die "inspect failed for a reason other than pending publication"
  fi

  if [ -f "$inspect_tmp" ]; then
    mv "$inspect_tmp" "$inspect_json"
    latest_version="$(jq -r '.latestVersion.version // empty' "$inspect_json")"
    if [ "$latest_version" != "$target_version" ]; then
      emit_stage "pending-latest" "exact version exists but latest is '$latest_version'"
    else
      public_html="$receipt_dir/public-page.html"
      public_page_error="$receipt_dir/public-page.error.txt"
      if curl -fsSL "https://clawhub.ai/$publisher_handle/skills/$slug" -o "$public_html" 2>"$public_page_error"; then
        :
      else
        curl_status=$?
        if [ "$curl_status" -eq 22 ]; then
          emit_stage "pending-page" "public page is not available"
          wait_for_next_poll
          continue
        fi
        cat "$public_page_error" >&2
        die "public page request failed"
      fi

      if [ -f "$public_html" ]; then
        catalog_tmp="$receipt_dir/catalog.tmp.json"
        catalog_json="$receipt_dir/catalog.json"
        catalog_error="$receipt_dir/catalog.error.txt"
        if curl -fsSL "https://clawhub.ai/api/v1/skills/$slug?ownerHandle=$publisher_handle" -o "$catalog_tmp" 2>"$catalog_error"; then
          :
        else
          curl_status=$?
          if [ "$curl_status" -eq 22 ]; then
            emit_stage "pending-catalog" "public skill metadata is not available"
            wait_for_next_poll
            continue
          fi
          cat "$catalog_error" >&2
          die "public catalog request failed"
        fi
        jq . "$catalog_tmp" >/dev/null 2>&1 || die "public skill metadata is not valid JSON"
        mv "$catalog_tmp" "$catalog_json"
        expected_topics="$(jq -c '.topics' <<<"$release_json")"
        actual_topics="$(jq -c '.skill.topics // []' "$catalog_json")"
        [ "$actual_topics" = "$expected_topics" ] ||
          die "public API topics $actual_topics do not match planned topics $expected_topics"

        verify_public_page "$public_html"
        if [ ! -f "$receipt_dir/source-verified" ]; then
          verify_installed_source "$inspect_json"
          : >"$receipt_dir/source-verified"
        fi

        jq -n \
          --arg schema "my-open-skills.clawhub-public.v1" \
          --arg public_at "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
          --arg categories "$categories_csv" \
          --arg topics "$topics_csv" \
          --arg source_path "$skill_path" \
          --slurpfile catalog "$catalog_json" \
          --slurpfile inspect "$inspect_json" \
          '{
            schema: $schema,
            public_at: $public_at,
            categories: ($categories | split(",")),
            topics: ($topics | split(",")),
            source_path: $source_path,
            catalog: $catalog[0],
            inspect: $inspect[0]
          }' >"$receipt_dir/public.json"

        emit_stage "public" "latest metadata, categories, topics, creator hooks, and exact install passed"

        if [ "$finalize_release" -eq 1 ]; then
          finalize_public "$catalog_json"
        fi

        if [ "$until_stage" = "public" ]; then
          printf 'public receipt: %s\n' "$receipt_dir/public.json"
          exit 0
        fi

        verify_tmp="$receipt_dir/verify.tmp.json"
        verify_json="$receipt_dir/verify.json"
        verify_error="$receipt_dir/verify.error.txt"
        clawhub skill verify "@$publisher_handle/$slug" --version "$target_version" --json >"$verify_tmp" 2>"$verify_error" || true

        if ! jq . "$verify_tmp" >/dev/null 2>&1; then
          if grep -Eqi 'network request failed|fetch failed|econn|enotfound|etimedout|tls|certificate' "$verify_error"; then
            cat "$verify_error" >&2
            die "security verification request failed"
          fi
          emit_stage "pending-security" "verification result is not available"
        else
          mv "$verify_tmp" "$verify_json"
          decision="$(jq -r '.decision // "unknown"' "$verify_json")"
          if [ "$decision" != "pass" ]; then
            reasons="$(jq -r '(.reasons // ["pending"]) | join(",")' "$verify_json")"
            emit_stage "pending-verification" "$reasons"
          else
            verify_registry_hashes "$verify_json"
            verify_installed_source "$inspect_json"

            expected_card_hash="$(jq -r '.card.sha256 // empty' "$verify_json")"
            [ -n "$expected_card_hash" ] || die "verification passed without a Skill Card hash"
            [ -f "$installed_path/skill-card.md" ] || die "verified installation is missing skill-card.md"
            actual_card_hash="$(shasum -a 256 "$installed_path/skill-card.md" | awk '{print $1}')"
            [ "$actual_card_hash" = "$expected_card_hash" ] || die "installed Skill Card hash does not match the registry"

            jq -n \
              --arg schema "my-open-skills.clawhub-verification.v2" \
              --arg verified_at "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
              --arg categories "$categories_csv" \
              --arg topics "$topics_csv" \
              --arg source_path "$skill_path" \
              --arg card_sha256 "$actual_card_hash" \
              --slurpfile catalog "$catalog_json" \
              --slurpfile inspect "$inspect_json" \
              --slurpfile verify "$verify_json" \
              '{
                schema: $schema,
                verified_at: $verified_at,
                categories: ($categories | split(",")),
                topics: ($topics | split(",")),
                source_path: $source_path,
                card_sha256: $card_sha256,
                catalog: $catalog[0],
                inspect: $inspect[0],
                verify: $verify[0]
              }' >"$receipt_dir/verification.json"

            emit_stage "verified" "categories, topics, install, hashes, security, and Skill Card passed"

            if [ "$finalize_release" -eq 1 ]; then
              finalize_verified "$verify_json"
            fi

            printf 'verification receipt: %s\n' "$receipt_dir/verification.json"
            exit 0
          fi
        fi
      fi
    fi
  fi

  wait_for_next_poll
done

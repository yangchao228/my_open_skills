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
poll_seconds=""
timeout_minutes=""

usage() {
  cat <<'EOF'
Usage:
  scripts/clawhub-watch-release.sh <slug>
  scripts/clawhub-watch-release.sh <slug> --once
  scripts/clawhub-watch-release.sh <slug> --finalize [--push --yes]

The watcher prints only state changes. It waits for public latest metadata,
validates public categories and creator hooks, installs the exact version,
compares source and registry hashes, waits for full security verification and
the generated Skill Card, then writes a machine-readable receipt.
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

for command_name in jq git clawhub curl shasum diff rg awk; do
  need_command "$command_name"
done

if [ "$push_release" -eq 1 ] && [ "$finalize_release" -ne 1 ]; then
  die "--push requires --finalize"
fi
if [ "$push_release" -eq 1 ] && [ "$confirmed" -ne 1 ]; then
  die "automatic commit and push require --push --yes"
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
  local category

  while IFS= read -r category; do
    grep -Fq "category=$category" "$public_html" || die "public page is missing category '$category'"
  done < <(jq -r --arg slug "$slug" '.releases[] | select(.slug == $slug) | .categories[]' "$plan_file")

  grep -Fq "$wechat_account" "$public_html" || die "public page is missing the WeChat creator hook"
  grep -Fq "$publisher_handle" "$public_html" || die "public page is missing the publisher handle"
  grep -Fq "github.com/$publisher_handle" "$public_html" || die "public page is missing the GitHub creator hook"
}

verify_installed_source() {
  clawhub --workdir "$install_workdir" --dir skills --no-input install \
    "@$publisher_handle/$slug" --version "$target_version" --force >/dev/null

  diff -qr \
    --exclude=skill-card.md \
    --exclude=_meta.json \
    --exclude=.clawhub \
    "$skill_path" "$installed_path" >"$receipt_dir/source-diff.txt" ||
    {
      cat "$receipt_dir/source-diff.txt" >&2
      die "installed source differs from the repository"
    }

  grep -Fq "$description_suffix" "$installed_path/SKILL.md" || die "installed SKILL.md is missing the canonical description hook"
  grep -Fq "$wechat_account" "$installed_path/SKILL.md" || die "installed SKILL.md is missing the WeChat footer"
  grep -Fq "$x_url" "$installed_path/SKILL.md" || die "installed SKILL.md is missing the X footer"
  grep -Fq "$github_url" "$installed_path/SKILL.md" || die "installed SKILL.md is missing the GitHub footer"
  grep -Fq "github.com/$publisher_handle/my_open_skills/tree/main/$skill_path" "$installed_path/SKILL.md" ||
    die "installed SKILL.md is missing the source homepage"
}

finalize_ledger() {
  local verify_json="$1"
  local verified_at published_at issue_count severity recommendation scan_text page_url
  local replacement ledger_tmp plan_tmp

  if [ -n "$(git status --porcelain=v1 --untracked-files=all)" ]; then
    git status --short >&2
    die "cannot finalize with unrelated worktree changes"
  fi

  verified_at="$(date '+%Y-%m-%d %H:%M CST')"
  published_at="$(format_epoch_ms_cst "$(jq -r '.createdAt' "$verify_json")")"
  issue_count="$(jq -r '.security.signals.skillSpector.issueCount // 0' "$verify_json")"
  severity="$(jq -r '.security.signals.skillSpector.severity // "UNKNOWN"' "$verify_json")"
  recommendation="$(jq -r '.security.signals.skillSpector.recommendation // "UNKNOWN"' "$verify_json")"
  page_url="$(jq -r '.pageUrl' "$verify_json")"
  scan_text="pass; static, VirusTotal, and SkillSpector clean; $recommendation/$severity ($issue_count notes)"
  [ "$issue_count" = "1" ] && scan_text="pass; static, VirusTotal, and SkillSpector clean; $recommendation/$severity (1 note)"

  replacement="| $order | \`$slug\` | \`$skill_path\` | $risk | \`$target_version\` | verified ($verified_at) | $scan_text | $published_at | [page]($page_url) |"
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

  plan_tmp="$(mktemp)"
  jq --arg slug "$slug" --arg version "$target_version" '
    (.releases[] | select(.slug == $slug) | .status) = "verified"
    | (.releases[] | select(.slug == $slug) | .remote_latest_version) = $version
  ' "$plan_file" >"$plan_tmp"
  mv "$plan_tmp" "$plan_file"

  "$repo/scripts/validate-skills.sh"
  git diff --check

  if [ "$push_release" -eq 1 ]; then
    current_branch="$(git branch --show-current)"
    [ "$current_branch" = "$source_ref" ] || die "current branch '$current_branch' does not match '$source_ref'"
    git add "$plan_file" docs/clawhub-releases.md
    git commit -m "Verify $slug $target_version on ClawHub"
    git push origin "$source_ref"
  fi
}

while :; do
  inspect_tmp="$receipt_dir/inspect.tmp.json"
  inspect_json="$receipt_dir/inspect.json"
  inspect_error="$receipt_dir/inspect.error.txt"

  if ! clawhub inspect "@$publisher_handle/$slug" --version "$target_version" --files --json >"$inspect_tmp" 2>"$inspect_error"; then
    emit_stage "pending-publication" "exact version is not inspectable yet"
  else
    mv "$inspect_tmp" "$inspect_json"
    latest_version="$(jq -r '.latestVersion.version // empty' "$inspect_json")"
    if [ "$latest_version" != "$target_version" ]; then
      emit_stage "pending-latest" "exact version exists but latest is '$latest_version'"
    else
      public_html="$receipt_dir/public-page.html"
      if ! curl -fsSL "https://clawhub.ai/$publisher_handle/skills/$slug" -o "$public_html"; then
        emit_stage "pending-page" "public page is not available"
      else
        verify_public_page "$public_html"
        if [ ! -f "$receipt_dir/source-verified" ]; then
          verify_installed_source
          : >"$receipt_dir/source-verified"
        fi

        verify_tmp="$receipt_dir/verify.tmp.json"
        verify_json="$receipt_dir/verify.json"
        verify_error="$receipt_dir/verify.error.txt"
        if clawhub skill verify "@$publisher_handle/$slug" --version "$target_version" --json >"$verify_tmp" 2>"$verify_error"; then
          :
        fi

        if ! jq . "$verify_tmp" >/dev/null 2>&1; then
          emit_stage "pending-security" "verification result is not available"
        else
          mv "$verify_tmp" "$verify_json"
          decision="$(jq -r '.decision // "unknown"' "$verify_json")"
          if [ "$decision" != "pass" ]; then
            reasons="$(jq -r '(.reasons // ["pending"]) | join(",")' "$verify_json")"
            emit_stage "pending-verification" "$reasons"
          else
            verify_registry_hashes "$verify_json"
            verify_installed_source

            expected_card_hash="$(jq -r '.card.sha256 // empty' "$verify_json")"
            [ -n "$expected_card_hash" ] || die "verification passed without a Skill Card hash"
            [ -f "$installed_path/skill-card.md" ] || die "verified installation is missing skill-card.md"
            actual_card_hash="$(shasum -a 256 "$installed_path/skill-card.md" | awk '{print $1}')"
            [ "$actual_card_hash" = "$expected_card_hash" ] || die "installed Skill Card hash does not match the registry"

            jq -n \
              --arg schema "my-open-skills.clawhub-verification.v1" \
              --arg verified_at "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
              --arg categories "$categories_csv" \
              --arg source_path "$skill_path" \
              --arg card_sha256 "$actual_card_hash" \
              --slurpfile inspect "$inspect_json" \
              --slurpfile verify "$verify_json" \
              '{
                schema: $schema,
                verified_at: $verified_at,
                categories: ($categories | split(",")),
                source_path: $source_path,
                card_sha256: $card_sha256,
                inspect: $inspect[0],
                verify: $verify[0]
              }' >"$receipt_dir/verification.json"

            emit_stage "verified" "public metadata, install, hashes, security, and Skill Card passed"

            if [ "$finalize_release" -eq 1 ]; then
              finalize_ledger "$verify_json"
            fi

            printf 'verification receipt: %s\n' "$receipt_dir/verification.json"
            exit 0
          fi
        fi
      fi
    fi
  fi

  if [ "$run_once" -eq 1 ]; then
    exit 2
  fi
  if [ "$(date +%s)" -ge "$deadline_epoch" ]; then
    emit_stage "timeout" "verification did not complete within $timeout_minutes minutes"
    exit 3
  fi
  sleep "$poll_seconds"
done

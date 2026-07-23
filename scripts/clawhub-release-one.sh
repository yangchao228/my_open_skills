#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo"

plan_file="config/clawhub-release-plan.json"
publish_live=0
confirmed=0
watch_release=0
watch_until="verified"
watch_option_count=0
finalize_release=0
push_release=0
slug=""
release_lock=""

usage() {
  cat <<'EOF'
Usage:
  scripts/clawhub-release-one.sh <slug>
  scripts/clawhub-release-one.sh <slug> --publish --yes [--watch-public | --watch]

Default mode is a fail-closed dry-run. Live publication requires both
--publish and --yes. A successful upload is recorded and pushed as submitted,
then the command exits. --watch-public waits for public page/install readiness;
--watch waits through security and Skill Card verification. Legacy --finalize
and --push flags remain accepted with --watch.
EOF
}

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

need_command() {
  command -v "$1" >/dev/null 2>&1 || die "missing required command: $1"
}

cleanup_release_lock() {
  if [ -n "$release_lock" ]; then
    rmdir "$release_lock" 2>/dev/null || true
  fi
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

record_submission() {
  local submitted_at submitted_at_display replacement plan_tmp page_url

  if [ -n "$(git status --porcelain=v1 --untracked-files=all)" ]; then
    git status --short >&2
    die "cannot record submission with unrelated worktree changes"
  fi

  submitted_at="$(jq -r '.submitted_at' "$receipt_dir/submission.json")"
  submitted_at_display="$(TZ=Asia/Shanghai date '+%Y-%m-%d %H:%M CST')"
  page_url="https://clawhub.ai/$publisher_handle/skills/$slug"
  replacement="| $order | \`$slug\` | \`$skill_path\` | $risk | \`$target_version\` | submitted ($submitted_at_display) | pending | — | [page]($page_url) |"
  replace_ledger_row "$replacement"

  plan_tmp="$(mktemp)"
  jq \
    --arg slug "$slug" \
    --arg submitted_at "$submitted_at" \
    --arg source_commit "$head_commit" \
    '
      (.releases[] | select(.slug == $slug) | .status) = "submitted"
      | (.releases[] | select(.slug == $slug) | .submitted_at) = $submitted_at
      | (.releases[] | select(.slug == $slug) | .source_commit) = $source_commit
    ' "$plan_file" >"$plan_tmp"
  mv "$plan_tmp" "$plan_file"

  "$repo/scripts/validate-skills.sh"
  git diff --check
  git add "$plan_file" docs/clawhub-releases.md
  git commit -m "Submit $slug $target_version to ClawHub"
  git push origin "$source_ref"
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --publish) publish_live=1 ;;
    --yes) confirmed=1 ;;
    --watch)
      watch_release=1
      watch_until="verified"
      watch_option_count=$((watch_option_count + 1))
      ;;
    --watch-public)
      watch_release=1
      watch_until="public"
      watch_option_count=$((watch_option_count + 1))
      ;;
    --finalize) finalize_release=1 ;;
    --push) push_release=1 ;;
    -h|--help)
      usage
      exit 0
      ;;
    -*)
      die "unknown option: $1"
      ;;
    *)
      if [ -n "$slug" ]; then
        die "only one slug may be released at a time"
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
[ "$watch_option_count" -le 1 ] || die "use either --watch-public or --watch"

for command_name in jq git clawhub curl shasum diff; do
  need_command "$command_name"
done

if [ "$publish_live" -eq 0 ] && { [ "$watch_release" -eq 1 ] || [ "$finalize_release" -eq 1 ] || [ "$push_release" -eq 1 ]; }; then
  die "--watch-public, --watch, --finalize, and --push require --publish"
fi
if [ "$publish_live" -eq 1 ] && [ "$confirmed" -ne 1 ]; then
  die "live publication requires --publish --yes"
fi
if [ "$finalize_release" -eq 1 ] && [ "$watch_release" -ne 1 ]; then
  die "--finalize requires --watch"
fi
if [ "$push_release" -eq 1 ] && [ "$finalize_release" -ne 1 ]; then
  die "--push requires --finalize"
fi

release_json="$(jq -ce --arg slug "$slug" '.releases[] | select(.slug == $slug)' "$plan_file" 2>/dev/null || true)"
[ -n "$release_json" ] || die "slug '$slug' is not present in $plan_file"

publisher_handle="$(jq -r '.publisher_handle' "$plan_file")"
source_repository="$(jq -r '.source_repository' "$plan_file")"
source_ref="$(jq -r '.source_ref' "$plan_file")"
state_root="$(jq -r '.state_dir' "$plan_file")"
poll_seconds="$(jq -r '.poll_interval_seconds' "$plan_file")"
timeout_minutes="$(jq -r '.timeout_minutes' "$plan_file")"

skill_path="$(jq -r '.path' <<<"$release_json")"
display_name="$(jq -r '.display_name' <<<"$release_json")"
risk="$(jq -r '.risk' <<<"$release_json")"
order="$(jq -r '.order' <<<"$release_json")"
release_status="$(jq -r '.status' <<<"$release_json")"
configured_remote="$(jq -r '.remote_latest_version // ""' <<<"$release_json")"
target_version="$(jq -r '.target_version' <<<"$release_json")"
categories_csv="$(jq -r '.categories | join(",")' <<<"$release_json")"
topics_csv="$(jq -r '.topics | join(",")' <<<"$release_json")"
tags_csv="$(jq -r '.tags | join(",")' <<<"$release_json")"
changelog="$(jq -r '.changelog' <<<"$release_json")"

[ -d "$skill_path" ] || die "missing skill path: $skill_path"
[ -f "$skill_path/SKILL.md" ] || die "missing $skill_path/SKILL.md"
[ "$release_status" = "planned" ] || die "$slug@$target_version has release status '$release_status'; only planned entries may be published"

blocking_prior="$(
  jq -ce --arg slug "$slug" '
    def status_rank($status):
      if $status == "planned" then 0
      elif $status == "submitted" then 1
      elif $status == "public" then 2
      elif $status == "verified" then 3
      else 4
      end;
    (.releases[] | select(.slug == $slug) | .order) as $target_order
    | .release_gate_policy as $gate_policy
    | [
        .releases[]
        | select(.order < $target_order)
        | select(.status != "blocked")
        | select(status_rank(.status) < status_rank($gate_policy[.risk]))
      ]
    | sort_by(.order)
    | .[0] // empty
  ' "$plan_file" 2>/dev/null || true
)"
if [ -n "$blocking_prior" ]; then
  blocking_slug="$(jq -r '.slug' <<<"$blocking_prior")"
  blocking_risk="$(jq -r '.risk' <<<"$blocking_prior")"
  blocking_status="$(jq -r '.status' <<<"$blocking_prior")"
  required_gate="$(jq -r --arg risk "$blocking_risk" '.release_gate_policy[$risk]' "$plan_file")"
  die "release order is blocked by '$blocking_slug' ($blocking_risk, $blocking_status); required gate is '$required_gate'"
fi

local_version="$(sed -n 's/^version:[[:space:]]*//p' "$skill_path/SKILL.md" | head -n 1)"
[ "$local_version" = "$target_version" ] || die "$skill_path/SKILL.md version '$local_version' does not match planned target '$target_version'"

if [ -n "$(git status --porcelain=v1 --untracked-files=all)" ]; then
  git status --short >&2
  die "worktree must be clean before ClawHub dry-run or publication"
fi

current_branch="$(git branch --show-current)"
[ "$current_branch" = "$source_ref" ] || die "current branch '$current_branch' does not match source_ref '$source_ref'"

head_commit="$(git rev-parse HEAD)"
upstream_commit="$(git rev-parse '@{upstream}' 2>/dev/null || true)"
[ -n "$upstream_commit" ] || die "current branch has no upstream"
[ "$head_commit" = "$upstream_commit" ] || die "HEAD $head_commit is not pushed to upstream $upstream_commit"

"$repo/scripts/validate-skills.sh"
git diff --check

authenticated_handle="$(clawhub whoami)"
[ "$authenticated_handle" = "$publisher_handle" ] || die "authenticated publisher '$authenticated_handle' does not match '$publisher_handle'"

receipt_dir="$repo/$state_root/$slug/$target_version"
mkdir -p "$receipt_dir"
remote_json="$receipt_dir/remote-before.json"
remote_error="$receipt_dir/remote-before.error.txt"
current_remote=""

if clawhub inspect "@$publisher_handle/$slug" --json >"$remote_json" 2>"$remote_error"; then
  current_remote="$(jq -r '.latestVersion.version // empty' "$remote_json")"
else
  if grep -Eqi 'not found|404' "$remote_error"; then
    : >"$remote_json"
    current_remote=""
  else
    cat "$remote_error" >&2
    die "remote inspection failed; refusing to treat an unknown error as an absent slug"
  fi
fi

if [ "$current_remote" = "$target_version" ]; then
  die "$slug@$target_version already exists remotely; run scripts/clawhub-watch-release.sh $slug instead of republishing"
fi
[ "$current_remote" = "$configured_remote" ] || die "remote latest '$current_remote' does not match configured baseline '$configured_remote'"

if [ -z "$configured_remote" ]; then
  expected_target="1.0.0"
else
  IFS=. read -r version_major version_minor version_patch <<<"$configured_remote"
  expected_target="$version_major.$version_minor.$((version_patch + 1))"
fi
[ "$target_version" = "$expected_target" ] || die "target '$target_version' is not the expected next version '$expected_target'"

publish_args=(
  skill publish "$skill_path"
  --slug "$slug"
  --name "$display_name"
  --owner "$publisher_handle"
  --version "$target_version"
  --changelog "$changelog"
  --tags "$tags_csv"
  --categories "$categories_csv"
  --topics "$topics_csv"
  --source-repo "$source_repository"
  --source-commit "$head_commit"
  --source-ref "$source_ref"
  --source-path "$skill_path"
)

dry_run_tmp="$receipt_dir/dry-run.tmp.json"
dry_run_json="$receipt_dir/dry-run.json"
preflight_json="$receipt_dir/preflight.json"
clawhub "${publish_args[@]}" --dry-run --json >"$dry_run_tmp"
jq -e '.ok == true and (.status == "would-publish" or .status == "already-published")' "$dry_run_tmp" >/dev/null ||
  die "ClawHub dry-run did not return an accepted plan"
mv "$dry_run_tmp" "$dry_run_json"

jq -n \
  --arg schema "my-open-skills.clawhub-preflight.v2" \
  --arg checked_at "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
  --arg source_commit "$head_commit" \
  --argjson release "$release_json" \
  --slurpfile dry_run "$dry_run_json" \
  '{
    schema: $schema,
    checked_at: $checked_at,
    source_commit: $source_commit,
    requested: {
      order: $release.order,
      slug: $release.slug,
      version: $release.target_version,
      categories: $release.categories,
      topics: $release.topics,
      tags: $release.tags,
      changelog: $release.changelog
    },
    dry_run: $dry_run[0]
  }' >"$preflight_json"

printf 'dry-run passed: %s@%s (risk=%s)\n' "$slug" "$target_version" "$risk"
printf 'categories: %s\n' "$categories_csv"
printf 'topics: %s\n' "$topics_csv"
printf 'tags: %s\n' "$tags_csv"
jq '{ok,status,slug,version,latestVersion,fileCount,fingerprint}' "$dry_run_json"
printf 'preflight receipt: %s\n' "$preflight_json"

if [ "$publish_live" -eq 0 ]; then
  printf 'live publication not requested; rerun with --publish --yes\n'
  exit 0
fi

mkdir -p "$repo/$state_root"
release_lock="$repo/$state_root/.publish-lock"
if ! mkdir "$release_lock" 2>/dev/null; then
  die "another live ClawHub publication may be running; inspect $release_lock before retrying"
fi
trap cleanup_release_lock EXIT
trap 'exit 130' HUP INT TERM

publish_tmp="$receipt_dir/publish.tmp.json"
publish_json="$receipt_dir/publish.json"
clawhub "${publish_args[@]}" --json >"$publish_tmp"
jq -e '.ok == true and .status == "published"' "$publish_tmp" >/dev/null ||
  die "ClawHub did not confirm publication"
mv "$publish_tmp" "$publish_json"

jq -n \
  --arg schema "my-open-skills.clawhub-submission.v2" \
  --arg submitted_at "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" \
  --arg source_commit "$head_commit" \
  --slurpfile preflight "$preflight_json" \
  --slurpfile publish "$publish_json" \
  '{
    schema: $schema,
    submitted_at: $submitted_at,
    source_commit: $source_commit,
    preflight: $preflight[0],
    publish: $publish[0]
  }' >"$receipt_dir/submission.json"

record_submission

printf 'submitted: %s@%s\n' "$slug" "$target_version"
printf 'submission receipt: %s\n' "$receipt_dir/submission.json"

if [ "$watch_release" -eq 1 ]; then
  watch_args=(
    "$slug"
    --until "$watch_until"
    --poll-seconds "$poll_seconds"
    --timeout-minutes "$timeout_minutes"
    --finalize
    --push
    --yes
  )
  "$repo/scripts/clawhub-watch-release.sh" "${watch_args[@]}"
  exit $?
fi

printf 'foreground release is complete; ClawHub public/security/Card workers continue asynchronously\n'
printf 'background reconciliation will promote submitted -> public -> verified\n'

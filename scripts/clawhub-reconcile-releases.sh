#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo"

plan_file="config/clawhub-release-plan.json"
watcher="$repo/scripts/clawhub-watch-release.sh"

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

[ -f "$plan_file" ] || die "missing $plan_file"
[ -x "$watcher" ] || die "missing executable watcher: $watcher"
command -v jq >/dev/null 2>&1 || die "missing required command: jq"
command -v git >/dev/null 2>&1 || die "missing required command: git"

"$repo/scripts/validate-skills.sh"

queue_file="$(mktemp)"
trap 'rm -f "$queue_file"' EXIT
jq -r '
  [
    .releases[]
    | select(.status == "submitted" or .status == "public")
  ]
  | sort_by(.order)
  | .[]
  | [.slug, .status]
  | @tsv
' "$plan_file" >"$queue_file"

if [ ! -s "$queue_file" ]; then
  printf 'no submitted or public ClawHub releases need reconciliation\n'
  exit 0
fi

if [ -n "$(git status --porcelain=v1 --untracked-files=all)" ]; then
  git status --short >&2
  die "worktree must be clean before release reconciliation"
fi

source_ref="$(jq -r '.source_ref' "$plan_file")"
current_branch="$(git branch --show-current)"
[ "$current_branch" = "$source_ref" ] ||
  die "current branch '$current_branch' does not match source_ref '$source_ref'"

failed=0
while IFS=$'\t' read -r slug status; do
  until_stage="public"
  [ "$status" = "public" ] && until_stage="verified"

  printf 'reconcile: %s (%s -> %s)\n' "$slug" "$status" "$until_stage"
  if "$watcher" "$slug" --once --until "$until_stage" --finalize --push --yes; then
    printf 'promoted: %s -> %s\n' "$slug" "$until_stage"
  else
    result=$?
    if [ "$result" -eq 2 ]; then
      printf 'pending: %s has not reached %s\n' "$slug" "$until_stage"
    else
      printf 'failed: %s reconciliation exited %s\n' "$slug" "$result" >&2
      failed=1
    fi
  fi
done <"$queue_file"

exit "$failed"

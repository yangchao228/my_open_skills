#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo"

find skills -name SKILL.md \
  -not -path '*/.git/*' \
  -not -path '*/deprecated/*' \
  -not -path '*/tmp/*' \
  | sort \
  | while read -r skill_md; do
    dir="$(dirname "$skill_md")"
    slug="$(basename "$dir")"
    category="$(printf '%s\n' "$dir" | awk -F/ '{print $2}')"
    printf '%s\t%s\t%s\n' "$category" "$slug" "$skill_md"
  done

#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
verifier="$repo/scripts/verify-clawhub-installed-source.sh"

fail() {
  printf 'test failure: %s\n' "$*" >&2
  exit 1
}

assert_error_contains() {
  local expected="$1"
  local error_file="$2"
  grep -Fq "$expected" "$error_file" ||
    {
      cat "$error_file" >&2
      fail "expected error containing: $expected"
    }
}

[ -x "$verifier" ] || fail "verifier is not executable: $verifier"
for command_name in jq shasum grep mktemp; do
  command -v "$command_name" >/dev/null 2>&1 || fail "missing required command: $command_name"
done

fixture_root="$(mktemp -d)"
trap 'rm -rf "$fixture_root"' EXIT

repository_skill="$fixture_root/repository"
installed_skill="$fixture_root/installed"
inspect_json="$fixture_root/inspect.json"
mkdir -p \
  "$repository_skill/scripts" \
  "$installed_skill/scripts" \
  "$installed_skill/.clawhub"

printf '%s\n' '# Fixture skill' >"$repository_skill/SKILL.md"
printf '%s\n' 'printf "fixture\n"' >"$repository_skill/scripts/run.sh"
printf '%s\n' 'LOCAL_ONLY=example' >"$repository_skill/config.example"
cp "$repository_skill/SKILL.md" "$installed_skill/SKILL.md"
cp "$repository_skill/scripts/run.sh" "$installed_skill/scripts/run.sh"
printf '%s\n' '# Generated card' >"$installed_skill/skill-card.md"
printf '%s\n' '{}' >"$installed_skill/_meta.json"
printf '%s\n' '{}' >"$installed_skill/.clawhub/origin.json"

skill_hash="$(shasum -a 256 "$repository_skill/SKILL.md" | awk '{print $1}')"
run_hash="$(shasum -a 256 "$repository_skill/scripts/run.sh" | awk '{print $1}')"
card_hash="$(shasum -a 256 "$installed_skill/skill-card.md" | awk '{print $1}')"
jq -n \
  --arg skill_hash "$skill_hash" \
  --arg run_hash "$run_hash" \
  --arg card_hash "$card_hash" \
  '{
    version: {
      files: [
        {path:"SKILL.md",sha256:$skill_hash},
        {path:"scripts/run.sh",sha256:$run_hash},
        {path:"skill-card.md",sha256:$card_hash}
      ]
    }
  }' >"$inspect_json"

"$verifier" \
  "$repository_skill" \
  "$installed_skill" \
  "$inspect_json" \
  "$fixture_root/receipts/pass"

printf '%s\n' '# Tampered install' >"$installed_skill/SKILL.md"
if "$verifier" \
  "$repository_skill" \
  "$installed_skill" \
  "$inspect_json" \
  "$fixture_root/receipts/hash-mismatch" \
  2>"$fixture_root/hash-mismatch.error.txt"; then
  fail "installed hash mismatch unexpectedly passed"
fi
assert_error_contains \
  "installed hash differs from the registry for SKILL.md" \
  "$fixture_root/hash-mismatch.error.txt"
cp "$repository_skill/SKILL.md" "$installed_skill/SKILL.md"

printf '%s\n' 'unexpected' >"$installed_skill/unexpected.txt"
if "$verifier" \
  "$repository_skill" \
  "$installed_skill" \
  "$inspect_json" \
  "$fixture_root/receipts/extra-path" \
  2>"$fixture_root/extra-path.error.txt"; then
  fail "undeclared installed source path unexpectedly passed"
fi
assert_error_contains \
  "installed source paths differ from the registry manifest" \
  "$fixture_root/extra-path.error.txt"

printf 'ClawHub installed-source fixture tests passed\n'

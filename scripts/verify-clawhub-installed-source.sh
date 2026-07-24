#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/verify-clawhub-installed-source.sh \
    <repository-skill-dir> <installed-skill-dir> <inspect-json> <receipt-dir>

Verify that every registry source file has the same SHA-256 in the repository
and exact-version install, then reject installed source paths not declared by
the registry manifest. ClawHub-generated metadata and Skill Cards are ignored.
EOF
}

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

need_command() {
  command -v "$1" >/dev/null 2>&1 || die "missing required command: $1"
}

[ "$#" -eq 4 ] || {
  usage >&2
  exit 1
}

repository_skill="$1"
installed_skill="$2"
inspect_json="$3"
receipt_dir="$4"

[ -d "$repository_skill" ] || die "missing repository skill directory: $repository_skill"
[ -d "$installed_skill" ] || die "missing installed skill directory: $installed_skill"
[ -f "$inspect_json" ] || die "missing inspect JSON: $inspect_json"
mkdir -p "$receipt_dir"

for command_name in jq shasum awk find sed sort uniq diff; do
  need_command "$command_name"
done

source_files="$receipt_dir/source-files.tsv"
expected_paths="$receipt_dir/source-paths.expected.txt"
installed_paths="$receipt_dir/source-paths.installed.txt"

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

: >"$expected_paths"
while IFS=$'\t' read -r relative_path expected_hash; do
  case "$relative_path" in
    ""|/*|..|../*|*/..|*/../*) die "unsafe path in version file manifest: $relative_path" ;;
  esac
  [[ "$expected_hash" =~ ^[0-9a-f]{64}$ ]] ||
    die "invalid SHA-256 in version file manifest for $relative_path"

  [ -f "$repository_skill/$relative_path" ] ||
    die "registry source file is missing from the repository: $relative_path"
  [ -f "$installed_skill/$relative_path" ] ||
    die "registry source file is missing from the exact-version install: $relative_path"

  repository_hash="$(shasum -a 256 "$repository_skill/$relative_path" | awk '{print $1}')"
  installed_hash="$(shasum -a 256 "$installed_skill/$relative_path" | awk '{print $1}')"
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
  cd "$installed_skill"
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

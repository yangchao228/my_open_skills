# Validation

Run:

```bash
./scripts/list-skills.sh
./scripts/validate-skills.sh
```

The validation script checks:

- every `SKILL.md` has frontmatter
- every frontmatter contains `name` and `description`
- every skill folder has `skill.json`
- every `skill.json` is valid JSON
- `skill.json.source_dir` matches the real folder
- `skill.json.source_dir` values are unique
- every first-phase public skill has example files
- every `README.md` has a sibling `README.zh-CN.md`
- catalog skill links point to real paths
- repository Markdown links point to real local files or directories
- public files do not contain common private-path or credential markers
- every `ready` skill appears exactly once in `config/clawhub-release-plan.json`
- every release has a valid ordered status (`planned`, `submitted`, `public`, `verified`, or reasoned `blocked`), risk, next semver, one to three explicit non-`other` categories, three to five topics, tags, and a changelog
- risk gates remain fixed at low=`submitted`, medium=`public`, and high=`verified`
- every topic uses lowercase ASCII kebab-case, stays within ClawHub's 48-character limit, avoids reserved platform slugs, and does not duplicate a broad category
- release-plan categories, topics, order, source path, risk, and target version match `docs/clawhub-releases.md`
- every ready skill has the canonical creator suffix and footer exactly once, a source homepage, and a package under ClawHub's size limit
- local ClawHub state is ignored, all release scripts remain executable, and the 15-minute reconciliation workflow stays pinned

For a safe ClawHub release preflight, run:

```bash
# Dry-run only. Requires a clean main branch whose HEAD matches origin/main.
./scripts/clawhub-release-one.sh <slug>

# Live publication requires both explicit flags, records submitted, then returns.
./scripts/clawhub-release-one.sh <slug> --publish --yes

# Optional foreground waits.
./scripts/clawhub-release-one.sh <slug> --publish --yes --watch-public
./scripts/clawhub-release-one.sh <slug> --publish --yes --watch
```

The watcher resumes independently with `./scripts/clawhub-watch-release.sh <slug> --until public|verified`. It records transient receipts under the ignored `.clawhub-release-state/` directory and reports only state changes. `./scripts/clawhub-reconcile-releases.sh` promotes submitted releases to public and public releases to verified; the scheduled GitHub Action invokes it every 15 minutes and never uploads a new skill.

ClawHub currently allows at most five Topics of at most 48 characters each and normalizes them for catalog discovery. The repository uses a stricter lowercase ASCII kebab-case policy for stable CLI and Markdown handling. Update the release policy and validator together if ClawHub changes its [catalog metadata schema](https://github.com/openclaw/clawhub/blob/main/packages/schema/src/catalogMetadata.ts).

The script is intentionally simple. If a check blocks a legitimate public example, update the policy and script together.

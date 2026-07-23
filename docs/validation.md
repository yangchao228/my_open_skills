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
- every release has a valid ordered status (`planned`, `verified`, or reasoned `blocked`), risk, next semver, one to three explicit non-`other` categories, tags, and a changelog
- release-plan categories, order, source path, risk, and target version match `docs/clawhub-releases.md`
- every ready skill has the canonical creator suffix and footer exactly once, a source homepage, and a package under ClawHub's size limit
- local ClawHub state is ignored, and both single-skill release scripts remain executable

For a safe ClawHub release preflight, run:

```bash
# Dry-run only. Requires a clean main branch whose HEAD matches origin/main.
./scripts/clawhub-release-one.sh <slug>

# Live publication requires both explicit flags and still publishes one skill only.
./scripts/clawhub-release-one.sh <slug> --publish --yes --watch
```

The watcher resumes independently with `./scripts/clawhub-watch-release.sh <slug>`. It records transient receipts under the ignored `.clawhub-release-state/` directory and reports only state changes while it waits for the public metadata, exact install, source hashes, security scans, and Skill Card to pass.

The script is intentionally simple. If a check blocks a legitimate public example, update the policy and script together.

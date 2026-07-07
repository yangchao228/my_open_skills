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

The script is intentionally simple. If a check blocks a legitimate public example, update the policy and script together.

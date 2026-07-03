# My Open Skills

Public AI Agent Skills collected from local workflows that have been cleaned, generalized, and made reusable.

This repository is not a single-skill package. It is a long-term open skills library organized by workflow area.

## Why This Exists

Good agent work needs reusable process, not one-off prompts. This repo collects workflows that repeatedly help with:

- content creation from topic to publish check
- structured work output such as interview preparation
- future engineering, publishing, and verification workflows

Each public skill should be understandable by a new user, safe to share, and testable with a small example.

## Skill Groups

### Content

The first public workflow is `Wenchang`, a content creation system that routes a topic or draft through research, evidence gathering, drafting, review, and publish checks.

Start here:

- [wenchang-orchestrator](skills/content/wenchang-orchestrator) - full workflow coordinator
- [wenchang-router](skills/content/wenchang-router) - lightweight stage router

Core content skills:

- [storm-research](skills/content/storm-research)
- [wenchang-research](skills/content/wenchang-research)
- [wenchang-wechat-writer](skills/content/wenchang-wechat-writer)
- [wenchang-review](skills/content/wenchang-review)
- [wenchang-publish-check](skills/content/wenchang-publish-check)

See [skills/content/README.md](skills/content/README.md).

### Work

Reusable structured work output.

- [resume-interview-generator](skills/work/resume-interview-generator) - generate structured interview questions, follow-up paths, scoring criteria, and risk checks from a resume and role.

See [skills/work/README.md](skills/work/README.md).

### Engineering

Engineering workflow skills will be added later. See [skills/engineering/README.md](skills/engineering/README.md).

### Publishing

Publishing and distribution helper skills will be added later. See [skills/publishing/README.md](skills/publishing/README.md).

## Install

Current public package names are maintained per skill. Existing install commands for `resume-interview-generator` remain:

```bash
npx @skills-hub-ai/cli install resume-interview-generator-2
```

```bash
clawhub install resume-interview-generator
```

For local development, clone this repo and link or copy the skill folders into the skill directory used by your agent runtime.

## Validate

```bash
./scripts/list-skills.sh
./scripts/validate-skills.sh
```

Validation checks skill metadata, paths, examples, JSON, and common private-content leaks.

The first Wenchang workflow smoke is documented in [docs/examples/wenchang-end-to-end-smoke.md](docs/examples/wenchang-end-to-end-smoke.md).

## Public Boundary

Public skills in this repo should not contain private files, local absolute paths, credentials, real account details, private content outputs, or private book/material systems.

Local workflows are used only as source experience. Public skills are rewritten and generalized before they are added here.

See [docs/publishing-policy.md](docs/publishing-policy.md).

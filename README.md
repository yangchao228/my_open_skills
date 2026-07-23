# My Open Skills

[中文版本](README.zh-CN.md)

Public AI Agent Skills collected from local workflows that have been cleaned, generalized, and made reusable.

This repository is not a single-skill package. It is a long-term open skills library organized by workflow area.

## Why This Exists

Good agent work needs reusable process, not one-off prompts. This repo collects workflows that repeatedly help with:

- content creation from topic to publish check
- structured work output such as interview preparation
- future engineering, publishing, and verification workflows

Each public skill should be understandable by a new user, safe to share, and testable with a small example.

## Handcrafted Skills Public Series

`我亲手打造的 Skills` is a Chinese Zhihu and Xiaohongshu series that demonstrates this library through reproducible cases. Each episode starts from one public input and records the actual output, design decisions, boundaries, and a reproduction path.

- [Season 1 plan](docs/series/handcrafted-skills/series-plan.md)
- [Case Pack template](docs/series/handcrafted-skills/case-pack-template.md)
- [Theme 01: Turn one long-form article into cross-platform content assets](docs/series/handcrafted-skills/themes/01-content-asset-pipeline/case-pack.md)
- [Episode 01: Xiaohongshu Topic Generator](docs/series/handcrafted-skills/season-01/01-xiaohongshu-topic-generator/case-pack.md)

## Skill Groups

### Content

The first public workflow is `Wenchang`, a content creation system that routes a topic or draft through research, evidence gathering, drafting, review, platform adaptation, long-form illustration, recoverable image-generation backends, publish-ready card rendering, and publish checks.

Start here:

- [wenchang-orchestrator](skills/content/wenchang-orchestrator) - full workflow coordinator
- [wenchang-router](skills/content/wenchang-router) - lightweight stage router

Core content skills:

- [zhihu-topic-hunter](skills/content/zhihu-topic-hunter)
- [xiaohongshu-topic-generator](skills/content/xiaohongshu-topic-generator)
- [long-to-cards](skills/content/long-to-cards)
- [redbook-cards-skill](skills/content/redbook-cards-skill)
- [cards-to-images](skills/content/cards-to-images)
- [resilient-imagegen](skills/content/resilient-imagegen)
- [chatgpt-image-handoff](skills/content/chatgpt-image-handoff)
- [wechat-to-cards](skills/content/wechat-to-cards)
- [article-to-illustrations](skills/content/article-to-illustrations)
- [storm-research](skills/content/storm-research)
- [wenchang-research](skills/content/wenchang-research)
- [wenchang-wechat-writer](skills/content/wenchang-wechat-writer)
- [wenchang-review](skills/content/wenchang-review)
- [wenchang-publish-check](skills/content/wenchang-publish-check) - create preflight platform packages and run the final release gate

See [skills/content/README.md](skills/content/README.md).

### Work

Reusable structured work output.

- [resume-interview-generator](skills/work/resume-interview-generator) - generate structured interview questions, follow-up paths, scoring criteria, and risk checks from a resume and role.
- [project-weekly-report](skills/work/project-weekly-report) - generate evidence-based project weekly reports from local repository history, tags, docs, and artifacts.
- [create-plan](skills/work/create-plan) - create concise implementation plans before coding, documentation, repository, or workflow changes.
- [doc-coauthoring](skills/work/doc-coauthoring) - guide substantial documents from context alignment through section drafting, reader testing, and final checks.

See [skills/work/README.md](skills/work/README.md).

### Engineering

Engineering workflow skills will be added later. See [skills/engineering/README.md](skills/engineering/README.md).

### Publishing

Publishing and distribution helpers make content assets ready for public URLs and platform delivery.

- [md-img-r2](skills/publishing/md-img-r2) - inspect local Markdown images, create a dry-run public-URL plan, and apply reviewed R2 or S3-compatible replacements behind an explicit confirmation gate.

See [skills/publishing/README.md](skills/publishing/README.md).

## Install

Use [Install and Trial](docs/install-and-trial.md) as the repository-level guide.

Package commands are maintained per skill. Current documented package commands exist for `resume-interview-generator`:

```bash
npx @skills-hub-ai/cli install resume-interview-generator-2
```

```bash
clawhub install resume-interview-generator
```

For local development, clone this repo and link or copy the skill folders into the skill directory used by your agent runtime.

For skills without a documented package command, start by reading that skill's `SKILL.md`, `examples/minimal-input.md`, and `examples/expected-output-notes.md`. The public series Case Packs provide an additional end-to-end reproduction path without claiming a universal one-command installer.

## Validate

```bash
./scripts/list-skills.sh
./scripts/validate-skills.sh
```

Validation checks skill metadata, paths, examples, JSON, README Chinese counterparts, and common private-content leaks.

The first Wenchang workflow smoke is documented in [docs/examples/wenchang-end-to-end-smoke.md](docs/examples/wenchang-end-to-end-smoke.md).

## Public Boundary

Public skills in this repo should not contain private files, local absolute paths, credentials, real account details, private content outputs, or private book/material systems.

Local workflows are used only as source experience. Public skills are rewritten and generalized before they are added here.

See [docs/publishing-policy.md](docs/publishing-policy.md).

## License

MIT. See [LICENSE](LICENSE).

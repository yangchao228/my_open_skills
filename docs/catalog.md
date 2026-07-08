# Skill Catalog

Status values: `ready`, `draft`, `incubating`, `private-source`, `deprecated`.

Invocation values: `model-invoked`, `user-invoked`, `router-only`.

## Content

| Skill | Status | Invocation | Purpose |
| --- | --- | --- | --- |
| [wenchang-orchestrator](../skills/content/wenchang-orchestrator) | ready | user-invoked | Full content workflow coordinator |
| [wenchang-router](../skills/content/wenchang-router) | ready | model-invoked | Route content requests to the next stage |
| [storm-research](../skills/content/storm-research) | ready | model-invoked | Pre-writing multi-perspective research |
| [wenchang-research](../skills/content/wenchang-research) | ready | model-invoked | Evidence gathering and confidence review |
| [wenchang-wechat-writer](../skills/content/wenchang-wechat-writer) | ready | model-invoked | Draft WeChat-style long-form articles |
| [wenchang-review](../skills/content/wenchang-review) | ready | model-invoked | Diagnose or edit existing drafts |
| [wenchang-publish-check](../skills/content/wenchang-publish-check) | ready | model-invoked | Final publish asset check |
| [zhihu-topic-hunter](../skills/content/zhihu-topic-hunter) | ready | user-invoked | Generate ranked Zhihu topic candidates from a theme |
| [xiaohongshu-topic-generator](../skills/content/xiaohongshu-topic-generator) | ready | user-invoked | Generate Xiaohongshu-ready topic candidates and card outlines |
| [long-to-cards](../skills/content/long-to-cards) | ready | user-invoked | Transform long-form content into card-based social packages |
| [wechat-to-cards](../skills/content/wechat-to-cards) | ready | user-invoked | Transform WeChat articles into card and distribution assets |

Future candidates: `redbook-cards`.

## Work

| Skill | Status | Invocation | Purpose |
| --- | --- | --- | --- |
| [resume-interview-generator](../skills/work/resume-interview-generator) | ready | model-invoked | Generate structured interview questions from resumes |
| [project-weekly-report](../skills/work/project-weekly-report) | ready | model-invoked | Generate evidence-based project weekly reports from local repositories |
| [create-plan](../skills/work/create-plan) | ready | user-invoked | Create concise implementation plans before changes are made |
| [doc-coauthoring](../skills/work/doc-coauthoring) | ready | user-invoked | Guide structured co-authoring of substantial documents |

Future candidates: none selected.

## Engineering

No public ready skills in the first phase.

Future candidates: `wechat-miniprogram-ui-acceptance`, `playwright`, `figma`, `figma-implement-design`, `mcp-builder`, `frontend-design`, `webapp-testing`.

## Publishing

No public ready skills in the first phase.

Current migration decision: see [Publishing Risk Review](publishing-risk-review.md).

| Candidate | Status | Invocation | Public-safe direction |
| --- | --- | --- | --- |
| `md-img-r2` | incubating | user-invoked | Dry-run-first Markdown image publishing helper after safety rewrite |
| `bilibili-video-publisher` | private-source | user-invoked | Metadata package and pre-publish checklist only |
| `superman-blog-publisher` | private-source | user-invoked | Generic Markdown blog importer after site-specific cleanup |

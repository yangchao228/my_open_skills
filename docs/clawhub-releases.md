# ClawHub Releases

[中文说明](#中文说明)

This ledger is the reader-facing source of truth for one-at-a-time ClawHub releases from this repository. The canonical creator profile lives in [`config/clawhub-profile.json`](../config/clawhub-profile.json), while [`config/clawhub-release-plan.json`](../config/clawhub-release-plan.json) stores the machine-readable release order, categories, topics, remote baselines, target versions, tags, and status.

## Release Policy

- Publish exactly one skill per release command; do not use `clawhub sync --all`.
- Run repository validation and `clawhub skill publish <path> --dry-run --json` before every live publish.
- Choose and record one to three valid ClawHub category slugs before every live publish, and pass them explicitly with `--categories`; do not rely on automatic inference or the `Other` fallback.
- Choose three to five specific discovery topics before every live publish, order the most important four first for the current page UI, and pass them explicitly with `--topics`. Keep `--tags` for version aliases such as `latest`.
- Publish only from a clean, committed source and pass the source repository, commit, ref, and path to the CLI.
- Treat a successful ClawHub upload response as `submitted`, then let the platform finish public indexing, security scans, and Skill Card generation asynchronously.
- Advance the serial release queue at the configured risk gate: low at `submitted`, medium at `public`, and high at `verified`. Every submitted version still progresses to full verification in the background.
- Run the background reconciler every 15 minutes. It may inspect, install, verify, update the plan and ledger, commit, and push; it never uploads a new skill.
- Treat ClawHub's MIT-0 release license as a distribution rule. Do not publish bundled third-party material when its attribution or license cannot be preserved safely.
- Keep the capability and trigger language first in `description`; append the canonical creator suffix exactly once.
- Promote skills through theme-level Case Packs even though registry releases are atomic.

## Catalog Metadata Decisions

| Slug | Categories | Topics | Application |
| --- | --- | --- | --- |
| `create-plan` | `agents`, `development`, `productivity` | `implementation-planning`, `rollout-planning`, `technical-design`, `task-breakdown`, `change-safety` | owner updates existing listing manually |
| `doc-coauthoring` | `knowledge`, `creative`, `productivity` | `document-coauthoring`, `prd`, `technical-spec`, `rfc`, `reader-review` | owner updated existing listing manually |
| `project-weekly-report` | `productivity`, `knowledge`, `development` | `git-history`, `weekly-report`, `project-status`, `evidence-based-reporting`, `engineering-updates` | owner adds topics to existing listing manually |
| `resume-interview-generator` | `productivity`, `knowledge`, `development` | `technical-interview`, `resume-evaluation`, `interview-questions`, `hiring-assessment`, `scoring-rubric` | owner adds topics to existing listing manually |
| `storm-research` | `research`, `knowledge`, `productivity` | `deep-research`, `source-synthesis`, `citation-workflow`, `contradiction-mapping`, `research-brief` | explicit CLI metadata |
| `wenchang-research` | `research`, `knowledge`, `productivity` | `content-research`, `source-validation`, `fact-checking`, `contrarian-evidence`, `evidence-pack` | explicit CLI metadata |
| `wenchang-review` | `creative`, `knowledge`, `productivity` | `content-review`, `editorial-diagnosis`, `draft-revision`, `publish-readiness`, `structural-editing` | explicit CLI metadata |
| `wenchang-wechat-writer` | `creative`, `communication`, `productivity` | `wechat-writing`, `long-form-writing`, `article-outline`, `content-hooks`, `editorial-workflow` | explicit CLI metadata |
| `xiaohongshu-topic-generator` | `creative`, `research`, `productivity` | `xiaohongshu`, `rednote`, `topic-ideation`, `content-hooks`, `audience-pain-points` | explicit CLI metadata |
| `zhihu-topic-hunter` | `research`, `knowledge`, `creative` | `zhihu`, `topic-research`, `debate-angles`, `question-selection`, `content-strategy` | explicit CLI metadata |
| `long-to-cards` | `creative`, `communication`, `productivity` | `content-repurposing`, `social-cards`, `carousel-content`, `card-scripts`, `platform-copy` | explicit CLI metadata |
| `wechat-to-cards` | `communication`, `creative`, `productivity` | `wechat-cards`, `moments-copy`, `community-sharing`, `content-repurposing`, `visual-snippets` | explicit CLI metadata |
| `article-to-illustrations` | `creative`, `productivity`, `knowledge` | `article-illustration`, `image-prompts`, `visual-storytelling`, `markdown-images`, `alt-text` | explicit CLI metadata |
| `cards-to-images` | `creative`, `automation`, `productivity` | `card-rendering`, `social-images`, `carousel-design`, `image-quality`, `visual-qa` | explicit CLI metadata |
| `resilient-imagegen` | `automation`, `creative`, `productivity` | `image-generation`, `retry-workflow`, `job-queue`, `fallback-routing`, `human-review` | explicit CLI metadata |
| `chatgpt-image-handoff` | `automation`, `creative`, `productivity` | `chatgpt-images`, `browser-handoff`, `prompt-pack`, `visual-qa`, `resumable-workflow` | explicit CLI metadata |
| `wenchang-router` | `agents`, `creative`, `productivity` | `content-routing`, `workflow-state`, `multi-platform-content`, `next-action`, `content-pipeline` | explicit CLI metadata |
| `wenchang-publish-check` | `productivity`, `communication`, `knowledge` | `publish-preflight`, `release-readiness`, `platform-packaging`, `asset-verification`, `human-approval` | explicit CLI metadata |
| `wenchang-orchestrator` | `agents`, `automation`, `productivity` | `content-orchestration`, `multi-platform-content`, `workflow-automation`, `asset-pipeline`, `knowledge-capture` | explicit CLI metadata |
| `md-img-r2` | `integrations`, `automation`, `productivity` | `cloudflare-r2`, `markdown-images`, `s3-upload`, `image-hosting`, `url-replacement` | explicit CLI update metadata |

## Release Ledger

| Order | Slug | Source path | Risk | Target | Status | Scan | Published at | ClawHub |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `create-plan` | `skills/work/create-plan` | low | `1.0.0` | verified (2026-07-23 12:29 CST) | pass; static, VirusTotal, and SkillSpector clean; SAFE | 2026-07-23 10:22:29 CST | [page](https://clawhub.ai/yangchao228/skills/create-plan) |
| 2 | `doc-coauthoring` | `skills/work/doc-coauthoring` | low | `1.0.0` | verified (2026-07-23 13:40 CST) | pass; static, VirusTotal, and SkillSpector clean; SAFE/LOW (3 notes) | 2026-07-23 12:58:41 CST | [page](https://clawhub.ai/yangchao228/skills/doc-coauthoring) |
| 3 | `project-weekly-report` | `skills/work/project-weekly-report` | medium | `1.0.0` | verified (2026-07-23 15:25 CST) | pass; static, VirusTotal, and SkillSpector clean; SAFE/LOW (1 note) | 2026-07-23 14:34:26 CST | [page](https://clawhub.ai/yangchao228/skills/project-weekly-report) |
| 4 | `resume-interview-generator` | `skills/work/resume-interview-generator` | medium | `1.0.1` | verified (2026-07-23 16:26 CST) | pass; static, VirusTotal, and SkillSpector clean; SAFE/LOW (1 note) | 2026-07-23 16:05:59 CST | [page](https://clawhub.ai/yangchao228/skills/resume-interview-generator) |
| 5 | `storm-research` | `skills/content/storm-research` | low | `1.0.0` | verified (2026-07-23 21:05 CST) | pass; static, VirusTotal, and SkillSpector clean; SAFE/LOW (1 note) | 2026-07-23 20:13:27 CST | [page](https://clawhub.ai/yangchao228/skills/storm-research) |
| 6 | `wenchang-research` | `skills/content/wenchang-research` | low | `1.0.0` | submitted (2026-07-23 21:42 CST) | pending | — | [page](https://clawhub.ai/yangchao228/skills/wenchang-research) |
| 7 | `wenchang-review` | `skills/content/wenchang-review` | low | `1.0.0` | submitted (2026-07-23 21:43 CST) | pending | — | [page](https://clawhub.ai/yangchao228/skills/wenchang-review) |
| 8 | `wenchang-wechat-writer` | `skills/content/wenchang-wechat-writer` | low | `1.0.0` | submitted (2026-07-23 21:44 CST) | pending | — | [page](https://clawhub.ai/yangchao228/skills/wenchang-wechat-writer) |
| 9 | `xiaohongshu-topic-generator` | `skills/content/xiaohongshu-topic-generator` | low | `1.0.0` | submitted (2026-07-23 21:46 CST) | pending | — | [page](https://clawhub.ai/yangchao228/skills/xiaohongshu-topic-generator) |
| 10 | `zhihu-topic-hunter` | `skills/content/zhihu-topic-hunter` | low | `1.0.0` | submitted (2026-07-23 21:46 CST) | pending | — | [page](https://clawhub.ai/yangchao228/skills/zhihu-topic-hunter) |
| 11 | `long-to-cards` | `skills/content/long-to-cards` | medium | `1.0.0` | submitted (2026-07-23 21:47 CST) | pending | — | [page](https://clawhub.ai/yangchao228/skills/long-to-cards) |
| 12 | `wechat-to-cards` | `skills/content/wechat-to-cards` | medium | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/wechat-to-cards) |
| 13 | `redbook-cards-skill` | `skills/content/redbook-cards-skill` | blocked | — | blocked: third-party MIT attribution conflicts with ClawHub MIT-0 packaging | not run | — | — |
| 14 | `article-to-illustrations` | `skills/content/article-to-illustrations` | medium | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/article-to-illustrations) |
| 15 | `cards-to-images` | `skills/content/cards-to-images` | medium | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/cards-to-images) |
| 16 | `resilient-imagegen` | `skills/content/resilient-imagegen` | medium | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/resilient-imagegen) |
| 17 | `chatgpt-image-handoff` | `skills/content/chatgpt-image-handoff` | high | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/chatgpt-image-handoff) |
| 18 | `wenchang-router` | `skills/content/wenchang-router` | medium | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/wenchang-router) |
| 19 | `wenchang-publish-check` | `skills/content/wenchang-publish-check` | medium | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/wenchang-publish-check) |
| 20 | `wenchang-orchestrator` | `skills/content/wenchang-orchestrator` | medium | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/wenchang-orchestrator) |
| 21 | `md-img-r2` | `skills/publishing/md-img-r2` | high | `1.0.4` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/md-img-r2) |

Status values: `prepared`, `submitted`, `public`, `verified`, `blocked`. `submitted` means ClawHub accepted the upload. `public` means the page, metadata, Topics, creator hooks, and exact-version install passed. `verified` additionally means registry hashes, security workers, and Skill Card passed. A skill-specific block does not authorize weakening validation or changing the skill's safety boundary.

## Optimized Single-Skill Runner

The automated path keeps live publication atomic and fail-closed:

```bash
# Validate metadata, remote baseline, clean pushed source, and ClawHub dry-run.
./scripts/clawhub-release-one.sh wenchang-research

# Publish, record and push submitted state, then return immediately.
./scripts/clawhub-release-one.sh wenchang-research --publish --yes

# Optional foreground waits.
./scripts/clawhub-release-one.sh wenchang-research --publish --yes --watch-public
./scripts/clawhub-release-one.sh wenchang-research --publish --yes --watch
```

The watcher can also resume independently:

```bash
./scripts/clawhub-watch-release.sh wenchang-research --until public
./scripts/clawhub-watch-release.sh wenchang-research --once --until verified
./scripts/clawhub-reconcile-releases.sh
```

Transient preflight, submission, public, inspect, page, install, scan, and Skill Card receipts are written under the ignored `.clawhub-release-state/` directory. The watcher verifies all planned Topics through the public API and the first four Topics rendered by the current page UI, and prints only state changes.

The runner accepts the next `planned` entry whose earlier releases have reached their configured risk gates, and it acquires an atomic live-publish lock. The scheduled GitHub Action runs at minutes 7, 22, 37, and 52, so platform work never holds the interactive terminal open. If a skill-specific gate cannot pass, record that plan entry as `blocked` with a `blocked_reason` and update its ledger row before advancing; publisher identity, creator-hook, or authentication failures stop the sequence.

## 中文说明

- 每个 skill 独立执行 dry-run 和发布；ClawHub 接受上传后立即记为 `submitted`，前台任务完成。
- 公开页面、临时安装、安全扫描和 Skill Card 由后台每 15 分钟对账，依次晋级为 `public` 和 `verified`。
- 发布队列按风险门槛推进：低风险到 `submitted`，中风险到 `public`，高风险到 `verified`；所有版本最终仍需达到 `verified`。
- ClawHub 描述统一追加公众号、X 和 GitHub 作者入口；能力和触发条件始终放在前面。
- ClawHub 发布采用 MIT-0。含第三方版权或无法确认再许可边界的 skill 保持 `blocked`，不强行发布。
- ClawHub 条目逐个发布，自媒体内容继续按主题 Case Pack 组织，避免把公开系列拆成零散功能介绍。
- 默认脚本只执行 dry-run；正式发布必须显式传入 `--publish --yes`。上传成功后脚本自动更新并推送 `submitted` 台账；定时任务只对账已有发布，不会上传新 skill。
- Categories 用于平台大类，Topics 用于细粒度发现，Tags 仅保留版本别名用途；发布前都从机器可读计划中显式传入。

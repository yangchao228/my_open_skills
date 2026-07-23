# ClawHub Releases

[中文说明](#中文说明)

This ledger is the reader-facing source of truth for one-at-a-time ClawHub releases from this repository. The canonical creator profile lives in [`config/clawhub-profile.json`](../config/clawhub-profile.json), while [`config/clawhub-release-plan.json`](../config/clawhub-release-plan.json) stores the machine-readable release order, categories, remote baselines, target versions, tags, and status.

## Release Policy

- Publish exactly one skill per release command; do not use `clawhub sync --all`.
- Run repository validation and `clawhub skill publish <path> --dry-run --json` before every live publish.
- Choose and record one to three valid ClawHub category slugs before every live publish, and pass them explicitly with `--categories`; do not rely on automatic inference or the `Other` fallback.
- Publish only from a clean, committed source and pass the source repository, commit, ref, and path to the CLI.
- Verify every live version with `clawhub inspect`, a temporary install, and the registry security scan before advancing.
- Treat ClawHub's MIT-0 release license as a distribution rule. Do not publish bundled third-party material when its attribution or license cannot be preserved safely.
- Keep the capability and trigger language first in `description`; append the canonical creator suffix exactly once.
- Promote skills through theme-level Case Packs even though registry releases are atomic.

## Category Decisions

| Slug | Categories | Application |
| --- | --- | --- |
| `create-plan` | `agents`, `development`, `productivity` | planned manual update by owner |
| `doc-coauthoring` | `knowledge`, `creative`, `productivity` | planned manual update by owner |
| `project-weekly-report` | `productivity`, `knowledge`, `development` | explicit CLI publish metadata |
| `resume-interview-generator` | `productivity`, `knowledge`, `development` | explicit CLI update metadata |
| `storm-research` | `research`, `knowledge`, `productivity` | planned explicit CLI metadata |
| `wenchang-research` | `research`, `knowledge`, `productivity` | planned explicit CLI metadata |
| `wenchang-review` | `creative`, `knowledge`, `productivity` | planned explicit CLI metadata |
| `wenchang-wechat-writer` | `creative`, `communication`, `productivity` | planned explicit CLI metadata |
| `xiaohongshu-topic-generator` | `creative`, `research`, `productivity` | planned explicit CLI metadata |
| `zhihu-topic-hunter` | `research`, `knowledge`, `creative` | planned explicit CLI metadata |
| `long-to-cards` | `creative`, `communication`, `productivity` | planned explicit CLI metadata |
| `wechat-to-cards` | `communication`, `creative`, `productivity` | planned explicit CLI metadata |
| `article-to-illustrations` | `creative`, `productivity`, `knowledge` | planned explicit CLI metadata |
| `cards-to-images` | `creative`, `automation`, `productivity` | planned explicit CLI metadata |
| `resilient-imagegen` | `automation`, `creative`, `productivity` | planned explicit CLI metadata |
| `chatgpt-image-handoff` | `automation`, `creative`, `productivity` | planned explicit CLI metadata |
| `wenchang-router` | `agents`, `creative`, `productivity` | planned explicit CLI metadata |
| `wenchang-publish-check` | `productivity`, `communication`, `knowledge` | planned explicit CLI metadata |
| `wenchang-orchestrator` | `agents`, `automation`, `productivity` | planned explicit CLI metadata |
| `md-img-r2` | `integrations`, `automation`, `productivity` | planned explicit CLI update metadata |

## Release Ledger

| Order | Slug | Source path | Risk | Target | Status | Scan | Published at | ClawHub |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `create-plan` | `skills/work/create-plan` | low | `1.0.0` | verified (2026-07-23 12:29 CST) | pass; static, VirusTotal, and SkillSpector clean; SAFE | 2026-07-23 10:22:29 CST | [page](https://clawhub.ai/yangchao228/skills/create-plan) |
| 2 | `doc-coauthoring` | `skills/work/doc-coauthoring` | low | `1.0.0` | verified (2026-07-23 13:40 CST) | pass; static, VirusTotal, and SkillSpector clean; SAFE/LOW (3 notes) | 2026-07-23 12:58:41 CST | [page](https://clawhub.ai/yangchao228/skills/doc-coauthoring) |
| 3 | `project-weekly-report` | `skills/work/project-weekly-report` | medium | `1.0.0` | verified (2026-07-23 15:25 CST) | pass; static, VirusTotal, and SkillSpector clean; SAFE/LOW (1 note) | 2026-07-23 14:34:26 CST | [page](https://clawhub.ai/yangchao228/skills/project-weekly-report) |
| 4 | `resume-interview-generator` | `skills/work/resume-interview-generator` | medium | `1.0.1` | verified (2026-07-23 16:26 CST) | pass; static, VirusTotal, and SkillSpector clean; SAFE/LOW (1 note) | 2026-07-23 16:05:59 CST | [page](https://clawhub.ai/yangchao228/skills/resume-interview-generator) |
| 5 | `storm-research` | `skills/content/storm-research` | low | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/storm-research) |
| 6 | `wenchang-research` | `skills/content/wenchang-research` | low | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/wenchang-research) |
| 7 | `wenchang-review` | `skills/content/wenchang-review` | low | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/wenchang-review) |
| 8 | `wenchang-wechat-writer` | `skills/content/wenchang-wechat-writer` | low | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/wenchang-wechat-writer) |
| 9 | `xiaohongshu-topic-generator` | `skills/content/xiaohongshu-topic-generator` | low | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/xiaohongshu-topic-generator) |
| 10 | `zhihu-topic-hunter` | `skills/content/zhihu-topic-hunter` | low | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/zhihu-topic-hunter) |
| 11 | `long-to-cards` | `skills/content/long-to-cards` | medium | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/long-to-cards) |
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

Status values: `prepared`, `pending-publication`, `published`, `verified`, `blocked`. `pending-publication` means ClawHub accepted the upload but still hides it from inspect/install while platform security workers finish. A skill-specific block does not authorize weakening validation or changing the skill's safety boundary.

## Optimized Single-Skill Runner

The automated path keeps live publication atomic and fail-closed:

```bash
# Validate metadata, remote baseline, clean pushed source, and ClawHub dry-run.
./scripts/clawhub-release-one.sh storm-research

# Explicitly publish one version and keep watching until the full gate passes.
./scripts/clawhub-release-one.sh storm-research --publish --yes --watch

# Optional: after verification, update the plan and ledger, commit, and push.
./scripts/clawhub-release-one.sh storm-research --publish --yes --watch --finalize --push
```

The watcher can also resume independently:

```bash
./scripts/clawhub-watch-release.sh storm-research
./scripts/clawhub-watch-release.sh storm-research --once
```

Transient inspect, page, install, scan, and Skill Card receipts are written under the ignored `.clawhub-release-state/` directory. The watcher prints only state changes. Preparing the next skill is allowed while it waits, but another live publish still waits for the current skill's final `decision: pass`.

The runner accepts only the first `planned` entry by release order and acquires an atomic live-publish lock. If a skill-specific gate cannot pass, record that plan entry as `blocked` with a `blocked_reason` and update its ledger row before advancing; publisher identity, creator-hook, or authentication failures stop the sequence.

## 中文说明

- 每个 skill 独立执行 dry-run、发布、inspect、临时安装和安全扫描，完成后再进入下一项。
- ClawHub 描述统一追加公众号、X 和 GitHub 作者入口；能力和触发条件始终放在前面。
- ClawHub 发布采用 MIT-0。含第三方版权或无法确认再许可边界的 skill 保持 `blocked`，不强行发布。
- ClawHub 条目逐个发布，自媒体内容继续按主题 Case Pack 组织，避免把公开系列拆成零散功能介绍。
- 默认脚本只执行 dry-run；正式发布必须显式传入 `--publish --yes`。自动改台账并推送还需要 `--finalize --push`，避免误触外部写入。

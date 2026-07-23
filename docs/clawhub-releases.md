# ClawHub Releases

[中文说明](#中文说明)

This ledger is the source of truth for one-at-a-time ClawHub releases from this repository. The canonical creator profile lives in [`config/clawhub-profile.json`](../config/clawhub-profile.json).

## Release Policy

- Publish exactly one skill per release command; do not use `clawhub sync --all`.
- Run repository validation and `clawhub skill publish <path> --dry-run --json` before every live publish.
- Publish only from a clean, committed source and pass the source repository, commit, ref, and path to the CLI.
- Verify every live version with `clawhub inspect`, a temporary install, and the registry security scan before advancing.
- Treat ClawHub's MIT-0 release license as a distribution rule. Do not publish bundled third-party material when its attribution or license cannot be preserved safely.
- Keep the capability and trigger language first in `description`; append the canonical creator suffix exactly once.
- Promote skills through theme-level Case Packs even though registry releases are atomic.

## Release Ledger

| Order | Slug | Source path | Risk | Target | Status | Scan | Published at | ClawHub |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `create-plan` | `skills/work/create-plan` | low | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/create-plan) |
| 2 | `doc-coauthoring` | `skills/work/doc-coauthoring` | low | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/doc-coauthoring) |
| 3 | `project-weekly-report` | `skills/work/project-weekly-report` | medium | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/project-weekly-report) |
| 4 | `resume-interview-generator` | `skills/work/resume-interview-generator` | medium | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/resume-interview-generator) |
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
| 21 | `md-img-r2` | `skills/publishing/md-img-r2` | high | `1.0.0` | prepared | pending | — | [page](https://clawhub.ai/yangchao228/skills/md-img-r2) |

Status values: `prepared`, `published`, `verified`, `blocked`. A skill-specific block does not authorize weakening validation or changing the skill's safety boundary.

## 中文说明

- 每个 skill 独立执行 dry-run、发布、inspect、临时安装和安全扫描，完成后再进入下一项。
- ClawHub 描述统一追加公众号、X 和 GitHub 作者入口；能力和触发条件始终放在前面。
- ClawHub 发布采用 MIT-0。含第三方版权或无法确认再许可边界的 skill 保持 `blocked`，不强行发布。
- ClawHub 条目逐个发布，自媒体内容继续按主题 Case Pack 组织，避免把公开系列拆成零散功能介绍。

# 主题 01：图片 Manifest V2

## 正式长文插图

| ID | 平台 | Markdown | 本地路径 | 正文锚点 | 尺寸 | R2 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| IMG-WECHAT-01 | 公众号 | `wechat-draft.md` | `assets/longform-v2/01-content-flow-wechat-16x9.png` | `## 我把分发流程拆成了 7 个 Skills` | 1600 × 900 | `verified` |
| IMG-WECHAT-02 | 公众号 | `wechat-draft.md` | `assets/longform-v2/03-r2-flow-wechat-16x9.png` | `## 图片资产，才是多平台分发里容易丢失的一层` | 1600 × 900 | `verified` |
| IMG-ZHIHU-01 | 知乎 | `zhihu-draft.md` | `assets/longform-v2/02-content-flow-zhihu-3x4.png` | `## 这次实际用了 7 个 Skills` | 1080 × 1440 | `planned` |
| IMG-ZHIHU-02 | 知乎 | `zhihu-draft.md` | `assets/longform-v2/04-r2-flow-zhihu-3x4.png` | `## 第三段：图片环节也要留下状态` | 1080 × 1440 | `planned` |

四张图片均已生成并完成视觉检查。公众号两张图片已替换为经过公网验收的 R2 URL；知乎两张图片仍以相对路径保留在正式 Markdown 中。

## ALT 与来源

| ID | ALT | 来源与事实边界 |
| --- | --- | --- |
| IMG-WECHAT-01 | 审核后的母稿经过发布预检、长文插图、小红书卡片、R2 图片计划和最终人工确认 | V2 Skill 合同；原 7 Skill 案例继续保留为历史事实 |
| IMG-WECHAT-02 | 本地 Markdown 图片经过 dry-run 和人工审核后进入 R2，为长文提供稳定公网引用 | `md-img-r2` 公开合同；平台原生图文使用本地 PNG 人工上传 |
| IMG-ZHIHU-01 | 审核后的母稿经过发布预检，分别形成公众号知乎长文插图和小红书卡片，再进入图片计划与发布门禁 | V2 Skill 合同；不改写原案例运行事实 |
| IMG-ZHIHU-02 | 本地图片经过 dry-run 和人工审核后进入 R2，为公众号、知乎长文与博客提供稳定公网引用 | `md-img-r2` 公开合同；计划不等于上传 |

## R2 交付状态

公众号报告：[wechat-draft.md.image-publish-plan.json](wechat-draft.md.image-publish-plan.json)

| ID | 对象键 | 公网 URL |
| --- | --- | --- |
| IMG-WECHAT-01 | `my-open-skills/theme-01/longform-v2/bc8d4f1ba0353efe-01-content-flow-wechat-16x9.png` | `https://images.reai.group/my-open-skills/theme-01/longform-v2/bc8d4f1ba0353efe-01-content-flow-wechat-16x9.png` |
| IMG-WECHAT-02 | `my-open-skills/theme-01/longform-v2/c04e5e3564c94346-03-r2-flow-wechat-16x9.png` | `https://images.reai.group/my-open-skills/theme-01/longform-v2/c04e5e3564c94346-03-r2-flow-wechat-16x9.png` |

2026-07-20 已按计划上传公众号两张图片并改写 `wechat-draft.md`。两条公网 URL 均返回 `HTTP 200` 和 `Content-Type: image/png`；本地备份与替换报告仅作为忽略的运行证据保留。

知乎报告：[zhihu-draft.md.image-publish-plan.json](zhihu-draft.md.image-publish-plan.json)

| ID | 对象键 | 计划 URL |
| --- | --- | --- |
| IMG-ZHIHU-01 | `my-open-skills/theme-01/longform-v2/e010cfa319a0c622-02-content-flow-zhihu-3x4.png` | `https://images.reai.group/my-open-skills/theme-01/longform-v2/e010cfa319a0c622-02-content-flow-zhihu-3x4.png` |
| IMG-ZHIHU-02 | `my-open-skills/theme-01/longform-v2/6606cb3e55ee861c-04-r2-flow-zhihu-3x4.png` | `https://images.reai.group/my-open-skills/theme-01/longform-v2/6606cb3e55ee861c-04-r2-flow-zhihu-3x4.png` |

公众号两张图片状态为 `verified`。知乎报告仍为 `mode=plan`，合计 `planned=2`、`issues=0`；知乎计划 URL 尚未上传或进行公网验收，不能作为已存在链接使用。

## 回归样例

早期链路样例仍保留在 [workflow-v2-illustrated-sample.md](workflow-v2-illustrated-sample.md)，对应报告为 [workflow-v2-illustrated-sample.md.image-publish-plan.json](workflow-v2-illustrated-sample.md.image-publish-plan.json)。它只证明单图插入与 dry-run，不进入正式平台稿。

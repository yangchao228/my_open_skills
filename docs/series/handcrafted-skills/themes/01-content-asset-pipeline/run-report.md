# 主题 01：真实案例运行记录

运行日期：2026-07-14

## 目标

用一篇真实公开长文和 `my_open_skills` 的内容技能包，生成公众号、知乎长文、知乎想法与小红书发布资产，并记录长文插图、卡片成图和分平台 R2 交付状态。

## 输入

- 真实源材料：《Loop Engineering 从入门到进阶手册》公开介绍稿
- 公众号母稿：[多平台内容分发与开源 Skills 技能包](wechat-draft.md)
- 目标读者：已经有长文、报告、复盘或课程材料，希望减少跨平台重复劳动的人
- 公开边界：不使用私有配置、账号状态、平台效果数据或未经确认的流量承诺

## 实际执行

| 步骤 | 使用能力 | 实际输出 | 状态 |
| --- | --- | --- | --- |
| 1. 源文诊断 | `wenchang-review` | 核心判断、保留材料、降级材料、平台适配边界 | 完成 |
| 2. 知乎适配 | 知乎平台合同 | [知乎正式稿](zhihu-draft.md) | 完成 |
| 3. 小红书拆卡 | `long-to-cards`，`delivery_mode=publish_ready` | [8 页卡片文案](xiaohongshu-cards.md) 与图片生产交接 | 完成 |
| 4. 卡片成图与逐图检查 | `cards-to-images`，使用确定性画布 / Open Weave | 8 张 1080×1440 PNG、总览图与 [cards manifest](xiaohongshu-upload-manifest.md) | `generated`、QA `passed`、人工确认 `pending` |
| 5. 图片发布计划 | `md-img-r2` | 8 张小红书图片的历史 R2 dry-run | 完成验证，本次发布改为本地上传 |
| 6. 发布检查 | `wenchang-publish-check` | 标题、摘要、标签、配图、CTA 与人工确认项 | 完成 |

## V2 增量回归

原运行记录保留了主题 01 的历史产物。V2 在此基础上增加长文插图层与双阶段发布门禁：

| 步骤 | 使用能力 | 实际输出 | 状态 |
| --- | --- | --- | --- |
| 7. 发布预检 | `wenchang-publish-check` preflight | 四种发布形态的标题、摘要、正文描述、标签时效与插图判断 | 完成 |
| 8. 长文插图 | `article-to-illustrations`、`canvas-design` | [公众号/知乎插图计划](illustration-plan-v2.md) 与 [4 张成图](assets/longform-v2/contact-sheet.png) | 完成并插入正式稿 |
| 9. 插入与 manifest | `article-to-illustrations` | [公众号稿](wechat-draft.md)、[知乎稿](zhihu-draft.md) 与 [manifest](image-manifest-v2.md) | 4 张相对路径已插入 |
| 10. 图片交付 | `md-img-r2` | [公众号报告](wechat-draft.md.image-publish-plan.json)、[知乎报告](zhihu-draft.md.image-publish-plan.json) | 公众号 `verified=2`；知乎 `planned=2`、`issues=0` |
| 11. 最终门禁 | `wenchang-publish-check` final | [V2 回归](workflow-v2-regression.md) 与 [content_state](content-state-v2.yaml) | `needs_review` |
| 12. 公众号贴图 | `wechat-to-cards -> long-to-cards -> cards-to-images` | [3 张 1600×900 贴图](assets/wechat-inline/contact-sheet.png) 与 [Manifest](wechat-inline-manifest.md) | `generated=3`、QA `passed=3`、人工确认 `pending` |
| 13. 知乎想法 | `long-to-cards -> cards-to-images` | [知乎想法正文和 5 张成图](zhihu-idea-cards.md) 与 [Manifest](zhihu-idea-manifest.md) | `generated=5`、QA `passed=5`、人工确认 `pending` |
| 14. 宣传卡重构 | `long-to-cards -> cards-to-images` | 按四种真实发布资产重写并重绘 [小红书 8 张宣传卡](assets/contact-sheet.png) | `generated=8`、QA `passed=8`、本地 PNG 交付 |

## Publish-ready 卡片链补充验证

- 统一链路：`long-to-cards -> cards-to-images -> visual QA -> human confirmation`
- 平台 profile：`xiaohongshu`、`wechat-inline`、`zhihu-idea`
- 卡片分支成图：16 张，包括小红书 8 张、公众号贴图 3 张、知乎想法 5 张
- Manifest：[小红书](xiaohongshu-upload-manifest.md)、[公众号贴图](wechat-inline-manifest.md)、[知乎想法](zhihu-idea-manifest.md)
- 逐图 QA：16 张全部 `passed`
- QA 修复：第一轮发现母稿连线穿过输出卡、公众号 R2 分支超出安全区，以及人工门禁的中英混合标签缺字；修复布局与字体选择后重新生成，并逐张复查通过
- 人工确认：`pending`
- R2：三组平台卡片包均使用本地交付，`r2_state=not_planned`；R2 只处理公众号和知乎长文的 4 张插图
- 可直接交付方式：用户确认后分别使用本地 PNG 进入对应平台编辑器

## 小红书视觉验收

- 图片数量：8 张
- 单张尺寸：1080 × 1440
- 视觉哲学：[Open Weave](visual-philosophy.md)
- 总览：[contact-sheet.png](assets/contact-sheet.png)
- 首屏信息：一篇母稿，变成 4 种发布资产
- 重点证据页：第 2 页展示 1 篇母稿、4 种发布形态、20 张本地成图和 4 份 Manifest
- 流程证据：第 4、5、6 页分别展示两条生产链、卡片成图链和 R2 条件分支
- 复现入口：第 8 页展示仓库名与完整执行提示词
- 人工检查：标题换行、中文与 Skill 名、连线关系、安全区、R2 边界、仓库名和页面顺序已逐图检查

## 小红书历史 R2 dry-run 结果

执行对象：[小红书成图上传清单](xiaohongshu-upload-manifest.md)

- 计划图片：8 张
- 跳过远程图片：0 张
- 问题：0
- 对象前缀：`my-open-skills/theme-01`
- 计划公网域名：`https://images.reai.group`
- 报告：仅保留在本地工作区，不进入公开发布包
- 计划刷新：8 张宣传卡重构后重新执行 plan-only，新的内容哈希对象键已写入报告
- 外部写入：未执行
- Markdown 改写：未执行
- 最终发布决策：保留报告作为验证记录，小红书改用本地 PNG 人工上传

## 发布状态

### 公众号

- 长文正文与 2 张插图：完成
- 3 张 `wechat-inline` 贴图：生成并完成逐图 QA
- 当前状态：等待用户确认贴图是否插入正式稿，以及最终编辑器排版

### 知乎长文

- 正文：完成
- 标题、摘要、标签与分享文案：完成
- 图片：可使用小红书第 1、3、6、8 页，也可只发布长文
- 当前状态：可以进入知乎编辑器排版

V2 补充：两张 1080×1440 正式插图已经插入，发布状态因 R2 和编辑器外部门禁保持为 `needs_review`。

### 知乎想法

- 正文描述、普通话题标签和 CTA：完成
- 5 张 1080×1440 成图：生成并完成逐图 QA
- 当前状态：等待用户确认后进入知乎想法编辑器；热门标签未实时核验

### 小红书

- 8 张成图：完成
- 发布正文与普通主题标签：完成
- 实时热门标签：`unverified`，发布当天需要时再核验
- 顺序：按 `01` 至 `08` 上传
- 当前状态：8 张本地 PNG 已具备并完成视觉检查；用户确认后按顺序人工上传，不进入本次 R2 apply

## 停止点

本轮停在两个外部动作之前：

1. 知乎长文 2 张插图的 R2 实际上传与 Markdown 引用替换。
2. 公众号、知乎长文、知乎想法和小红书账号内的最终发布。

这些剩余外部动作需要用户明确确认。当前 20 张正式本地成图已经完成，公众号两张长文插图已上传 R2、替换引用并通过公网验收；剩余阻塞项是三组卡片图片的人工确认、知乎长文 2 张插图的 R2 apply、发布当天的可选热门标签核验，以及平台编辑器内的排版与链接检查。详细证据见 [多平台发布工作流 V2 回归](workflow-v2-regression.md)。

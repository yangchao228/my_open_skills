# 公众号贴图包：一篇母稿怎样形成四种发布资产

## Source Diagnosis

- 核心判断：多平台分发需要分别管理内容适配、图片生产、图片引用与最终发布门禁。
- 读者问题：长文写完以后，平台稿、贴图和图片地址仍然需要重复整理。
- 最强材料：四种发布形态、共享卡片链、R2 条件分支和人工确认边界。
- 卡片类型：公众号文内总结卡；每张图离开正文后仍能独立理解。
- 已核事实：Theme 01 已完成公众号长文、知乎长文、小红书 8 张成图和四张长文插图。
- 本轮新增：3 张公众号贴图；生成后逐图检查，保留人工确认。

## Shared Card Handoff

- `delivery_mode`: `publish_ready`
- `platform_profile`: `wechat-inline`
- `asset_url_policy`: `local`
- 卡片数量：3
- 目标尺寸：1600 × 900，16:9
- 视觉体系：[Open Weave](visual-philosophy.md)
- 建议插入位置：公众号正文“这次最终公开了哪些资产”之后、“你可以怎样复现”之前
- Canonical card package：本文件

## Cards

### WECHAT-INLINE-01

- 标题：一篇母稿，形成四种发布资产
- 正文：公众号长文、知乎长文、知乎想法和小红书图文共享同一份事实基线，再分别进入适合自己的正文或卡片分支。
- 微文案：ONE SOURCE / FOUR RELEASE FORMS
- 视觉方向：左侧母稿文件卡连接右侧四类平台资产；用蓝色表示长文，用橙色表示卡片。
- 来源锚点：`case-pack.md` 的跨平台派生合同与当前交付状态。
- ALT：同一篇审核母稿分别形成公众号长文、知乎长文、知乎想法和小红书图文四种发布资产。
- 文件：`assets/wechat-inline/01-four-release-forms.png`

### WECHAT-INLINE-02

- 标题：卡片文案，要继续走到真实图片
- 正文：`long-to-cards` 负责卡片叙事，`cards-to-images` 负责生成成图、逐张 QA 和 Cards Manifest。`publish_ready` 不在视觉建议阶段停下。
- 微文案：COPY → IMAGE → QA → MANIFEST
- 视觉方向：四段流水线；把“真实 PNG”与“Manifest”作为两个清晰产物节点。
- 来源锚点：`long-to-cards`、`cards-to-images` 和 `wenchang-publish-check` 当前合同。
- ALT：卡片文案依次经过真实图片生成、逐张视觉检查和 Manifest 记录，最后进入人工确认。
- 文件：`assets/wechat-inline/02-copy-to-checked-images.png`

### WECHAT-INLINE-03

- 标题：图片是否上 R2，取决于交付方式
- 正文：直接上传平台时保留本地 PNG；需要公网引用或长期归档时，先生成 `md-img-r2` dry-run 计划，人工确认后再上传和改写。
- 微文案：LOCAL BY DEFAULT / PUBLIC WHEN NEEDED
- 视觉方向：从已检查图片分成两条路径：本地直传与 R2 公网引用；人工确认位于外部写入前。
- 来源锚点：`cards-to-images` 的 `asset_url_policy` 与 `md-img-r2` 安全边界。
- ALT：经过检查的本地图片可以直接上传平台，需要公网引用时再经过 dry-run、人工确认和 R2 上传。
- 文件：`assets/wechat-inline/03-local-or-public.png`

## Distribution Assets

- 朋友圈文案：我用一篇真实长文跑通了公众号、知乎、知乎想法和小红书四种发布形态。内容适配、卡片成图、图片引用和发布门禁都被拆成可检查的 Skills，完整 Case Pack 已放进公开仓库。
- 社群文案：如果你手上已有长文，可以用这套开源 Skills 依次完成平台适配、长文插图、卡片成图、逐图 QA 和发布检查。图片默认保留本地文件，需要公网引用时再进入 R2 计划，外部上传继续由人确认。
- 卡片 CTA：用一篇自己的公开长文，复现一次这条链路。
- 标题、摘要、正文与主 CTA：继续使用 `publish-check.md` 已批准口径。
- 热门标签：未实时核验，不在贴图中展示。

## Image Production Handoff

- Next skill：`cards-to-images`
- Ordered card ids：`WECHAT-INLINE-01`、`WECHAT-INLINE-02`、`WECHAT-INLINE-03`
- Stable filenames：`01-four-release-forms.png`、`02-copy-to-checked-images.png`、`03-local-or-public.png`
- 输出目录：`assets/wechat-inline/`
- Manifest：`wechat-inline-manifest.md`
- 人工决策：确认三张贴图后，再决定是否插入正式公众号稿及是否准备公网 URL。
- 停止条件：停在人工确认之前；不执行 R2 上传或公众号发布。

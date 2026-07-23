# 知乎想法图文包：一篇母稿怎样变成四种发布资产

## Source Diagnosis

- 核心判断：多平台分发的关键在于共享事实基线，并让长文、卡片、图片与发布状态分别留下可检查产物。
- 读者问题：同一篇文章跨平台时，经常只有文案副本，没有稳定的图片生产与验收链路。
- 最强材料：真实资产矩阵、两条内容生产分支、R2 条件路径和人工发布门禁。
- 放弃材料：原手册的领取方式、作者转化话术、版本数字和未验证的传播效果。
- 事实状态：源文与公开链接已确认；当前没有平台效果数据，不承诺流量或效率数字。

## Card Strategy

- `delivery_mode`: `publish_ready`
- `platform_profile`: `zhihu-idea`
- `asset_url_policy`: `local`
- 目标读者：希望把长文沉淀成跨平台内容资产的创作者、开发者和独立产品人
- 卡片数量：5
- 叙事结构：结果 → 分支 → 成图链 → 图片资产 → 人工门禁
- 目标尺寸：1080 × 1440，3:4
- 视觉体系：[Open Weave](visual-philosophy.md)

## Cards

### ZHIHU-IDEA-01

- 标题：一篇母稿，怎样真正变成四种发布资产？
- 正文：这次我用一篇公开长文跑通公众号长文、知乎长文、知乎想法和小红书图文，并把中间产物留在公开 Case Pack。
- 微文案：ONE SOURCE / FOUR RELEASE FORMS
- 视觉方向：母稿位于中心，四类真实发布资产分布在四周；突出“真实文件”而非 Skill 数量。
- 来源锚点：`case-pack.md` 当前交付状态。
- ALT：一篇审核母稿连接公众号长文、知乎长文、知乎想法和小红书图文四种发布资产。
- 文件：`assets/zhihu-idea/01-one-source-four-assets.png`

### ZHIHU-IDEA-02

- 标题：先分清长文和卡片两条生产链
- 正文：公众号、知乎长文先判断是否需要插图；小红书、公众号贴图和知乎想法进入共享卡片链。事实基线一致，交付结构按平台重做。
- 微文案：LONGFORM / CARD BRANCH
- 视觉方向：一条母稿路径分成蓝色长文分支与橙色卡片分支，每条分支显示各自的最终文件。
- 来源锚点：`wenchang-orchestrator` 平台分支合同。
- ALT：审核母稿分别进入长文插图分支和卡片成图分支，再形成不同平台资产。
- 文件：`assets/zhihu-idea/02-two-production-branches.png`

### ZHIHU-IDEA-03

- 标题：卡片稿完成，还不能算发布资产
- 正文：`long-to-cards` 之后继续运行 `cards-to-images`，直到真实 PNG、逐图 QA 和 Cards Manifest 都存在，才进入人工确认。
- 微文案：COPY → PNG → QA → MANIFEST
- 视觉方向：把卡片文案、PNG 文件、QA 状态和 Manifest 依次排成可检查链路。
- 来源锚点：`long-to-cards` 与 `cards-to-images` 当前合同。
- ALT：卡片文案依次生成真实 PNG、完成逐图 QA 并写入 Cards Manifest。
- 文件：`assets/zhihu-idea/03-copy-is-not-delivery.png`

### ZHIHU-IDEA-04

- 标题：R2 是按需进入的图片资产层
- 正文：平台支持直接上传时使用本地图片；需要公开引用、博客复用或长期归档时，再用 `md-img-r2` 生成计划并等待人工确认。
- 微文案：PLAN ≠ UPLOAD
- 视觉方向：本地图片分成“平台直传”和“公网引用”两条路径；外部写入前放置醒目的人工门禁。
- 来源锚点：`md-img-r2` 的 dry-run 与显式确认边界。
- ALT：本地图片可以直接上传平台，需要公网引用时再经过 R2 计划与人工确认。
- 文件：`assets/zhihu-idea/04-r2-when-needed.png`

### ZHIHU-IDEA-05

- 标题：Skills 负责组织，人保留最终判断
- 正文：事实、正文、图片、Manifest 和发布字段都可以自动准备；角度、图示、外部上传与最终发布继续由人确认。
- 微文案：READY FOR REVIEW
- 视觉方向：左侧列出已完成产物，右侧橙色人工门禁；底部给出仓库与复现入口。
- 来源锚点：`publish-check.md` 与 `content-state-v2.yaml`。
- ALT：已完成的内容与图片资产进入人工确认，外部上传和平台发布保持待确认。
- 文件：`assets/zhihu-idea/05-human-final-gate.png`

## Publishing Assets

- 标题：一篇母稿，怎样真正变成四种发布资产？
- 首句：我最近用一篇已经完成事实核验的公开长文，把自己的内容 Skills 技能包完整跑了一遍。
- 正文：

  这次没有停在“改写出三份文案”。公众号和知乎分别保留长文正文与插图，小红书、公众号贴图和知乎想法走共享卡片链，继续生成真实图片、逐张 QA 和 Manifest。

  图片也保留两种交付方式：可以直接上传平台的就使用本地 PNG；需要公网引用或长期归档时，再进入 `md-img-r2` dry-run 和人工确认。

  最终留下的是一套可复查的 Case Pack：正文、卡片、图片、Manifest、发布字段和明确的人机边界。外部上传和平台发布仍然停在人的决定前。

  仓库：`yangchao228/my_open_skills`

- CTA：如果你手上已经有一篇长文，最想先复用这条链路里的哪一步？
- `core_tags`：`AI Agent`、`AI工作流`、`内容创作`
- `scene_tags`：`多平台内容分发`、`知识管理`、`数字资产`
- `series_tags`：`我亲手打造的Skills`、`开源项目`
- `verified_hot_tags`：
  - 状态：`unverified`
  - 检查时间：空
  - 来源：空
  - 值：空
- 来源说明：本图文只陈述仓库内已记录的真实输入、输出与状态，不包含平台效果数据。

## Image Production Handoff

- Next skill：`cards-to-images`
- Ordered card ids：`ZHIHU-IDEA-01` 至 `ZHIHU-IDEA-05`
- Stable filenames：`01-one-source-four-assets.png` 至 `05-human-final-gate.png`
- 输出目录：`assets/zhihu-idea/`
- Manifest：`zhihu-idea-manifest.md`
- 人工决策：确认五张图片、知乎想法正文和标签后，再进入平台编辑器。
- 停止条件：停在人工确认之前；不执行平台上传或发布。

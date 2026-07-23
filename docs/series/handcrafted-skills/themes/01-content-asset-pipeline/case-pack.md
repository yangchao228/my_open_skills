# 主题 01：一篇长文怎样成为跨平台内容资产

## 基本信息

- 源材料：公开文章《Loop Engineering 从入门到进阶手册》介绍稿
- 公开入口：[完整电子书免费获取](https://yangxingzhi.reai.group/zh/orange-books/loop-engineering-handbook)
- 诊断与事实确认日期：2026-07-12、2026-07-14
- 原案例参与 skills：`wenchang-review`、`zhihu-topic-hunter`、`xiaohongshu-topic-generator`、`long-to-cards`、`wechat-to-cards`、`md-img-r2`、`wenchang-publish-check`
- V2 回归新增：`article-to-illustrations`，并把 `wechat-to-cards` 明确为按需分支
- Publish-ready 卡片链新增：`cards-to-images`，把 `long-to-cards` 的卡片包继续生成成真实图片、逐图 QA 和 manifest
- 自适应生图恢复层新增：`resilient-imagegen` 与 `chatgpt-image-handoff`，按运行能力选择 Computer Use、内置生图、手动交接或本地渲染
- 资产矩阵 V3：补齐 3 张公众号 `wechat-inline` 贴图和 5 张知乎想法配图，并按真实产物重构小红书 8 张宣传卡
- 目标读者：手上已有长文、报告、复盘或课程材料，希望把内容工作沉淀成可复用流程的人
- 本期唯一 CTA：用一篇自己的公开长文复现这条链路，并反馈最值得保留或改造的 Skill

## 本期对外主张

这期宣传的是 `my_open_skills` 里的内容技能包：它把“长文跨平台分发”拆成可检查、可替换、可复现的工作步骤。

《Loop Engineering 从入门到进阶手册》介绍稿只作为真实输入，用来展示这组 Skills 怎样工作。平台稿不承担手册推广、领取转化或版本介绍任务。

## 源文诊断

### 核心判断

重复、跨轮次、需要外部反馈的 Agent 任务，应该从单条提示词升级为包含目标、状态、反馈、停止规则和人工确认的可控循环。

### 最强的可复用材料

- 用 Prompt、Checklist、普通工作流和 Loop 区分任务复杂度
- Loop 的四个判断条件：可验证、可停止、可纠错、可交接
- CI 自动修复与 UI 精准复刻两个反馈闭环案例
- 对权限、生产配置、数据删除和公开发布保留人工确认

### 不直接复用的材料

- 作者身份、私信获取方式和站外转化话术
- 未附原始来源的产品功能、版本号和人物引述
- 具体“已发布篇数”“章节数”“模板数”等版本性数字

## 图片交付状态

源文中的 3 张图片已经通过 R2 公网域名引用。原始只读检查结果为：3 个可继续复用的公网 URL，0 个本地图片需要上传或替换。

因此：

- `md-img-r2` 已完成图片状态核查，不产生上传、备份或正文改写。
- 本期展示的是 R2 图片源资产怎样被多平台复用；本轮没有新增上传，避免重复存储已有图片。
- 后续若源文或卡片资产仍引用本地图片，再以 dry-run 计划、审核 URL 和明确确认演示上传路径。

V2 回归随后选取一张已审核卡片插入公开 Markdown 样例，生成了 1 张本地图片、0 个问题、0 次外部写入的 [dry-run 报告](workflow-v2-illustrated-sample.md.image-publish-plan.json)。这次新增计划只验证插图与图片发布交接，不代表图片已经上传。

## 事实核验记录

作者已于 2026-07-14 确认源文中的事实字段和公开链接没有问题。本期仍采用收敛的对外口径，避免让版本性信息主导内容。

| 字段 | 核验结果 | 在平台稿中的处理 |
| --- | --- | --- |
| 完整电子书与 `loop-builder` 公开入口 | 已确认 | 保留为延伸阅读与复现入口 |
| 版本、章节、模板与文章篇数 | 已确认 | 不作为标题、封面或核心论点 |
| Loop 的结构、案例与人工确认边界 | 已确认 | 作为知乎论证和小红书卡片的核心材料 |
| 带时间性的产品功能与命令 | 已确认 | 不脱离原文扩写为泛化产品承诺 |

## 跨平台派生合同

### 知乎

- 核心问题：一篇已经完成的长文，怎样被一组 Skills 拆成知乎、小红书和发布检查？
- 文章结构：跨平台分发问题 → 7 个 Skills 的分工 → 三段中间产物 → 图片状态 → 人工确认 → 复现入口
- 保留材料：源文诊断、平台适配、卡片化、图片状态和发布检查的实际产物
- 放弃材料：手册推介、免费领取、版本数字和产品功能细节

### 知乎想法

- 核心判断：一篇母稿可以形成多种发布资产，但卡片稿必须继续走到真实图片、逐图 QA 和 Manifest。
- 5 页结构：四种发布资产 → 两条生产链 → 卡片成图链 → R2 条件分支 → 人工门禁。
- 交付：[知乎想法图文包](zhihu-idea-cards.md)、[5 张成图总览](assets/zhihu-idea/contact-sheet.png) 与 [Cards Manifest](zhihu-idea-manifest.md)。
- 当前状态：成图与逐图 QA 已完成，人工确认 `pending`，不进入平台编辑器。

### 小红书

- 核心场景：一篇已审核长文怎样继续形成真实正文、真实图片和可检查交付状态。
- 8 页结构：四种发布资产 → 真实文件 → 四层协作 → 两条生产链 → 卡片成图链 → R2 条件分支 → 人工门禁 → 完整提示词。
- 首屏钩子：一篇母稿，变成 4 种发布资产。
- 视觉证据：1 篇审核母稿、4 种发布形态、20 张本地成图和 4 份 Manifest。

### 公众号分发

- 核心主题：我是如何做多平台内容分发，并把流程开源成 Skills 技能包的
- 文章结构：分发痛点 → 7 个 Skills 分工 → 内容适配 → `md-img-r2` 与 R2 图片资产层 → 安全边界 → 开源产物与复现入口
- 重点巧思：公众号长文插图已通过 `md-img-r2` 进入 R2 并获得稳定公网引用；知乎长文插图仍处于计划阶段，平台原生图文保留本地 PNG
- 平台边界：R2 负责长文 Markdown 图片的公网引用；公众号贴图、知乎想法和小红书图文由人工上传本地 PNG
- 公众号贴图：新增 3 张 1600×900 `wechat-inline` 总结卡，分别展示四种发布资产、卡片成图链和 R2 条件分支。
- 朋友圈文案：围绕“内容适配 + 图片资产层”介绍这套开源 Skills 工作流。
- 社群文案：说明适用读者、四层职责、图片复用方式和公开复现入口。
- 交付：[公众号贴图包](wechat-inline-cards.md)、[3 张成图总览](assets/wechat-inline/contact-sheet.png) 与 [Cards Manifest](wechat-inline-manifest.md)。

## 三个设计判断

1. **主题优先**：用“跨平台内容资产”组织内容，读者首先看到的是问题链路，Skills 在关键节点提供可复现能力。
2. **源文优先**：保留已成形长文的论点与案例，平台适配只改变进入方式和表达结构。
3. **交付分层**：内容生成、图片状态和最终发布分开记录；图片已是公网 URL 时，图片上传阶段可以安全跳过。

## 复现路径

1. 打开公开原文，确认核心观点、图示和外链仍然可访问。
2. 用 `wenchang-review` 建立源文诊断，标记待核事实。
3. 用知乎与小红书选题 skill 分别选择平台入口，避免直接搬运标题。
4. 用 `wenchang-publish-check` 的 `preflight` 模式生成四种发布形态所需字段，并为公众号、知乎长文分别留下插图判断。
5. 用 `article-to-illustrations` 规划公众号、知乎长文插图；用 `long-to-cards` 生成标准卡片包。
6. 对 `publish_ready` 卡片运行 `cards-to-images`。生成式或混合式方案先交给 `resilient-imagegen` 以 `backend=auto` 检查运行能力；需要 ChatGPT 时进入 `chatgpt-image-handoff`，有 Computer Use 就自动执行，没有则导出 Handoff Pack 交给用户，再把下载结果导回统一 QA。本地确定性渲染继续直接生成真实图片。
7. 需要公网引用时，本地图片再进入 `md-img-r2` dry-run；直接上传平台可以保留本地 PNG。
8. 图片、卡片和发布字段汇总后，再用 `wenchang-publish-check` 的 `final` 模式输出状态和阻塞项。

## 当前交付状态

- 源文诊断、图片状态和事实确认已完成。
- [公众号母稿](wechat-draft.md) 已完成，主线为多平台内容分发、开源 Skills 技能包与 R2 图片资产复用。
- [知乎正式稿](zhihu-draft.md) 与 [小红书 8 页卡片稿](xiaohongshu-cards.md) 已基于这份 Case Pack 分别完成。
- 小红书卡片以 `delivery_mode=publish_ready` 进入 `cards-to-images`；8 张 1080×1440 成图与 [视觉总览](assets/contact-sheet.png) 已生成并完成逐图检查。
- [Cards Manifest](xiaohongshu-upload-manifest.md) 已记录文件、顺序、尺寸、ALT、渲染方式、QA、人工确认与 R2 状态；人工确认仍为 `pending`。
- `md-img-r2` 曾为 8 张小红书成图生成本地 dry-run：8 张待处理、0 个问题、0 次外部写入。该报告仅作为本地验证证据，不进入公开发布包；本次小红书使用本地 PNG 人工上传。
- [真实运行记录](run-report.md) 已记录各阶段输入、输出、验收与停止点。
- [发布包与最终检查](publish-check.md) 已整理标题、摘要、小红书正文描述、标签时效、插图判断与图片验收条件。
- [V2 插图计划](illustration-plan-v2.md)、[图片 Manifest](image-manifest-v2.md)、[插图回归样例](workflow-v2-illustrated-sample.md) 和 [完整回归记录](workflow-v2-regression.md) 已验证长文插图到 R2 dry-run 的交接。
- 公众号 2 张 1600×900 横图、知乎 2 张 1080×1440 竖图与 [视觉总览](assets/longform-v2/contact-sheet.png) 已生成并检查；公众号两张已进入 R2、改写正文引用并通过公网验收，知乎两张 dry-run 为 0 个问题且仍待处理。
- [公众号贴图包](wechat-inline-cards.md) 已生成 3 张 1600×900 本地 PNG，并通过逐图 QA；[Manifest](wechat-inline-manifest.md) 的人工确认仍为 `pending`。
- [知乎想法图文包](zhihu-idea-cards.md) 已生成正文、5 张 1080×1440 本地 PNG 和 [Manifest](zhihu-idea-manifest.md)，逐图 QA 通过，人工确认仍为 `pending`。
- 小红书 8 张宣传卡已按真实资产矩阵重构；当前总计 20 张正式本地成图和 4 份 Manifest。
- 重构后的 8 张小红书图片使用 `asset_url_policy=local`、`r2_state=not_planned`；既有 dry-run 报告不进入本次发布。
- [自适应 ChatGPT 生图规格](chatgpt-image-handoff-spec.json) 已整理为 8 个独立任务，默认 `backend=auto` 并优先 Computer Use；当前只完成公开规格和本地 Handoff 准备，尚未向 ChatGPT 提交。
- 公众号两张长文插图的 R2 实际上传已经完成；知乎两张插图的 R2 上传以及所有外部平台发布，仍保留人工确认。

# 主题 01：发布包与最终检查 V2

检查日期：2026-07-20

- Preflight：公众号、知乎长文、知乎想法和小红书发布字段与图片决策已形成。
- Final：当前状态为 `needs_review`，详细回归见 [多平台发布工作流 V2 回归](workflow-v2-regression.md)。

## 来源基线

- 正式案例源：[Case Pack](case-pack.md)
- 事实状态：`verified`
- 内容审核状态：`reviewed`
- 唯一 CTA：用一篇自己的公开长文复现这条链路，并反馈最值得保留或改造的 Skill

## 发布判断

- **公众号：`needs_review`。** 母稿、发布字段和两张 1600×900 横图已经完成；两张图片已上传 R2、替换正文引用并通过公网验收，等待终审和编辑器验收。
- **公众号贴图：`needs_review`。** 3 张 1600×900 `wechat-inline` 图片与 Manifest 已完成并通过逐图 QA，等待用户决定是否插入正式稿。
- **知乎：`needs_review`。** 标题、论证、来源入口、两张 1080×1440 插图和 dry-run 已完成；等待 R2 决策和编辑器验收。
- **知乎想法：`needs_review`。** 正文描述、普通话题标签、5 张 1080×1440 配图与 Manifest 已完成并通过逐图 QA，等待用户确认和编辑器验收。
- **小红书：`needs_review`。** `long-to-cards -> cards-to-images` 已产出 8 页文案、8 张 1080×1440 成图和标准 manifest；逐图视觉检查通过，等待用户确认，热门标签没有实时核验。
- **R2：公众号已完成，知乎等待确认。** 公众号两张长文插图已上传并通过公网验收；知乎两张插图的 dry-run 为 0 个问题，仍未上传。公众号贴图、知乎想法和小红书图文均使用本地 PNG 人工上传。
- **外部操作：仅执行公众号 R2。** 尚未登录平台、上传平台图片或发布内容。

## 必做项

- [ ] 终审公众号母稿，确认标题、篇幅和 R2 图片复用表述。
- [x] 分别完成公众号与知乎的插图判断、正文锚点和事实约束。
- [x] 按 [插图计划](illustration-plan-v2.md) 制作公众号两张横图和知乎两张竖图。
- [x] 将四张正式插图以相对路径插入平台稿，更新 manifest，并完成两份 R2 dry-run。
- [x] 上传公众号两张长文插图，替换 Markdown 引用并验证两条公网 URL。
- [ ] 上传知乎两张长文插图，替换 Markdown 引用并验证两条公网 URL。
- [x] 将小红书 8 页卡片稿制作成 1080 × 1440 图片，并逐页检查字号、留白、错别字和末页仓库名。
- [x] 将小红书卡片链记录为 `delivery_mode=publish_ready`，并补齐真实图片、尺寸、顺序和逐图 QA 的 [cards manifest](xiaohongshu-upload-manifest.md)。
- [x] 生成公众号 `wechat-inline` 内容包、3 张真实贴图和 [Cards Manifest](wechat-inline-manifest.md)。
- [x] 生成知乎想法正文、5 张真实配图和 [Cards Manifest](zhihu-idea-manifest.md)。
- [ ] 用户确认小红书 8 张成图可以用于平台上传。
- [ ] 用户确认公众号 3 张贴图是否插入正式稿。
- [ ] 用户确认知乎想法正文与 5 张配图可以进入平台编辑器。
- [ ] 发布当天打开原文入口与 GitHub Case Pack，确认链接可访问。
- [ ] 在知乎编辑器中检查 7 个 Skills 分工表和仓库链接的换行。
- [ ] 在小红书编辑器中确认封面在缩略图尺寸下仍能读到“一篇母稿”和“4 种发布资产”。

## 公众号发布包

- 标题：我是如何做多平台内容分发，并把流程开源成 Skills 技能包的
- 备选标题：
  1. 一篇长文如何变成公众号、知乎和小红书内容资产
  2. 我把多平台内容分发拆成 Skills，还补上了图片资产层
  3. 从母稿到发布包：我开源了一套多平台内容工作流
- 搜索标题：多平台内容分发工作流：内容 Skills、R2 图片存储与发布检查
- 摘要：我用一篇公开长文测试了 7 个内容 Skills，从源文诊断、平台适配、卡片化一直走到发布检查。其中 `md-img-r2` 为公众号和知乎长文插图生成可审核的 R2 公网引用；平台图文继续人工上传本地 PNG。
- 关键词：`AI Agent`、`Agent Skills`、`多平台内容分发`、`Cloudflare R2`、`开源工作流`
- 封面文案：一篇长文，7 个 Skills，一套多平台内容资产
- 插图判断：`required`
- 图片交付：见 [长文插图计划 V2](illustration-plan-v2.md)；完整流程图和 R2 图片资产层机制图已插入正文。
- 分享文案：我把多平台内容分发拆成了 7 个 Skills，还为图片补了一层 R2 源资产：内容按平台重新组织，图片保留稳定公网引用，整条链路已经开源。
- 评论引导：你在多平台分发里最容易卡住的是内容改写、图片处理、平台格式，还是发布前检查？
- 公众号贴图包：[wechat-inline-cards.md](wechat-inline-cards.md)
- 贴图成图：3 张 1600×900 PNG，见 [总览](assets/wechat-inline/contact-sheet.png)
- 贴图 Manifest：[wechat-inline-manifest.md](wechat-inline-manifest.md)
- 贴图状态：`generated=3`、QA `passed=3`、人工确认 `pending`、R2 `not_planned`

## 知乎发布包

- 标题：一篇已经写完的长文，怎样被 7 个 Skills 拆成知乎、小红书和发布包？
- 判断型标题：多平台分发真正缺的，是一套能留下中间状态的内容工作流
- 经验型标题：我用一篇真实长文，跑完了从平台适配到图片交付的 Skills 链路
- 开头导语：我用一篇已经完成的公开长文测试 `my_open_skills`，验证一组职责清楚的 Skill 能否留下可检查、可替换和可复现的多平台内容资产。
- 摘要：我用一篇公开长文测试了 `my_open_skills` 里的 7 个内容 Skills。它们分别处理源文诊断、平台入口、卡片化、图片状态和发布检查，最终留下可复查的 Case Pack 与两端平台稿。
- 话题标签：`AI Agent`、`Agent Skills`、`内容创作`、`知识管理`、`开源项目`
- 封面文案：一篇长文，我拆给了 7 个 Skills
- 插图判断：`recommended`
- 配图交付：见 [长文插图计划 V2](illustration-plan-v2.md)；正式稿已插入完整链路图和 R2 图片资产图两张。
- 分享文案：我把一篇公开长文交给 7 个 Skills，留下了一套可以替换、检查和复现的内容工作流。
- 评论引导：你的长文跨平台分发时，最费力的是取舍、平台改写、图片交付，还是发布前检查？

## 知乎想法发布包

- 正文与卡片包：[zhihu-idea-cards.md](zhihu-idea-cards.md)
- 标题：一篇母稿，怎样真正变成四种发布资产？
- 首句：我最近用一篇已经完成事实核验的公开长文，把自己的内容 Skills 技能包完整跑了一遍。
- 图片顺序：严格使用 `01-one-source-four-assets.png` 至 `05-human-final-gate.png`
- 卡片交付模式：`publish_ready`
- 平台 profile：`zhihu-idea`
- 成图目录：`assets/zhihu-idea/`
- Cards Manifest：[zhihu-idea-manifest.md](zhihu-idea-manifest.md)
- 渲染状态：`generated`
- 逐图视觉检查：`passed`
- 人工确认：`pending`
- 资产策略：`local`，当前不需要 R2 公网 URL
- 普通话题标签：`AI Agent`、`AI工作流`、`内容创作`、`多平台内容分发`、`数字资产`
- 实时热门标签：`unverified`
- CTA：如果你手上已经有一篇长文，最想先复用这条链路里的哪一步？

## 小红书发布包

- 标题：一篇母稿，变成 4 种发布资产
- 备选标题：
  1. 我用一篇真实长文，跑通了四种平台发布资产
  2. 从母稿到 20 张图片：我怎样测试这套开源 Skills
- 首屏文案：一篇母稿，变成 4 种发布资产
- 首句钩子：我用一篇已经完成事实核验的公开长文，把公众号、知乎长文、知乎想法和小红书四种发布形态完整跑了一遍。
- 发布正文：使用 [小红书 8 页卡片稿](xiaohongshu-cards.md) 中的“发布正文”。
- 图片顺序：严格使用 `01-cover.png` 至 `08-reproduce.png`。
- 卡片交付模式：`publish_ready`
- 平台 profile：`xiaohongshu`
- 成图目录：`assets/`
- Cards manifest：[小红书 Cards Manifest 与上传清单](xiaohongshu-upload-manifest.md)
- 渲染状态：`generated`
- 逐图视觉检查：`passed`
- 人工确认：`pending`
- 资产策略：`local`，小红书人工上传本地 PNG，不进入本次 R2 apply
- `core_tags`：`#AIAgent` `#AI工作流` `#内容创作`
- `scene_tags`：`#多平台内容分发` `#知识管理` `#数字资产`
- `series_tags`：`#我亲手打造的Skills` `#开源项目`
- `verified_hot_tags`：`status=unverified`，`checked_at`、`source` 和 `values` 留空，发布当天需要时再核验。
- 图片计划：8 页依次展示四种发布资产、真实文件、四层协作、两条生产链、卡片成图、R2 条件分支、人工门禁和完整提示词。
- 唯一 CTA：如果你手上已经有一篇长文，最想先复用这条链路里的哪一步？

## 长期资产建议

- 保留资产：源文诊断、事实核验记录、四种发布形态、20 张正式成图、4 份 Manifest、发布前检查和发布后反馈。
- 资产类型：主题化 Case Pack。
- 建议归档：`docs/series/handcrafted-skills/themes/01-content-asset-pipeline/`。
- 发布后补充：各平台链接、首周评论中出现的真实问题、读者复现反馈，以及下一期应该保留或删掉的步骤。

## 交接状态

```yaml
content_state:
  source:
    body_file: case-pack.md
    fact_status: verified
    review_status: reviewed
  platforms:
    wechat:
      body_file: wechat-draft.md
      illustration_status: generated_and_inserted
      inline_cards_file: wechat-inline-cards.md
      inline_manifest_file: wechat-inline-manifest.md
    zhihu:
      body_file: zhihu-draft.md
      illustration_status: generated_and_inserted
    zhihu_idea:
      cards_file: zhihu-idea-cards.md
      manifest_file: zhihu-idea-manifest.md
      caption_status: ready
      tag_freshness: unverified
    xiaohongshu:
      cards_file: xiaohongshu-cards.md
      caption_status: ready
      tag_freshness: unverified
  cards:
    xiaohongshu:
      delivery_mode: publish_ready
      platform_profile: xiaohongshu
      package_file: xiaohongshu-cards.md
      images_dir: assets
      manifest_file: xiaohongshu-upload-manifest.md
      render_status: generated
      visual_qa_status: passed
      human_confirmation: pending
      asset_url_policy: local
      r2_state: not_planned
    wechat_inline:
      delivery_mode: publish_ready
      platform_profile: wechat-inline
      package_file: wechat-inline-cards.md
      images_dir: assets/wechat-inline
      manifest_file: wechat-inline-manifest.md
      render_status: generated
      visual_qa_status: passed
      human_confirmation: pending
      asset_url_policy: local
      r2_state: not_planned
    zhihu_idea:
      delivery_mode: publish_ready
      platform_profile: zhihu-idea
      package_file: zhihu-idea-cards.md
      images_dir: assets/zhihu-idea
      manifest_file: zhihu-idea-manifest.md
      render_status: generated
      visual_qa_status: passed
      human_confirmation: pending
      asset_url_policy: local
      r2_state: not_planned
  images:
    plan_file: illustration-plan-v2.md
    manifest_file: image-manifest-v2.md
    r2_report_file:
      wechat: wechat-draft.md.image-publish-plan.json
      zhihu: zhihu-draft.md.image-publish-plan.json
    r2_status: partially_verified
    r2_status_by_platform:
      wechat: verified
      zhihu: planned
    r2_scope: longform_only
  publish_gate:
    mode: final
    status: needs_review
    blockers:
      - confirm the eight Xiaohongshu, three WeChat inline, and five Zhihu Idea images before platform delivery
      - optionally verify current hot tags on publication day
      - confirm the two remaining Zhihu long-form R2 uploads and Markdown URL rewrites
      - complete editor layout and link checks before platform publishing
  next_step:
    skill: wenchang-publish-check
    reason: rerun final after human confirmation of all three card sets and the remaining Zhihu R2 decision
    user_decision_needed: true
  handoff:
    from_stage: cards-to-images
    to_stage: human-image-confirmation
    accepted_inputs:
      - illustration-plan-v2.md
      - image-manifest-v2.md
      - workflow-v2-regression.md
      - xiaohongshu-upload-manifest.md
      - wechat-inline-manifest.md
      - zhihu-idea-manifest.md
    ignored_context:
      - private source files
      - account sessions
    stop_condition: user approves R2 apply or external publishing
```

# 主题 01：知乎想法 Cards Manifest

- `delivery_mode`：`publish_ready`
- `platform_profile`：`zhihu-idea`
- `asset_url_policy`：`local`
- 输出：5 张 1080 × 1440 PNG 与 [总览](assets/zhihu-idea/contact-sheet.png)
- 生成状态：5 张 `generated`
- 逐图 QA：5 张 `passed`
- 人工确认：`pending`
- R2 状态：`not_planned`

| card_id | source_card | local_path | width | height | alt_text | render_strategy | generation_status | visual_qa_status | human_confirmation | r2_state |
| --- | --- | --- | ---: | ---: | --- | --- | --- | --- | --- | --- |
| ZHIHU-IDEA-01 | 四种发布资产 | `assets/zhihu-idea/01-one-source-four-assets.png` | 1080 | 1440 | 一篇审核母稿连接公众号长文、知乎长文、知乎想法和小红书图文四种发布资产 | deterministic | generated | passed | pending | not_planned |
| ZHIHU-IDEA-02 | 两条生产链 | `assets/zhihu-idea/02-two-production-branches.png` | 1080 | 1440 | 审核母稿分别进入长文插图分支和卡片成图分支，再形成不同平台资产 | deterministic | generated | passed | pending | not_planned |
| ZHIHU-IDEA-03 | 卡片成图链 | `assets/zhihu-idea/03-copy-is-not-delivery.png` | 1080 | 1440 | 卡片文案依次生成真实 PNG、完成逐图 QA 并写入 Cards Manifest | deterministic | generated | passed | pending | not_planned |
| ZHIHU-IDEA-04 | R2 条件分支 | `assets/zhihu-idea/04-r2-when-needed.png` | 1080 | 1440 | 本地图片可以直接上传平台，需要公网引用时再经过 R2 计划与人工确认 | deterministic | generated | passed | pending | not_planned |
| ZHIHU-IDEA-05 | 人工门禁 | `assets/zhihu-idea/05-human-final-gate.png` | 1080 | 1440 | 已完成的内容与图片资产进入人工确认，外部上传和平台发布保持待确认 | deterministic | generated | passed | pending | not_planned |

知乎想法正文、标签与来源说明记录在 [知乎想法图文包](zhihu-idea-cards.md)。用户确认前不进入平台编辑器。

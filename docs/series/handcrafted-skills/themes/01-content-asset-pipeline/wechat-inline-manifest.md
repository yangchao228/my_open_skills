# 主题 01：公众号贴图 Cards Manifest

- `delivery_mode`：`publish_ready`
- `platform_profile`：`wechat-inline`
- `asset_url_policy`：`local`
- 输出：3 张 1600 × 900 PNG 与 [总览](assets/wechat-inline/contact-sheet.png)
- 生成状态：3 张 `generated`
- 逐图 QA：3 张 `passed`
- 人工确认：`pending`
- R2 状态：`not_planned`

| card_id | source_card | local_path | width | height | alt_text | render_strategy | generation_status | visual_qa_status | human_confirmation | r2_state |
| --- | --- | --- | ---: | ---: | --- | --- | --- | --- | --- | --- |
| WECHAT-INLINE-01 | 四种发布资产 | `assets/wechat-inline/01-four-release-forms.png` | 1600 | 900 | 同一篇审核母稿分别形成公众号长文、知乎长文、知乎想法和小红书图文四种发布资产 | deterministic | generated | passed | pending | not_planned |
| WECHAT-INLINE-02 | 卡片成图链 | `assets/wechat-inline/02-copy-to-checked-images.png` | 1600 | 900 | 卡片文案依次经过真实图片生成、逐张视觉检查和 Manifest 记录，最后进入人工确认 | deterministic | generated | passed | pending | not_planned |
| WECHAT-INLINE-03 | R2 条件分支 | `assets/wechat-inline/03-local-or-public.png` | 1600 | 900 | 经过检查的本地图片可以直接上传平台，需要公网引用时再经过 dry-run、人工确认和 R2 上传 | deterministic | generated | passed | pending | not_planned |

建议插入位置记录在 [公众号贴图包](wechat-inline-cards.md)。用户确认前不写入正式公众号稿。

# 主题 01：多平台发布工作流 V2 回归

回归日期：2026-07-14

## 回归目标

验证审核后的真实母稿能否沿着 V2 链路形成：

- 公众号、知乎长文、知乎想法和小红书各自的发布资产
- 公众号和知乎各自的插图判断
- 带正文锚点、事实约束、提示词和 ALT 的插图计划
- 已插入正式本地插图的公众号与知乎 Markdown
- 可交给 `md-img-r2` 的图片 manifest
- 从卡片文案继续生成真实图片、逐图 QA 和 `cards-manifest` 的 publish-ready 卡片链
- 无外部写入的 R2 dry-run
- 区分普通主题标签和实时热门标签的发布门禁

## 使用的真实输入

- [主题 Case Pack](case-pack.md)
- [公众号母稿](wechat-draft.md)
- [知乎稿](zhihu-draft.md)
- [小红书卡片稿](xiaohongshu-cards.md)
- [8 张已审核小红书成图](assets/contact-sheet.png)
- [公众号贴图包与 3 张成图](wechat-inline-cards.md)
- [知乎想法图文包与 5 张成图](zhihu-idea-cards.md)
- [4 张长文插图总览](assets/longform-v2/contact-sheet.png)

公众号和知乎长文继续保留原案例的 7 Skills 历史运行叙事。本次资产矩阵回归补齐公众号贴图和知乎想法，并把小红书宣传卡改为展示当前真实产物、共享链路与人工门禁。

## 阶段结果

| 阶段 | Skill | 产物 | 结果 |
| --- | --- | --- | --- |
| 发布预检 | `wenchang-publish-check` | [发布包](publish-check.md) | 三个平台字段齐全；热门标签仍需发布当天核验 |
| 长文插图判断 | `article-to-illustrations` | [插图计划](illustration-plan-v2.md) | 公众号 `required`；知乎 `recommended` |
| 插图生成与插入 | `article-to-illustrations`、`canvas-design` | [4 张长文插图](assets/longform-v2/contact-sheet.png) | 公众号 2 张横图、知乎 2 张竖图均已检查并插入正式稿 |
| 图片 manifest | `article-to-illustrations` | [图片 Manifest](image-manifest-v2.md) | 路径、锚点、ALT、来源、尺寸和 R2 状态齐全 |
| 图片发布交付 | `md-img-r2` | [公众号报告](wechat-draft.md.image-publish-plan.json)、[知乎报告](zhihu-draft.md.image-publish-plan.json) | 公众号 `verified=2`；知乎 `planned=2`、`issues=0` |
| 卡片包 | `long-to-cards` | [小红书卡片稿](xiaohongshu-cards.md) | `delivery_mode=publish_ready`，没有停在文案阶段 |
| 卡片成图与检查 | `cards-to-images` | [8 张成图和 Cards Manifest](xiaohongshu-upload-manifest.md) | `generated=8`、QA `passed=8`、人工确认 `pending` |
| 公众号贴图 | `wechat-to-cards -> long-to-cards -> cards-to-images` | [3 张贴图和 Manifest](wechat-inline-manifest.md) | `generated=3`、QA `passed=3`、人工确认 `pending` |
| 知乎想法 | `long-to-cards -> cards-to-images` | [正文、5 张成图和 Manifest](zhihu-idea-cards.md) | `generated=5`、QA `passed=5`、人工确认 `pending` |
| 宣传卡重构 | `cards-to-images` | [四种发布资产总览](assets/contact-sheet.png) | 8 张重新生成、逐图 QA 通过、按本地 PNG 交付 |
| 最终检查 | `wenchang-publish-check` | 本文件与 [content_state](content-state-v2.yaml) | `needs_review`，没有伪装成已经可直接发布 |

## 正式插图验收

- 视觉体系：沿用 [Open Weave](visual-philosophy.md)
- 生成方式：确定性画布渲染，保证中文、Skill 名称、箭头关系和平台比例可检查
- 公众号：2 张 1600 × 900 横图
- 知乎：2 张 1080 × 1440 竖图
- 总览：[assets/longform-v2/contact-sheet.png](assets/longform-v2/contact-sheet.png)
- 正文插入：4 张图片均使用相对路径和描述性 ALT

## R2 Dry-run 证据

- 公众号输入：`wechat-draft.md`
- 公众号结果：`planned=2`、`issues=0`
- 知乎输入：`zhihu-draft.md`
- 知乎结果：`planned=2`、`issues=0`
- 对象前缀：`my-open-skills/theme-01/longform-v2`
- 上传：未执行
- Markdown 改写：未执行
- URL 公网验收：未执行，四个计划 URL 尚不能当作已存在链接使用

## 发布资产覆盖

### 公众号

- 标题、搜索标题、摘要、封面文案、分享文案和关键词：已生成
- 插图判断：`required`
- 两张 1600 × 900 横图：已生成、检查、插入并完成 dry-run
- 三张 1600 × 900 `wechat-inline` 贴图：已生成、逐图检查并写入 Cards Manifest，等待人工确认后决定是否插入正文

### 知乎

- 问题型标题、导语、摘要、话题和评论引导：已生成
- 插图判断：`recommended`
- 两张 1080 × 1440 竖图：已生成、检查、插入并完成 dry-run

### 知乎想法

- 正文描述、CTA、普通话题标签：已生成
- 五张 1080 × 1440 配图：已生成并逐张检查
- Cards Manifest：路径、尺寸、ALT、生成、QA、人工确认和 R2 状态齐全
- 人工确认：`pending`

### 小红书

- 封面标题、首句钩子、发布正文、图片顺序和唯一 CTA：已生成
- `core_tags`、`scene_tags`、`series_tags`：已生成
- `verified_hot_tags`：`unverified`，没有使用模型记忆冒充当前热门
- `cards-to-images`：8 张本地 PNG 已生成并逐张检查
- `cards-manifest`：文件、顺序、尺寸、ALT、渲染方式、QA、人工确认和 R2 状态齐全
- 逐图回归：发现并修复连线穿透、安全区溢出和中英混合标签缺字；修复后重新生成并逐张检查 8 页
- R2 决策：小红书使用本地 PNG 人工上传，`r2_state=not_planned`；既有 8 张 dry-run 报告仅作为历史验证证据
- 人工确认：`pending`，因此仍保持 `needs_review`

## Final 检查

- 状态：`needs_review`
- 已通过：事实基线、四种发布形态、发布元数据、插图决策、20 张正式本地成图、逐图 QA、4 份 manifest、R2 dry-run
- 阻塞项：
  1. 如果发布时需要热门标签，在平台发布当天查询并记录来源与时间。
  2. 用户确认小红书 8 张、公众号贴图 3 张和知乎想法 5 张图片可以进入平台交付。
  3. 公众号两张插图已完成 R2 上传与 Markdown URL 替换；知乎两张插图进入同一步骤前仍需明确确认。
  4. 进入平台编辑器后检查排版、链接和图片缩放。

## 回归结论

V2 已能从审核后的母稿形成公众号长文、知乎长文、知乎想法和小红书四种发布形态。当前共有 20 张正式本地成图：4 张长文插图、3 张公众号贴图、5 张知乎想法配图和 8 张小红书宣传卡；四份 Manifest 分别记录状态。时效标签、用户确认和外部写入保持为可见门禁。本次回归没有执行外部上传或平台发布。

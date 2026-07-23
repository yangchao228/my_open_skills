# Content Skills

[English](README.md)

`skills/content/` 存放文昌内容工作流。

文昌是一组可组合的 skills，用来把选题、趋势、外部材料或草稿推进到经过审核的平台正文、插图资产和发布包。

## 推荐入口

需要完整工作流时，使用 [wenchang-orchestrator](wenchang-orchestrator)。

只需要判断下一步时，使用 [wenchang-router](wenchang-router)。

## 核心链路

```text
wenchang-orchestrator
  -> wenchang-router
  -> storm-research
  -> wenchang-research
  -> wenchang-wechat-writer
  -> wenchang-review
  -> wenchang-publish-check（preflight）
  -> [公众号/知乎：article-to-illustrations -> 自适应生图 -> md-img-r2 plan]
  -> [卡片平台：long-to-cards -> cards-to-images -> 自适应生图 -> 人工确认]
  -> [生成恢复：resilient-imagegen -> 需要时进入 chatgpt-image-handoff]
  -> [可选公网 URL：md-img-r2 plan]
  -> wenchang-publish-check（final）
```

卡片分支覆盖小红书、公众号文内卡片、知乎想法和通用 Carousel。`publish_ready` 会继续生成并检查真实图片；只有显式 `copy_only` 才停在文案。生成式或混合式工作通过 `resilient-imagegen` 的 `backend=auto` 路由；`chatgpt-image-handoff` 提供 Computer Use 和手动兜底，并统一回到本地 QA。`wechat-to-cards` 在共享链路外围补充朋友圈、社群和公众号插入说明。

## Skills

- [wenchang-orchestrator](wenchang-orchestrator)：完整工作流总控
- [wenchang-router](wenchang-router)：阶段和平台路由
- [zhihu-topic-hunter](zhihu-topic-hunter)：基于主题的知乎选题发现与排序
- [xiaohongshu-topic-generator](xiaohongshu-topic-generator)：小红书选题生成和卡片大纲规划
- [long-to-cards](long-to-cards)：把长文材料复用为卡片式社交内容包
- [redbook-cards-skill](redbook-cards-skill)：把文章切成可在浏览器预览和截图的小红书 HTML 卡片页
- [cards-to-images](cards-to-images)：把审核后的卡片包渲染成经过检查的平台图片和 cards manifest
- [resilient-imagegen](resilient-imagegen)：路由并恢复逐张执行的多图生成任务
- [chatgpt-image-handoff](chatgpt-image-handoff)：自适应选择 Computer Use、内置生图、手动 ChatGPT 交接或本地渲染，并把结果导回 QA
- [wechat-to-cards](wechat-to-cards)：为共享卡片链路补充公众号专用贴图约束和分发素材
- [article-to-illustrations](article-to-illustrations)：长文插图判断、生成计划、正文插入和图片 manifest
- [storm-research](storm-research)：多视角研究地图
- [wenchang-research](wenchang-research)：基于来源的事实采证
- [wenchang-wechat-writer](wenchang-wechat-writer)：公众号风格长文起稿
- [wenchang-review](wenchang-review)：草稿诊断和编辑
- [wenchang-publish-check](wenchang-publish-check)：发布预检包和最终发布门禁

## 边界

这些 skills 不会执行外部发布，也不会在缺少用户确认时做最终不可逆决策。可选的 Computer Use 提交和参考图上传需要操作前确认，账号与运行状态始终留在本地。

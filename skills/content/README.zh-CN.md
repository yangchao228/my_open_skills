# Content Skills

[English](README.md)

`skills/content/` 存放文昌内容工作流。

文昌是一组可组合的 skills，用来把选题、趋势、外部材料或草稿推进到可发布的内容包。

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
  -> wenchang-publish-check
```

## Skills

- [wenchang-orchestrator](wenchang-orchestrator)：完整工作流总控
- [wenchang-router](wenchang-router)：阶段和平台路由
- [zhihu-topic-hunter](zhihu-topic-hunter)：基于主题的知乎选题发现与排序
- [xiaohongshu-topic-generator](xiaohongshu-topic-generator)：小红书选题生成和卡片大纲规划
- [long-to-cards](long-to-cards)：把长文材料复用为卡片式社交内容包
- [wechat-to-cards](wechat-to-cards)：把公众号文章复用为卡片和分发素材
- [storm-research](storm-research)：多视角研究地图
- [wenchang-research](wenchang-research)：基于来源的事实采证
- [wenchang-wechat-writer](wenchang-wechat-writer)：公众号风格长文起稿
- [wenchang-review](wenchang-review)：草稿诊断和编辑
- [wenchang-publish-check](wenchang-publish-check)：发布前资产检查

## 边界

这些 skills 不会执行外部发布、上传文件、使用私有账号会话，或在没有用户确认的情况下做最终不可逆决策。

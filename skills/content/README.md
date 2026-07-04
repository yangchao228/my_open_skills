# Content Skills

`skills/content/` contains the Wenchang content workflow.

Wenchang is a set of composable skills for moving from a topic, trend, external material, or draft into a publish-ready content package.

## Recommended Entry

Use [wenchang-orchestrator](wenchang-orchestrator) when you want the full workflow.

Use [wenchang-router](wenchang-router) when you only need to decide the next step.

## Core Flow

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

- [wenchang-orchestrator](wenchang-orchestrator): full workflow coordinator
- [wenchang-router](wenchang-router): stage and platform router
- [zhihu-topic-hunter](zhihu-topic-hunter): theme-based Zhihu topic hunting and ranking
- [xiaohongshu-topic-generator](xiaohongshu-topic-generator): Xiaohongshu topic generation and card-outline planning
- [storm-research](storm-research): multi-perspective research map
- [wenchang-research](wenchang-research): source-backed evidence gathering
- [wenchang-wechat-writer](wenchang-wechat-writer): WeChat-style long-form drafting
- [wenchang-review](wenchang-review): draft diagnosis and editing
- [wenchang-publish-check](wenchang-publish-check): pre-publish asset check

## Boundary

These skills do not publish externally, upload files, use private account sessions, or make final irreversible decisions without user confirmation.

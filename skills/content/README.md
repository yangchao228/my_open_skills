# Content Skills

[中文版本](README.zh-CN.md)

`skills/content/` contains the Wenchang content workflow.

Wenchang is a set of composable skills for moving from a topic, trend, external material, or draft into reviewed platform bodies, illustration assets, and a verified publish package.

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
  -> wenchang-publish-check (preflight)
  -> [WeChat/Zhihu: article-to-illustrations -> adaptive image generation -> md-img-r2 plan]
  -> [Card platforms: long-to-cards -> cards-to-images -> adaptive image generation -> human confirmation]
  -> [Generative recovery: resilient-imagegen -> chatgpt-image-handoff when selected]
  -> [Optional public URLs: md-img-r2 plan]
  -> wenchang-publish-check (final)
```

The card branch covers Xiaohongshu, WeChat inline cards, Zhihu Idea, and generic carousels. `publish_ready` continues to real checked images; only explicit `copy_only` stops at copy. Generative or mixed work uses `resilient-imagegen` with `backend=auto`; `chatgpt-image-handoff` provides Computer Use and manual fallback while converging on the same local QA. `wechat-to-cards` adds WeChat-specific Moments, community, and insertion assets around the shared branch.

## Skills

- [wenchang-orchestrator](wenchang-orchestrator): full workflow coordinator
- [wenchang-router](wenchang-router): stage and platform router
- [zhihu-topic-hunter](zhihu-topic-hunter): theme-based Zhihu topic hunting and ranking
- [xiaohongshu-topic-generator](xiaohongshu-topic-generator): Xiaohongshu topic generation and card-outline planning
- [long-to-cards](long-to-cards): long-form source repurposing into card-based social packages
- [redbook-cards-skill](redbook-cards-skill): repository candidate for article-to-Xiaohongshu HTML cards; ClawHub release is blocked pending third-party license review
- [cards-to-images](cards-to-images): render approved card packages into checked platform images and a cards manifest
- [resilient-imagegen](resilient-imagegen): route and recover serial multi-image generation jobs
- [chatgpt-image-handoff](chatgpt-image-handoff): adaptively use Computer Use, built-in generation, manual ChatGPT handoff, or local rendering and import outputs into QA
- [wechat-to-cards](wechat-to-cards): WeChat-specific adapter for inline-card requirements and distribution assets
- [article-to-illustrations](article-to-illustrations): long-form illustration decisions, generation plans, insertion, and image manifests
- [storm-research](storm-research): multi-perspective research map
- [wenchang-research](wenchang-research): source-backed evidence gathering
- [wenchang-wechat-writer](wenchang-wechat-writer): WeChat-style long-form drafting
- [wenchang-review](wenchang-review): draft diagnosis and editing
- [wenchang-publish-check](wenchang-publish-check): preflight publish package and final release check

## Boundary

These skills do not publish externally or make final irreversible decisions without user confirmation. Optional Computer Use submission and reference upload require action-time confirmation, while account and run state stay local.

## ClawHub

Ready content skills are released individually under `@yangchao228`; use the repository [release ledger](../../docs/clawhub-releases.md) as the status source. Registry releases include the same compact creator hook while public promotion remains organized by theme-level Case Packs.

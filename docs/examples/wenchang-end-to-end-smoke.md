# Wenchang End-to-End Smoke

This public smoke shows how Wenchang turns one reviewed source into WeChat, Zhihu, Xiaohongshu, and Zhihu Idea delivery artifacts. Publish-ready card branches continue to real checked images. The smoke stops before human image approval, external upload, and platform publishing.

## Input

```text
I have a source-backed article about turning a personal knowledge base from a collection folder into a reusable workbench.

Adapt it for WeChat, Zhihu, Xiaohongshu, and Zhihu Idea. Prepare titles, summaries, captions and tags, decide whether the two long-form versions need illustrations, turn publish-ready card packages into checked local images, prepare an R2 dry-run only where public URLs are useful, and run a final check. Stop before human approval and external writes.
```

## 1. Route With `wenchang-router`

The source is reviewed, so the workflow enters at publish preflight instead of repeating topic discovery and drafting.

```yaml
content_state:
  request:
    current_stage: publish-preflight
    target_platforms: [wechat, zhihu, xiaohongshu]
  source:
    body_file: source.md
    fact_status: verified
    review_status: reviewed
  cards:
    delivery_mode: publish_ready
    platform_profile: xiaohongshu
    render_status: not_started
    visual_qa_status: pending
    human_confirmation: pending
    asset_url_policy: local
    r2_state: not_planned
  images:
    r2_status: not_planned
  publish_gate:
    mode: preflight
    status: blocked
    blockers: []
  next_step:
    skill: wenchang-publish-check
    reason: generate the multi-platform package and illustration decisions
    user_decision_needed: false
```

## 2. Preflight With `wenchang-publish-check`

```md
## Decision
- Mode: preflight
- Status: blocked
- Blockers: illustration plan and platform bodies are not complete

## WeChat
- Title: Turn Your Knowledge Base Into A Reusable Workbench
- Search title: Personal Knowledge Base Workflow: From Collection To Reuse
- Summary: A practical workflow for turning saved information into repeated judgment and output.
- Illustration decision: required; one mechanism diagram

## Zhihu
- Question title: Why Do Personal Knowledge Bases Become Collection Folders?
- Opening lead: More capture does not guarantee more retrieval, judgment, or output.
- Summary: A source-backed explanation and a small workflow readers can test.
- Illustration decision: recommended; one comparison diagram

## Xiaohongshu
- Cover title: Your Knowledge Base Needs A Reuse Loop
- First-line hook: If your notes keep growing but your output does not, inspect the workflow before adding another tool.
- Body caption: <platform-adapted caption>
- Image order: cover -> problem -> mechanism -> checklist -> CTA
- Core tags: [personal knowledge management, writing workflow]
- Scene tags: [note reuse, knowledge work]
- Series tags: []
- Verified hot tags: unverified
```

## 3. Run Platform Branches

### WeChat And Zhihu

Use `article-to-illustrations` to create separate decisions and slots. Each slot includes a body anchor, reader purpose, factual constraints, ratio, prompt, alt text, and status.

After the user approves the plan, generate or accept local images, inspect them, insert relative references into each formal platform body, and write an image manifest.

### Xiaohongshu

Use `long-to-cards` with `delivery_mode=publish_ready` and `platform_profile=xiaohongshu` to produce the card sequence, cover title, first-line hook, body caption, image order, CTA, freshness-aware tags, and image-production handoff.

### WeChat Inline Cards And Zhihu Idea

Use the same canonical card path with `platform_profile=wechat-inline` or `zhihu-idea`. Use `wechat-to-cards` for Moments copy, community sharing, and WeChat-specific insertion notes around the shared card package.

## 4. Render Card Images With `cards-to-images`

For every `publish_ready` card package:

```text
approved card package
  -> deterministic render or resilient-imagegen backend routing
  -> optional chatgpt-image-handoff through Computer Use or manual pack
  -> imported real local PNG or JPG files
  -> per-image visual QA and revision
  -> cards-manifest
  -> human confirmation gate
```

The workflow may stop after card copy only when the user explicitly selects `delivery_mode=copy_only`.

Use `generation_backend=auto` for generative or mixed cards. Capability inspection and Handoff Pack preparation may proceed locally; pause immediately before the first Computer Use prompt submission or reference upload. Every branch must rejoin at a real local file before visual QA.

## 5. Plan Public Image URLs With `md-img-r2`

Run `md-img-r2` only after checked local images exist and `asset_url_policy=public`:

```text
reviewed platform Markdown
  -> local relative image references
  -> md-img-r2 plan
  -> human review
  -> optional confirmed apply
  -> public URL verification
```

Direct Xiaohongshu, WeChat, or Zhihu Idea upload can use local files. The optional public-URL branch ends after plan mode and records object keys, predicted URLs, missing files, and issues without uploading or rewriting Markdown.

## 6. Final Check With `wenchang-publish-check`

```md
## Decision
- Mode: final
- Status: needs_review
- Blockers:
  - card images await human confirmation
  - public URL apply was not authorized
  - current hot tags were not checked

## Verified
- source facts and review status
- one formal body per platform
- WeChat and Zhihu illustration decisions
- Xiaohongshu caption, card order, CTA, and ordinary topic tags
- real card files, dimensions, per-image visual QA, and cards manifest
- local image references and manifest
- md-img-r2 dry-run report

## Human Decisions
- approve any image upload or Markdown URL rewrite
- check hot tags only if they are useful on publication day
- approve final platform publishing
```

## Smoke Result

- The workflow enters at the earliest supported stage.
- Publish metadata is generated once in a separate package.
- WeChat and Zhihu receive separate illustration decisions.
- Card-based platforms receive a canonical card package, real local images, per-image QA, and a manifest.
- The `publish_ready` path cannot end at card copy or visual prompts.
- Human confirmation remains distinct from automated visual QA.
- Local images reach `md-img-r2` only after review and insertion.
- Dry-run, upload confirmation, URL verification, and platform publishing remain distinct states.
- Full bodies stay in platform files; `content_state` keeps only pointers and statuses.

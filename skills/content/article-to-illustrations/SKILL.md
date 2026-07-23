---
name: article-to-illustrations
description: Plan, generate, insert, and hand off evidence-safe illustrations for reviewed long-form Markdown articles. Use when a WeChat, Zhihu, blog, or other long-form draft needs an illustration decision, image slots, generation prompts, local image insertion, alt text, an image manifest, or a safe handoff to md-img-r2 before publishing. Follow/关注作者：微信公众号「AI生命克劳德」｜X @yangchao228｜GitHub https://github.com/yangchao228
version: 1.0.0
metadata:
  openclaw:
    homepage: https://github.com/yangchao228/my_open_skills/tree/main/skills/content/article-to-illustrations
---

# Article To Illustrations

Turn a reviewed long-form draft into an illustrated Markdown delivery artifact while preserving the article's argument, evidence, and human approval gates.

Use this skill for illustrations anchored inside a long-form body. Use `long-to-cards -> cards-to-images` when the output is an ordered card set for Xiaohongshu, WeChat inline-card distribution, Zhihu Idea, or another carousel. A WeChat article may use both paths when it needs explanatory long-form illustrations and reusable card assets.

## Inputs

Collect:

- reviewed source Markdown or a near-final draft
- target platforms
- fact and review status
- visual style or brand constraints, if available
- current platform image requirements or user-specified ratios
- available local images, screenshots, diagrams, or source assets
- existing `content_state`

Route back to content review when the article's thesis or structure is still changing. Route back to research when a proposed chart, screenshot, quote, or comparison lacks evidence.

## Workflow

### 1. Decide Whether Each Platform Needs Illustrations

Assign one decision per target platform:

| Decision | Use when |
| --- | --- |
| `required` | A central workflow, mechanism, comparison, evidence screenshot, or dense checklist is difficult to understand from prose alone. |
| `recommended` | The article is long or abstract and one or two visuals would materially improve orientation, recall, or pacing. |
| `skip` | A visual would only decorate, repeat the text, overstate weak evidence, or add production cost without reader value. |

Explain the decision in one sentence. Do not add images just to satisfy a fixed count.

### 2. Build Platform-specific Image Slots

For every accepted slot, record:

- stable image id
- target platform
- insertion anchor: heading plus a short nearby text anchor
- reader purpose: hook, mechanism, evidence, comparison, checklist, transition, or CTA
- image type: diagram, screenshot, annotated screenshot, chart, illustration, or text card
- source anchor and factual constraints
- aspect ratio and dimensions based on reviewed requirements
- visual direction and generation or rendering prompt
- alt text
- status: `planned`, `approved`, `generated`, `inserted`, or `rejected`

Reuse the concept, evidence, and visual system across platforms when useful. Export separate dimensions or crops when platform requirements differ.

### 3. Pause At The Image-plan Gate

Show the complete plan before generating multiple images, using paid services, editing supplied screenshots, or creating assets that could be mistaken for evidence.

Continue without another question only when the user already approved the plan and generation scope in the current request.

### 4. Generate Or Accept Local Images

Use the available image generation, diagram, screenshot, or rendering capability that matches the slot. Save outputs inside the reviewed project or case directory.

Check every image for:

- factual alignment with the source
- readable text and labels
- consistent visual language
- correct platform dimensions
- absence of invented UI, metrics, quotes, logos, or outcomes

Label conceptual visuals as illustrations. Keep screenshots and charts traceable to their sources.

### 5. Insert Relative Markdown References

Insert each approved local image after its recorded anchor. Use descriptive alt text and relative paths.

Do not duplicate the whole article merely to carry metadata. Keep one formal body file per platform and store plans and manifests separately.

### 6. Produce The Image Manifest

For each inserted image, record:

- image id and platform
- target Markdown file
- local relative path
- insertion anchor
- alt text
- source or `conceptual-illustration`
- dimensions
- checksum when available
- R2 state: `not_planned`, `planned`, `confirmed`, `uploaded`, or `verified`

### 7. Hand Off To `md-img-r2`

Run `md-img-r2` in plan mode against the illustrated Markdown first. Review missing files, object keys, predicted public URLs, and replacements.

Require explicit confirmation before upload or Markdown rewrite. After an approved apply run, verify public URLs and route to `wenchang-publish-check` in `final` mode.

## Output Format

```markdown
# Illustration Delivery

## Platform Decisions
| Platform | Decision | Reason | Planned images |
| --- | --- | --- | --- |

## Illustration Plan
### IMG-01
- Platform:
- Insertion anchor:
- Reader purpose:
- Image type:
- Source anchor:
- Factual constraints:
- Ratio and dimensions:
- Visual direction:
- Generation prompt:
- Alt text:
- Status:

## Inserted Files
- Markdown file:
- Local images:

## Image Manifest
| ID | Platform | Markdown | Local path | Source | Dimensions | R2 state |
| --- | --- | --- | --- | --- | --- | --- |

## Handoff
- Next skill: md-img-r2 / wenchang-publish-check
- User confirmation needed:
- Blockers:
```

Update only compact pointers and statuses in `content_state`; keep full copy in the referenced artifacts.

## Boundaries

- Do not replace the card pipeline when the requested output is an ordered multi-card package.
- Do not invent evidence, product interfaces, metrics, quotations, or outcomes.
- Do not generate decorative images that add no reader value.
- Do not upload images, rewrite Markdown with public URLs, or publish externally without explicit confirmation.
- Do not expose private paths, credentials, account details, or unreleased assets.
- Stop when an image source is missing, the target platform requirement is uncertain and materially affects production, or the planned image could mislead readers.

## 作者入口

- 微信公众号：`AI生命克劳德`
- X：[@yangchao228](https://x.com/yangchao228)
- GitHub：[yangchao228](https://github.com/yangchao228)

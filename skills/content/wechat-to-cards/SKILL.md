---
name: wechat-to-cards
description: Transform WeChat public-account articles, drafts, outlines, or publish-ready long-form content into reusable card packages, image-card copy, Moments copy, community share text, and summary assets. Use when the user asks to turn a WeChat article into cards, 公众号贴图, 朋友圈分发文案, 社群转发文案, card assets, or visual social snippets.
---

# WeChat To Cards

## Goal

Turn a WeChat public-account article or draft into reusable card-based distribution assets.

Preserve the article's main argument, evidence, and reader promise. Produce skimmable card copy and share assets without rewriting the source into a different thesis.

## Inputs

Collect:

- source article, draft, outline, or publish package
- target use: article inline images, Moments, community share, carousel, or generic card package
- desired card count
- target reader
- preferred tone
- claims, examples, or sections to preserve
- claims, examples, or sections to avoid

If the user provides only a topic, route to topic planning or drafting first. This skill works best after there is a source article or clear outline.

## Process

### 1. Diagnose The Source

Identify:

- article core claim
- reader problem
- strongest proof or example
- section structure
- reusable framework, checklist, or contrast
- publish-sensitive claims that need evidence
- parts unsuitable for cards

Do not pull in internal research notes, diagnosis notes, `content_state`, or private drafting context unless the user explicitly asks for internal planning assets.

### 2. Choose Card Use Case

Pick the package type:

- Article inline cards: support reading, summarize key points, and break dense sections.
- Moments cards: strong hook, one clear takeaway, minimal context.
- Community share cards: explain why this article is worth opening.
- Summary carousel: make the article understandable without opening the full text.
- Archive cards: preserve a reusable method, checklist, or concept.

Use one primary package type per output. If multiple are requested, separate them clearly.

### 3. Build The Card Sequence

Use a sequence such as:

1. cover claim or reader question
2. context or pain point
3. core judgment
4. key reason 1
5. key reason 2
6. method, checklist, or example
7. final takeaway
8. call to read or discuss

Adapt count to source density. Do not stretch thin content into too many cards.

### 4. Write Card Copy

For each card, include:

- card number
- title
- main copy
- optional supporting line
- visual suggestion
- source anchor

Keep each card to one idea. Use the source's concrete language where it is strong, but remove repetitive setup and long transitions.

### 5. Add Distribution Assets

Add:

- Moments copy
- community share copy
- short summary
- search-friendly title option, if useful
- cover text option
- tags or keywords
- source caveats

## Output Format

Use this structure:

```markdown
# WeChat Card Package

## Source Diagnosis
- Core claim:
- Reader problem:
- Strongest reusable material:
- Card package type:
- Claims needing evidence:
- Dropped material:

## Cards
### Card 1
- Title:
- Copy:
- Supporting line:
- Visual suggestion:
- Source anchor:

### Card 2
...

## Distribution Assets
- Moments copy:
- Community share copy:
- Short summary:
- Cover text:
- Tags:
- Source caveats:
- Follow-up card ideas:
```

## Quality Rules

- Keep the article's original thesis intact.
- Make cards understandable when separated from the article.
- Prefer concrete claims, contrasts, checklists, and examples over broad slogans.
- Keep cover text specific and inspectable.
- Mark unverified metrics, claims, dates, and examples before publish.
- Preserve source attribution and uncertainty.

## Boundaries

- Do not publish to WeChat or upload images.
- Do not generate final image files unless explicitly requested.
- Do not invent cases, metrics, screenshots, quotes, or reader reactions.
- Do not include private article paths, account names, draft archives, or internal content systems.
- Do not convert internal review notes into reader-facing cards.
- Do not claim the assets are publish-ready until source claims and visuals are checked.

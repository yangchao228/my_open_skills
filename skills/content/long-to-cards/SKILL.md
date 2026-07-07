---
name: long-to-cards
description: Transform long-form content, outlines, transcripts, research notes, or article drafts into reusable card-based social content packages. Use when the user asks to turn a long article into cards, carousel copy, image-card scripts, social card outlines, 小红书图文卡片, 微信图文卡片, or multi-platform card assets.
---

# Long To Cards

## Goal

Convert long-form source material into a clear card-based content package.

Preserve the source argument and evidence. Compress, sequence, and adapt the material for skimmable cards without inventing facts or turning the content into shallow slogans.

## Inputs

Collect:

- source material: article, outline, transcript, notes, or research brief
- target platform: Xiaohongshu, WeChat image cards, LinkedIn carousel, Instagram carousel, or generic cards
- audience
- desired card count
- content goal: explain, persuade, teach, summarize, promote, or archive
- tone and claims to avoid
- whether the user wants only copy or also visual direction

If the source material is missing, ask for it before producing final cards. If the material is too long to process safely, first create a section map and ask which sections to prioritize.

## Process

### 1. Diagnose The Source

Identify:

- central claim
- reader problem
- strongest examples or evidence
- reusable framework or steps
- weak sections to drop
- claims that need verification

Do not preserve every paragraph. Keep the parts that help a reader understand, decide, or act.

### 2. Choose A Card Narrative

Pick one primary structure:

- Problem to method: pain point -> mistake -> method -> example -> takeaway
- Myth to clarity: common belief -> correction -> proof -> practical advice
- Step-by-step: goal -> steps -> pitfalls -> checklist -> next action
- Case breakdown: situation -> decision -> action -> result -> lesson
- Summary: key idea -> 3-7 points -> conclusion -> save/share prompt

Use one structure per card package. Avoid mixing unrelated storylines.

### 3. Build The Card Plan

Create a card sequence:

1. cover hook
2. context or reader pain
3. core idea
4. supporting points or steps
5. example, evidence, or contrast
6. checklist or method
7. conclusion and action

Adjust the sequence to the target platform:

- Xiaohongshu: stronger hook, practical takeaway, save-worthy checklist
- WeChat image cards: clearer logic, fewer claims per card, stronger summary
- LinkedIn carousel: professional framing, concise business or workflow value
- Generic cards: prioritize clarity and reuse

### 4. Write Card Copy

For each card, output:

- card number
- card title
- main copy
- optional microcopy
- visual direction
- source anchor or note

Keep each card focused on one idea. If a card needs more than one paragraph, split it.

### 5. Add Publishing Assets

Add:

- caption or post intro
- hashtags or topic tags
- alt text guidance
- source caveats
- optional follow-up card ideas

## Output Format

Use this structure:

```markdown
# Card Package

## Source Diagnosis
- Core claim:
- Reader problem:
- Best reusable material:
- Dropped material:
- Claims needing verification:

## Card Strategy
- Target platform:
- Audience:
- Card count:
- Narrative structure:
- Hook direction:

## Cards
### Card 1
- Title:
- Copy:
- Microcopy:
- Visual direction:
- Source anchor:

### Card 2
...

## Publishing Assets
- Caption:
- Tags:
- Alt text guidance:
- Source caveats:
- Follow-up ideas:
```

## Quality Rules

- Each card must carry one clear idea.
- The card sequence must be readable without the original long article.
- Keep the cover specific; avoid vague motivation-style hooks.
- Preserve uncertainty and source caveats.
- Convert dense paragraphs into reader-facing steps, contrasts, examples, or checklists.
- Keep visual direction practical: layout, emphasis, icon idea, chart idea, or image type.

## Boundaries

- Do not invent examples, data, quotes, or results absent from the source.
- Do not generate final image files unless the user explicitly asks for image production.
- Do not include private paths, private accounts, or unpublished personal material unless the user supplied it for the current task.
- Do not optimize for a platform in ways that distort the source argument.
- Do not claim the package is ready to publish if source claims still need verification.

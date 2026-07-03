---
name: wenchang-publish-check
description: Final pre-publish content checklist. Use when the user has a near-final draft and needs title, summary, tags, cover copy, image plan, search-friendly title, sharing copy, platform fit, and knowledge asset suggestions.
---

# Wenchang Publish Check

Wenchang Publish Check verifies that a draft has the assets needed for publishing. It is not a rewrite stage.

## Inputs

- near-final draft
- target platform
- existing title, summary, tags, cover text, images, or sharing copy
- existing `content_state`

If the draft has major argument, evidence, or structure problems, route back to `wenchang-review` or `wenchang-research`.

## Checklist

### Long-form Article

- title is clear and not misleading
- search-friendly title states topic and reader gain
- social title can be more emotional but still accurate
- summary explains why to read
- opening 100-300 words show the problem quickly
- tags and keywords match the actual topic
- image plan is complete
- sharing copy sounds natural
- evidence and examples are not detached from claims

### Multi-platform Notes

- WeChat: title, summary, search title, sharing copy, image notes
- Zhihu: question or judgment framing, debate value, personal reasoning
- Xiaohongshu: cover hook, card structure, tags, save-worthy points

## Output Format

```md
## Publish Decision
- Recommendation: publish / publish after fixes / do not publish yet
- Blockers:

## Must Fix
- [ ] ...

## Suggested Improvements
- ...

## Publish Package
- Title:
- Search title:
- Social title:
- Summary:
- Tags:
- Cover copy:
- Image plan:
- Sharing copy:
- Comment prompt:

## Knowledge Asset Suggestion
- Preserve:
- Asset type:
- Suggested bucket:

## content_state Update
```yaml
content_state:
  publish_assets:
    title:
    search_title:
    social_title:
    summary:
    tags: []
    share_copy:
  knowledge_asset:
    should_preserve:
    asset_type:
    suggested_bucket:
  next_step:
    skill:
    reason:
    user_decision_needed:
  handoff:
    from_stage: publish-check
    to_stage:
    accepted_inputs: []
    ignored_context: []
    stop_condition:
```
```

## Boundaries

- Do not publish externally.
- Do not upload images or call external services unless explicitly requested.
- Do not keyword-stuff titles.
- Do not make a draft look ready if there are blockers.

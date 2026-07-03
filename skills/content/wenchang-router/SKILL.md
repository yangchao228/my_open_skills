---
name: wenchang-router
description: Route content creation requests to the right Wenchang skill. Use when the user gives a topic, draft, platform target, publishing task, research need, or asks what content workflow step should happen next.
---

# Wenchang Router

Wenchang Router identifies the current content stage and recommends the next skill. It does not write the final article.

## Stage Routing

| Stage | Signals | Route to |
| --- | --- | --- |
| topic discovery | "what should I write", broad direction, recent trends | platform-specific topic skill or topic brief |
| topic selection | candidate topics, one clear theme, external link | `storm-research` if angle is not settled; otherwise evidence or outline |
| storm research | trend, product, external article, complex question | `storm-research` |
| evidence | claims, data, sources, fact-heavy article | `wenchang-research` |
| drafting | confirmed topic and outline | `wenchang-wechat-writer` or another platform writer |
| review | existing draft | `wenchang-review` |
| publish check | title, summary, tags, distribution, search title | `wenchang-publish-check` |

If the platform is not specified, default to a long-form article path and note that it can later be adapted to other platforms.

## Brief Rules

Routing and topic selection produce a brief, not a full article. A useful brief includes:

- Angle: the core cut in one sentence
- Hook: a first-line candidate
- Subpoints: 3 supporting points
- What to avoid: weak or misleading directions
- Suggested format: platform, length, and shape
- Storm trigger: whether research should run next

## Output Format

```md
## Routing Decision
- Platform:
- Stage:
- Recommended path:
- Reason:

## Brief
- Angle:
- Hook:
- Subpoints:
- What to avoid:
- Suggested format:
- Storm trigger:

## content_state
```yaml
content_state:
  request:
    raw_intent:
    current_stage:
    target_platforms: []
  distribution:
    primary_platform:
    secondary_platforms: []
  next_step:
    skill:
    reason:
    user_decision_needed:
  handoff:
    from_stage:
    to_stage:
    accepted_inputs: []
    ignored_context: []
    stop_condition:
```

## Next Action
- <skill or user decision>
```

## Boundaries

- Do not produce a final draft in the routing stage.
- Do not skip evidence gathering for fact-heavy topics.
- Do not invent platform requirements.
- Do not turn a recommendation into a user decision.

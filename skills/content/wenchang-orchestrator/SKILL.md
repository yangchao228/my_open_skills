---
name: wenchang-orchestrator
description: Wenchang content workflow orchestrator. Use when the user wants to move from a topic, draft, article idea, or publishing need through a structured content workflow: routing, research, evidence gathering, drafting, review, publish checks, and reusable asset capture.
---

# Wenchang Orchestrator

Wenchang Orchestrator turns a content request into an executable workflow. It is a coordinator, not a single writing prompt.

## Core Workflow

```text
trend scan -> topic selection -> storm-research -> evidence gathering -> outline -> draft -> review -> publish check -> knowledge asset suggestion
```

Pick the entry point from the user's actual input. Do not force every request to start at the beginning.

| User input | Entry point | Default path |
| --- | --- | --- |
| Only a broad direction | trend scan | scan -> topic -> storm-research -> evidence -> outline -> draft -> review -> publish check |
| Clear topic but no draft | topic selection | topic -> storm-research -> evidence -> outline -> draft -> review -> publish check |
| External article, product, trend, or claim | storm-research | storm-research -> evidence -> outline -> draft -> review -> publish check |
| Existing draft | review | review -> evidence or edit -> publish check |
| Publish assets only | publish check | publish check -> knowledge asset suggestion |

## Automation Rules

Proceed automatically when the next step is low risk:

- route to the next stage
- produce a topic brief
- produce a storm-research map
- gather evidence and contrarian points
- create an outline
- draft when topic, platform, and angle are clear
- run review and publish checks

Pause for user judgment when:

- multiple viable topics or angles have similar value
- key claims lack primary sources
- research confidence is low
- review recommends rewrite, platform switch, or not investing further
- the next step would produce many images, cards, uploads, or external publishing actions
- the user explicitly asks to stop at decision points

Never perform final publishing, external uploads, deletion, paid distribution, or irreversible account actions without explicit user confirmation.

## State Contract

Every run should output or update `content_state`. Keep it compact. Pass only the fields the next stage needs through `handoff.accepted_inputs`; put rejected or stale context in `handoff.ignored_context`.

```yaml
content_state:
  request:
    raw_intent:
    current_stage:
    target_platforms: []
  topic:
    core_angle:
    selected_title:
    why_now:
    long_term_value:
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

## Output Format

```md
## Current Stage
- Entry:
- Workflow:

## Completed
- <what was completed in this run>

## Needs Your Decision
- <write "none" if the next step can proceed>

## Recommendation
- <next step and why>

## content_state
```yaml
<updated content_state>
```

## Suggested Skill
- <skill name and reason>
```

## Boundaries

- Do not collapse the workflow into one final article.
- Do not treat storm-research as verified fact.
- Do not continue past a blocking decision.
- Do not copy private author identity, private files, account positioning, or local output paths into public deliverables.

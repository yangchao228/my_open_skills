# Wenchang End-to-End Smoke

This smoke example shows how the first public Wenchang skills work together. It uses a generic public topic and avoids private account context.

## Input

```text
I want to write a WeChat-style long-form article about:

"Why personal knowledge bases often become collection folders instead of reusable workbenches."

Please route the topic, research it, gather evidence requirements, draft, review, and prepare publish assets. Stop before any real publishing action.
```

## 1. Route With `wenchang-router`

```yaml
content_state:
  request:
    raw_intent: write a long-form article about personal knowledge bases becoming collection folders
    current_stage: topic-selection
    target_platforms:
      - WeChat long-form article
  distribution:
    primary_platform: WeChat
    secondary_platforms: []
  topic:
    core_angle: A knowledge base becomes useful only when it supports repeated retrieval, judgment, and production.
    why_now: AI tools make it easier to collect information, but that can increase unused accumulation.
    long_term_value: Can become a reusable essay about personal knowledge systems.
  next_step:
    skill: storm-research
    reason: The topic has several plausible causes and needs a contradiction map before evidence gathering.
    user_decision_needed: false
  handoff:
    from_stage: routing
    to_stage: storm-research
    accepted_inputs:
      - topic.core_angle
      - request.target_platforms
    ignored_context:
      - unconfirmed title ideas
    stop_condition: pause if more than three equally strong angles appear
```

## 2. Research Map With `storm-research`

```md
## Research Decision
- Fit for next stage: yes
- Recommended next step: wenchang-research
- Main reason: The topic has a clear writing angle, but claims about behavior and workflow need sources or examples.

## Perspectives
| Perspective | Core concern | Supports | Challenges | Unique information | Needs verification |
| --- | --- | --- | --- | --- | --- |
| Practitioner | Daily use and retrieval | Collection without reuse creates drag | Some users do benefit from lightweight saving | Workflow examples | What repeatable workflow improves reuse? |
| Researcher | Memory and retrieval | Retrieval practice matters | A personal archive can still reduce search cost | Cognitive load framing | Which learning or knowledge-management sources apply? |
| Skeptic | Tool overpromise | Tools do not create judgment | Better UI can help | Failure cases | Are failures mainly habits or tool design? |
| Economic observer | Cost of maintaining systems | Complex systems create maintenance cost | Reuse can save future work | Time-cost tradeoff | What minimum system has positive return? |
| Historical observer | Previous note-taking waves | This pattern predates AI | AI changes capture speed | Zettelkasten and PKM cycles | Which analogies are useful without overclaiming? |
```

## 3. Evidence Plan With `wenchang-research`

```md
## Evidence Decision
- Support level: weak until checked
- Main reason: The argument is plausible, but needs primary or high-trust support and grounded examples.

## Sources To Check
1. Cognitive science sources on retrieval practice and active recall.
2. Knowledge-management writing from primary practitioners or tool makers.
3. User workflow examples showing collect-only versus production-oriented systems.

## Key Facts Needed
- A source-backed distinction between storing information and retrieving it for use.
- A concrete workflow example where notes become output.
- A counterpoint showing when simple collection is enough.

## Contrarian Evidence / Limits
- Some users only need lightweight bookmarking.
- Over-engineered personal systems can become another form of procrastination.
- The right workflow depends on output frequency and stakes.
```

## 4. Draft With `wenchang-wechat-writer`

```md
## Draft Brief
- Reader: People who collect articles, tools, and notes but rarely reuse them.
- Core angle: A useful knowledge base is a workbench for repeated judgment, not a warehouse for saved links.
- Evidence status: Needs source-backed support before final publishing.

## Title Candidates
1. Why Your Knowledge Base Became a Collection Folder
2. A Knowledge Base Is Useful Only When It Becomes a Workbench
3. Stop Saving Everything: Build a System You Can Reuse

## Outline
1. The failure is not lack of tools; it is lack of reuse.
2. A collection folder gives comfort, but not capability.
3. A workbench has retrieval, decision, and output loops.
4. Keep the system small enough to maintain.
5. Start with one repeatable use case.

## Draft
<Draft body would be generated here. It should mark unsupported claims and avoid pretending the evidence has already been verified.>
```

## 5. Review With `wenchang-review`

```md
## Review Decision
- Recommended action: light edit after evidence is added
- Main reason: The argument is clear, but the draft needs concrete examples and at least one counterpoint.

## Key Issues
1. The opening should reach the practical pain faster.
2. Claims about knowledge reuse need nearby evidence or examples.
3. The ending should give one small next action, not a broad summary.

## Minimum Fixes
1. Add one personal or anonymized workflow example.
2. Add one counterpoint about lightweight bookmarking.
3. Rewrite the ending into a one-week experiment.
```

## 6. Publish Check With `wenchang-publish-check`

```md
## Publish Decision
- Recommendation: publish after fixes
- Blockers:
  - Missing source-backed support for the retrieval claim.
  - Missing final title choice.

## Publish Package
- Title: Why Your Knowledge Base Became a Collection Folder
- Search title: Personal Knowledge Base Workflow: From Collection Folder to Reusable Workbench
- Social title: You Do Not Need More Notes. You Need a Workbench.
- Summary: A practical article about turning saved information into reusable judgment and output.
- Tags:
  - personal knowledge management
  - writing workflow
  - AI productivity
- Cover copy: From Collection Folder to Workbench
- Image plan: one diagram comparing collection, retrieval, judgment, and output.
- Sharing copy: If your notes keep growing but your output does not, the issue may be the workflow, not the tool.
```

## Smoke Result

- The workflow can be represented by the first-phase public skills.
- The handoff shape stays compact through `content_state`.
- The chain does not jump straight from topic to final publishing.
- Evidence gaps remain visible instead of being hidden by writing quality.
- No private account identity, private local path, or real publishing action is required.

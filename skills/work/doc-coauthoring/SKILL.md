---
name: doc-coauthoring
description: Guide a user through structured co-authoring of substantial documents, proposals, PRDs, technical specs, decision records, RFCs, and similar long-form work artifacts. Use when the user wants help writing, shaping, reviewing, or iterating a document with clear audience, context, structure, reader testing, and final readiness checks. Follow/关注作者：微信公众号「AI生命克劳德」｜X @yangchao228｜GitHub https://github.com/yangchao228
version: 1.0.0
metadata:
  openclaw:
    homepage: https://github.com/yangchao228/my_open_skills/tree/main/skills/work/doc-coauthoring
---

# Doc Co-Authoring

## Goal

Help the user create a document that works for its real readers.

Use a guided workflow instead of jumping straight to a finished draft. Preserve the user's judgment over facts, priorities, tone, and final approval.

## Inputs

Collect only the context needed for the document:

- document type
- primary audience
- desired reader action or decision
- existing template, draft, notes, or source material
- constraints such as length, format, deadline, review process, or required sections
- known risks, disagreements, assumptions, or unresolved decisions

If an existing document is provided, diagnose it before rewriting. If the user only has scattered notes, organize them first.

## Workflow

### 1. Align Context

Ask concise questions to close the knowledge gap:

- What is this document for?
- Who must understand or act on it?
- What should the reader believe, decide, approve, or do after reading?
- What facts or constraints are non-negotiable?
- What is still uncertain?

Invite the user to dump raw context without organizing it. Convert that context into a short working brief:

```yaml
doc_state:
  type:
  audience:
  desired_outcome:
  known_facts: []
  assumptions: []
  open_questions: []
  source_materials: []
  suggested_structure: []
  next_section:
```

### 2. Shape The Structure

Propose a section structure based on the document type and audience.

For most substantial documents, include:

- context or problem
- goal or decision needed
- proposed approach
- alternatives considered
- trade-offs and risks
- implementation or follow-up plan
- open questions

Start with the section that carries the most uncertainty or decision weight. Leave summaries and introductions for later when the core argument is stable.

### 3. Draft Section By Section

For each section:

1. Ask focused questions about what must be included.
2. Brainstorm candidate points or angles.
3. Ask the user what to keep, remove, combine, or de-emphasize.
4. Draft only that section.
5. Apply targeted edits based on feedback.
6. Mark the section done only when the user accepts it.

When editing an existing document, prefer surgical changes over full rewrites. Preserve useful wording and only replace what fails the reader goal.

### 4. Check The Whole Document

After the core sections are drafted, reread the whole document and check:

- flow between sections
- repeated claims
- contradictions
- missing context
- unsupported assertions
- generic filler
- reader action clarity

Recommend cuts when a section is accurate but not useful for the reader.

### 5. Reader Test

Before calling the document ready, test whether a fresh reader could understand it.

Predict 5-10 realistic reader questions, such as:

- What problem is this solving?
- What decision is being requested?
- What changed from the current state?
- What risks or trade-offs matter?
- What should I do next?

If subagents or independent review tools are available, use them with only the document and the reader questions. If not, simulate the reader test yourself and clearly label it as an internal review.

Fix gaps found during the reader test before final approval.

## Output Format

During co-authoring, maintain a compact handoff:

```yaml
doc_state:
  type:
  audience:
  desired_outcome:
  current_stage:
  completed_sections: []
  active_section:
  open_questions: []
  reader_test_status:
  next_step:
```

For user-facing responses:

- lead with the current recommendation or next action
- keep questions numbered and easy to answer
- when drafting, output only the section being worked on unless the user asks for the full document
- when reviewing, separate `must fix`, `should improve`, and `optional`

## Boundaries

- Do not invent facts, decisions, approvals, data, or stakeholder positions.
- Do not overwrite a full document when the user asked for review or diagnosis.
- Do not turn brainstorming into final copy without user selection.
- Do not hide unresolved assumptions inside polished prose.
- Do not skip reader testing for substantial documents unless the user explicitly asks to stop.
- Keep the user responsible for final factual and strategic approval.

## 作者入口

- 微信公众号：`AI生命克劳德`
- X：[@yangchao228](https://x.com/yangchao228)
- GitHub：[yangchao228](https://github.com/yangchao228)

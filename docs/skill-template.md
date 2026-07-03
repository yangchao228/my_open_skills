# Public Skill Template

Use this structure for new public skills.

## Required Files

```text
skills/<category>/<slug>/
├── SKILL.md
├── skill.json
└── examples/
    ├── minimal-input.md
    └── expected-output-notes.md
```

## SKILL.md Shape

```md
---
name: skill-slug
description: What this skill does and when to use it.
---

# Skill Title

## Goal

## Inputs

## Process

## Output Format

## Boundaries
```

## skill.json Shape

```json
{
  "slug": "skill-slug",
  "title": "Skill Title",
  "category": "content",
  "summary": "One-sentence summary.",
  "keywords": [],
  "user_needs": [],
  "source_dir": "skills/content/skill-slug",
  "entry": "SKILL.md",
  "package_strategy": "on-demand",
  "package_format": "skill",
  "status": "ready"
}
```

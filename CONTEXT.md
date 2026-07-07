# Repository Context

This file defines the language used in this repository.

## Terms

**Skill**

A folder containing a `SKILL.md` file and optional metadata, examples, references, scripts, or assets. A skill gives an agent a repeatable workflow.

**Public skill**

A skill that has been cleaned for public sharing. It contains no private paths, credentials, account details, real content outputs, or private-source-only context.

**Private source skill**

A local or private skill used as reference material. It can inform a public skill, but should not be copied directly into this repository.

**Category**

A top-level workflow group under `skills/`, such as `content`, `work`, `engineering`, or `publishing`.

**Router**

A skill that decides which workflow stage or skill should run next. It produces a compact recommendation and handoff rather than doing all work itself.

**Orchestrator**

A higher-level coordinator that can route across several stages and stop at human decision points.

**content_state**

A compact structured state object passed between content workflow stages. It records request, topic, research, draft, diagnosis, publish assets, next step, and handoff.

**handoff**

The part of `content_state` that states what the next stage may read and what it should ignore.

**Wenchang**

The public name for the content creation workflow in `skills/content/`. It is a set of composable skills for topic routing, research, evidence gathering, drafting, review, publish checks, and knowledge asset suggestions.

**Publishable skill**

A skill that a new user can understand, run with an example, and safely adapt without needing the author's private context.

## Documentation Conventions

Every `README.md` in this repository should have a sibling `README.zh-CN.md` Chinese version in the same directory. When a README changes materially, update its Chinese counterpart in the same change.

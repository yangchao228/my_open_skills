# Publishing Risk Review

Date: 2026-07-08

Scope:

- `md-img-r2`
- `bilibili-video-publisher`
- `superman-blog-publisher`

This review decides what can become a public skill, what must stay private, and what should be rewritten as a safer derivative skill.

## Review Rules

A publishing skill can move into this repository only when it:

- works without private account state;
- uses anonymized examples and placeholder configuration only;
- has an explicit dry-run or review-first path before any external write;
- documents where a human decision is required;
- avoids private local paths, real output archives, real account identity, and live browser session assumptions;
- can be understood by a stranger without access to the original private project.

## Decision Summary

| Candidate | Decision | Public-safe direction | Keep private |
| --- | --- | --- | --- |
| `md-img-r2` | Incubating | A dry-run-first Markdown image publishing helper with placeholder config and no real bucket assumptions | Real service config, direct upload defaults, private domains, local path assumptions |
| `bilibili-video-publisher` | Private source | A metadata package and pre-publish checklist skill that stops before browser automation | Logged-in browser publishing, upload flow, final submit action, account-specific defaults |
| `superman-blog-publisher` | Private source | A generic Markdown blog importer pattern after removing site-specific content model and paths | Personal site workflow, released-archive imports, image upload wiring, deployment coupling |

## `md-img-r2`

Current assessment: possible to publicize after a safety split.

Reusable parts:

- Markdown image discovery and replacement workflow.
- Dry-run report before file mutation.
- Backup-before-write behavior.
- Stable object-key concept based on local files.
- Placeholder configuration template.

Required public rewrite:

- Make dry-run the recommended first action.
- Require explicit user confirmation before external upload.
- Use generic provider language where possible, with R2 as an optional target.
- Replace real service names, domains, prefixes, and local paths with placeholders.
- Document rollback, report files, and missing-image handling.
- Add anonymized examples that do not require live credentials.

Recommended status after rewrite: `draft`, then `ready` only after validation with a fake or mocked upload path.

## `bilibili-video-publisher`

Current assessment: do not publish the automation skill.

Reusable parts:

- Video metadata package format.
- Title, description, tag, dynamic copy, and pinned-comment review rules.
- Final-submit confirmation pattern.
- Failure taxonomy for login, captcha, slow upload, and platform UI drift.

Required public rewrite:

- Create a separate metadata/checklist skill instead of publishing automation.
- Stop at a human-reviewed publish package.
- Do not instruct an agent to operate a logged-in browser session.
- Do not include account defaults, real upload behavior, or platform-specific selector details.

Recommended public derivative: `bilibili-publish-package-check`.

## `superman-blog-publisher`

Current assessment: keep private until rewritten as a generic blog-import skill.

Reusable parts:

- Markdown-to-blog frontmatter normalization.
- Slug, summary, category, tag, and language-pairing decisions.
- Reviewed manifest before batch import.
- Duplicate detection and import report concepts.
- Build and page verification as acceptance checks.

Required public rewrite:

- Remove personal site name, private repo assumptions, and private source archive references.
- Remove direct image-upload coupling or make it a separate optional handoff.
- Replace the fixed content model with a generic frontmatter contract.
- Keep batch import gated by a reviewed manifest.
- Do not include deployment instructions tied to a private project.

Recommended public derivative: `markdown-blog-importer`.

## Recommended Next Steps

1. Start with `md-img-r2` only if it is rewritten around dry-run, placeholder configuration, and explicit confirmation.
2. Keep Bilibili publishing automation private; publicize only a publish-package checker if needed.
3. Keep the personal blog publisher private; extract a generic Markdown importer later.
4. Do not migrate any live publishing script until it passes the public entry rules in [Publishing Policy](publishing-policy.md).

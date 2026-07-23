# Publishing Risk Review

Date: 2026-07-19

Scope:

- `md-img-r2`
- `chatgpt-image-handoff`
- `bilibili-video-publisher`
- `superman-blog-publisher`

This review decides what can become a public skill, what must stay private, and what should be rewritten as a safer derivative skill.

## Review Rules

A publishing-adjacent skill can move into this repository only when it:

- provides an account-independent path or a clean fallback when an optional account session is unavailable;
- uses anonymized examples and placeholder configuration only;
- has an explicit dry-run or review-first path before any external write;
- documents where a human decision is required;
- avoids private local paths, real output archives, real account identity, stored browser state, and fixed live-session assumptions;
- detects optional Computer Use and session capabilities at runtime instead of encoding them in public artifacts;
- can be understood by a stranger without access to the original private project.

## Decision Summary

| Candidate | Decision | Public-safe direction | Keep private |
| --- | --- | --- | --- |
| `md-img-r2` | Ready public derivative | A dry-run-first Markdown image helper with explicit upload and write confirmation | Real service config, direct upload defaults, private domains, local path assumptions |
| `chatgpt-image-handoff` | Ready public workflow | Adaptive backend routing, resumable prompt packs, stable import, and local visual QA with optional Computer Use | Active account state, account identifiers, fixed selectors, conversation ids, local run packs |
| `bilibili-video-publisher` | Private source | A metadata package and pre-publish checklist skill that stops before browser automation | Logged-in browser publishing, upload flow, final submit action, account-specific defaults |
| `superman-blog-publisher` | Private source | A generic Markdown blog importer pattern after removing site-specific content model and paths | Personal site workflow, released-archive imports, image upload wiring, deployment coupling |

## `md-img-r2`

Current assessment: public derivative released in `skills/publishing/md-img-r2`.

Reusable parts:

- Markdown image discovery and replacement workflow.
- Dry-run report before file mutation.
- Backup-before-write behavior.
- Stable object-key concept based on local files.
- Placeholder configuration template.

Public implementation:

- Default execution creates an image-publish plan without upload or Markdown mutation.
- R2 or S3-compatible upload requires `--apply --confirm-upload`.
- Reviewed URL-map replacement requires `--apply --confirm-write` and never contacts object storage.
- The package uses generic placeholder values, stable content-hash object keys, backups, and sanitized reports.
- Missing images, images outside the reviewed project root, incomplete maps, and missing upload configuration block rewriting.
- Anonymous Markdown, HTML image, and reference-style examples exercise the supported paths without live credentials.

Verification: a local fixture passed plan-only inspection, reviewed URL-map rewrite with backup creation, and missing-configuration blocking without external upload.

## `chatgpt-image-handoff`

Current assessment: public workflow released in `skills/content/chatgpt-image-handoff`.

Reusable parts:

- Capability-aware `backend=auto` routing.
- One-job-at-a-time prompt packs and resumable state.
- Manual handoff when Computer Use is unavailable.
- Download detection, stable filenames, checksum and dimension recording.
- Per-image visual QA, contact sheets, overwrite protection, and downstream manifest handoff.

Public implementation:

- Defaults to a generic runtime capability check and does not assume Codex, Computer Use, or an authenticated ChatGPT session.
- Can select Computer Use, built-in ImageGen, manual ChatGPT handoff, or local deterministic and mixed rendering.
- Requests action-time confirmation immediately before a Computer Use prompt submission or reference upload.
- Stores no account identifiers, selectors, coordinates, conversation ids, or active-session details.
- Keeps local `jobs.json`, inbox files, downloads, and generated outputs outside the public skill package.
- Stops at image QA and human confirmation before R2 work or platform publishing.

This workflow is public because its reusable contract is account-independent and its account-bound state remains local. The same rule does not make live platform publishing automation public: publishing represents the user externally and reaches a higher-impact final action.

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

1. Keep `md-img-r2` public as a dry-run-first derivative while actual account configuration and live defaults remain local.
2. Keep `chatgpt-image-handoff` public as an adaptive workflow while active session and run state remain local.
3. Keep Bilibili publishing automation private; publicize only a publish-package checker if needed.
4. Keep the personal blog publisher private; extract a generic Markdown importer later.
5. Do not migrate any live publishing script until it passes the public entry rules in [Publishing Policy](publishing-policy.md).

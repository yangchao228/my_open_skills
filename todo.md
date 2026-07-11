# TODO

## Current Goal

Build `my_open_skills` into a public, categorized AI Agent Skills library, and validate it through a reproducible public case series.

## Phase 1

- [x] Create category directories under `skills/`
- [x] Move `resume-interview-generator` to `skills/work/`
- [x] Add Wenchang content workflow under `skills/content/`
- [x] Add examples for first-phase public skills
- [x] Add root README, context, catalog, policy, and validation docs
- [x] Add list and validation scripts
- [x] Run validation and fix issues
- [x] Add Wenchang end-to-end smoke example
- [x] Enhance validation for catalog links, Markdown links, and unique `source_dir`

## Phase 2

- [x] Publicize `skills/work/project-weekly-report`
- [x] Publicize `skills/work/create-plan`
- [x] Publicize `skills/work/doc-coauthoring`
- [x] Publicize `skills/content/zhihu-topic-hunter`
- [x] Publicize `skills/content/xiaohongshu-topic-generator`
- [x] Publicize `skills/content/long-to-cards`
- [x] Publicize `skills/content/wechat-to-cards`
- [x] Add sibling `README.zh-CN.md` files for every project `README.md`
- [x] Enforce README Chinese counterpart validation
- [x] Review publishing candidates for credential and account-session risk before migration

## Phase 3: Handcrafted Skills Public Series

- [x] Define the Zhihu and Xiaohongshu series position, platform contract, and six-week first season
- [x] Add a reusable public Case Pack template
- [x] Produce the first `xiaohongshu-topic-generator` Case Pack from a public input
- [x] Draft separate Zhihu and Xiaohongshu assets for episode 01
- [x] Add the series and first episode to the root README files
- [x] Render and visually review the first eight 3:4 Xiaohongshu cards
- [x] Choose and add the repository license before describing the library as freely reusable open source
- [x] Unify verified install and trial instructions across ready skills
- [ ] Produce complete public outputs for the first three featured skills
- [ ] Publish episode 01 and record platform plus repository feedback

## Ready Skills

- `skills/work/resume-interview-generator`
- `skills/work/project-weekly-report`
- `skills/work/create-plan`
- `skills/work/doc-coauthoring`
- `skills/content/zhihu-topic-hunter`
- `skills/content/xiaohongshu-topic-generator`
- `skills/content/long-to-cards`
- `skills/content/wechat-to-cards`
- `skills/content/wenchang-orchestrator`
- `skills/content/wenchang-router`
- `skills/content/storm-research`
- `skills/content/wenchang-research`
- `skills/content/wenchang-wechat-writer`
- `skills/content/wenchang-review`
- `skills/content/wenchang-publish-check`

## Candidate Pool

- `skills/publishing/md-img-r2`
- `skills/publishing/bilibili-publish-package-check`
- `skills/publishing/markdown-blog-importer`
- `skills/engineering/playwright`
- `skills/engineering/wechat-miniprogram-ui-acceptance`

## Not Public In Phase 1

- private book or material systems
- private family workflows
- real platform publishing automation
- local output archives
- account-specific or browser-session workflows
- sales and after-sales documents

## Review

- 2026-07-03: Created the public library skeleton, categorized skills under `content`, `work`, `engineering`, and `publishing`, moved `resume-interview-generator` into `skills/work/`, added the first-phase Wenchang content workflow, documented an end-to-end smoke path, enhanced validation for links and unique `source_dir`, and passed `./scripts/validate-skills.sh`.
- 2026-07-03: Publicized `project-weekly-report` as a work skill by rewriting the local workflow into a shareable evidence-first weekly report skill, adding examples, and updating the README, catalog, work index, and candidate pool.
- 2026-07-03: Publicized `create-plan` as a work skill with a read-only planning boundary, concise output template, validation expectations, examples, and catalog updates.
- 2026-07-03: Publicized `doc-coauthoring` as a work skill with context alignment, section-by-section drafting, reader testing, final checks, examples, and catalog updates.
- 2026-07-04: Publicized `zhihu-topic-hunter` as a content skill for theme-bound Zhihu topic hunting, discussion-signal filtering, scoring, drop-list decisions, examples, and catalog updates.
- 2026-07-04: Publicized `xiaohongshu-topic-generator` as a content skill for platform-fit topic generation, hook and card-outline planning, scoring, risk checks, examples, and catalog updates.
- 2026-07-07: Publicized `long-to-cards` as a content skill for converting long-form source material into card-based social packages with source diagnosis, card copy, visual direction, publishing assets, and caveats.
- 2026-07-07: Added sibling `README.zh-CN.md` files for every current `README.md`, linked Chinese versions from the original README files, documented the bilingual README convention, and updated validation to fail when a README lacks a Chinese counterpart.
- 2026-07-08: Publicized `wechat-to-cards` as a content skill for transforming WeChat articles and drafts into card packages, Moments copy, community share copy, summaries, cover text, and source caveats.
- 2026-07-08: Reviewed publishing candidates before migration. `md-img-r2` should be rewritten as a dry-run-first public helper; Bilibili automation stays private with only a publish-package checker candidate; the personal blog publisher stays private until it is extracted into a generic Markdown blog importer.
- 2026-07-10: Started the `我亲手打造的 Skills` public series with a six-week Zhihu and Xiaohongshu plan, a reusable Case Pack contract, a reproducible `xiaohongshu-topic-generator` case, and separate first-episode drafts for both platforms. Kept license selection and unverified one-command installation claims as explicit pre-publish blockers.
- 2026-07-11: Rendered and visually reviewed the first eight 1080×1440 Xiaohongshu cards using the Trace Ledger visual philosophy, then refined spacing and linked the final PNG assets from the episode draft.
- 2026-07-11: Added the MIT license and a repository-level install/trial guide. Root README files and the `resume-interview-generator` README now distinguish documented package commands from the default local Case Pack trial path.

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
- [x] Publicize `skills/publishing/md-img-r2` as a dry-run-first Markdown image publishing helper with explicit upload and write confirmation

## Phase 3: Handcrafted Skills Public Series

- [x] Define the Zhihu and Xiaohongshu series position, platform contract, and six-week first season
- [x] Add a reusable public Case Pack template
- [x] Produce the first `xiaohongshu-topic-generator` Case Pack from a public input
- [x] Draft separate Zhihu and Xiaohongshu assets for episode 01
- [x] Add the series and first episode to the root README files
- [x] Render and visually review the first eight 3:4 Xiaohongshu cards
- [x] Choose and add the repository license before describing the library as freely reusable open source
- [x] Unify verified install and trial instructions across ready skills
- [x] Reframe the public series from individual skill introductions to theme-level case packs
- [x] Diagnose the first theme source article and record its image delivery state
- [x] Recheck source facts and links before drafting theme 01 platform assets
- [x] Draft source-backed Zhihu and Xiaohongshu assets for theme 01
- [x] Draft a WeChat anchor article about multi-platform distribution, the open Skills package, and R2-backed image reuse
- [x] Render and visually review eight Theme 01 Xiaohongshu cards
- [x] Generate an eight-image `md-img-r2` dry-run plan with no external writes
- [x] Apply and verify the reviewed Theme 01 WeChat long-form R2 image plan after explicit confirmation
- [ ] Apply and verify the remaining Theme 01 Zhihu long-form R2 image plan after explicit confirmation
- [ ] Produce source-backed Case Packs for the first three themes
- [ ] Publish theme 01 and record platform plus repository feedback

## Phase 4: Multi-platform Publishing Workflow V2

- [x] Add `article-to-illustrations` for long-form illustration decisions, plans, insertion, and image manifests
- [x] Upgrade `wenchang-publish-check` with `preflight` and `final` modes plus platform-specific publish assets
- [x] Extend Wenchang routing and compact `content_state` for illustration, R2, and publish-gate stages
- [x] Clarify `long-to-cards`, `wechat-to-cards`, writer, and `md-img-r2` responsibilities
- [x] Update the public catalog and bilingual workflow documentation
- [x] Forward-test the V2 workflow against Theme 01 without external uploads or platform publishing
- [x] Run repository validation and record the final review

## Phase 5: Publish-ready Card Image Pipeline

- [x] Add `cards-to-images` as the shared card rendering and visual-QA skill
- [x] Make `long-to-cards` hand off to image production by default in `publish_ready` mode
- [x] Align `wechat-to-cards`, Wenchang routing, publish checks, and compact state with the shared card pipeline
- [x] Document Xiaohongshu, WeChat inline-card, Zhihu Idea, and generic platform profiles
- [x] Forward-test the card pipeline against the existing Theme 01 eight-card package without external writes
- [x] Update bilingual workflow documentation, catalog entries, examples, and the public Case Pack contract
- [x] Run single-skill, repository, JSON, image, link, and diff validation
- [x] Record the final review while leaving R2 upload, platform publishing, commit, and push untouched

## Phase 6: Theme 01 Asset Matrix And Promotion Refresh

- [x] Freeze the truthful Theme 01 asset matrix across WeChat, Zhihu, Zhihu Idea, and Xiaohongshu
- [x] Produce a `wechat-inline` card package, checked local images, and cards manifest
- [x] Produce a Zhihu Idea post, `zhihu-idea` card package, checked local images, and cards manifest
- [x] Rewrite and redraw the eight Theme 01 promotion cards around real outputs and reproducibility
- [x] Update the Case Pack, run report, publish check, compact state, and asset pointers
- [x] Run image, Markdown, JSON, repository, and diff validation without external uploads or publishing

## Phase 7: Theme 01 Generative Visual Preview

- [x] Install and review `baoyu-xhs-images` at project scope
- [x] Define a zero-extra-API-cost three-card preview with saved analysis, outline, and prompts
- [x] Preserve the failed built-in ImageGen run as recoverable history
- [x] Render three screen-print previews locally with exact Chinese typography
- [x] Inspect every preview, fix the failed layout, and write a preview manifest

## Phase 8: Adaptive Public ChatGPT Image Handoff

- [x] Create the project-private `run-chatgpt-image-handoff` Skill
- [x] Implement resumable Handoff Pack generation, download detection, stable import, and contact-sheet scripts
- [x] Define Computer Use confirmation, browser-state, retry, and recovery rules
- [x] Prepare the eight-job Theme 01 ChatGPT image spec and local ignored run pack
- [x] Simulate prepare, scan, state transitions, import, idempotency, overwrite protection, ratio failure, and visual QA
- [x] Generalize the private prototype into public `skills/content/chatgpt-image-handoff`
- [x] Add `backend=auto` capability routing for Computer Use, built-in ImageGen, manual handoff, and deterministic rendering
- [x] Integrate the public handoff with `resilient-imagegen`, `cards-to-images`, and `wenchang-orchestrator`
- [x] Update bilingual indexes, catalog, examples, and publishing-risk boundaries
- [x] Re-run local simulation, single-skill validation, and repository validation
- [x] Migrate the existing Theme 01 local Handoff Pack to adaptive schema v2 and preflight Computer Use
- [x] Confirm the active ChatGPT session in the selected isolated browser
- [x] Run the first live ChatGPT image job after action-time transmission confirmation
- [x] Import and visually review the first real ChatGPT output; leave the remaining seven jobs unsent
- [x] Add fact sensitivity, render strategy, and readable-text policy to the public handoff contract
- [x] Refresh pending Theme 01 prompts without disturbing completed jobs
- [x] Validate strict prompt generation, backward compatibility, and resume safety

## Phase 9: Public Release Candidate

- [x] Freeze WeChat as the anchor article for the first public release
- [x] Freeze R2 scope to four WeChat and Zhihu long-form illustrations
- [x] Keep WeChat inline cards, Xiaohongshu cards, and Zhihu Idea images as local manual uploads
- [x] Exclude local agent installs, image-generation state, caches, experimental previews, and superseded plans
- [x] Update the ready-skill count from 17 to 20 and align the Theme 01 release state
- [x] Scan the public candidate for private absolute paths, credentials, tokens, account state, and symlinks
- [x] Make the Theme 01 renderer discover common fonts and accept explicit font overrides
- [x] Validate the five new skills, Python, JSON, YAML, image dimensions, repository rules, and a clean copied candidate
- [x] Copy `redbook-cards-skill` into the public content skill set with repository metadata and examples
- [ ] Complete human review of the three platform card sets and the final WeChat article
- [x] Apply and verify the two WeChat long-form R2 uploads after explicit confirmation
- [ ] Apply and verify the two remaining Zhihu long-form R2 uploads after explicit confirmation
- [ ] Commit, push, and verify all public article links before platform publication

## Phase 10: ChatGPT Native Image Delivery

- [x] Confirm the authenticated ordinary ChatGPT surface through Computer Use without requiring a named browser profile
- [x] Add deterministic ZIP batch preparation with exact filenames, prompt checksums, and a delivery manifest
- [x] Add safe ZIP import with traversal, symlink, encryption, duplicate-name, and archive-size guards
- [x] Preserve serial generation as the fallback for missing, failed, or revision-only jobs
- [x] Update the public Skill contract, metadata, and UI recovery rules
- [x] Validate a complete four-image synthetic ZIP against a copied Theme 01 handoff
- [x] Test `CARD-05` through `CARD-08` as one real native-only ZIP batch and record the missing-image-edit rejection
- [x] Confirm no valid archive exists, record the optional ZIP limitation, and route the jobs to ordinary Chat
- [x] Generate, import, and complete strict local QA for `CARD-05` through `CARD-08` one image at a time

## Phase 11: ClawHub One-by-One Releases

- [x] Freeze and commit the reviewed public candidate baseline
- [x] Install ClawHub CLI 0.23.1 and verify the authenticated publisher as `yangchao228`
- [x] Add the canonical creator profile and one-at-a-time release ledger
- [x] Add the creator description suffix, `1.0.0`, source homepage, and creator footer to every release-ready skill
- [x] Extend repository validation for creator metadata, semver, homepage, package size, credentials, and ClawHub local state
- [x] Move `redbook-cards-skill` back to incubation because its third-party MIT attribution conflicts with ClawHub MIT-0 packaging
- [x] Pass explicit `1.0.0` ClawHub dry-runs for all 20 release-ready skills from committed source `cbe3c92`
- [x] Verify `create-plan@1.0.0` through inspect, exact-version temporary install, source-file hash comparison, security evidence, creator-link checks, and public-page HTTP 200
- [x] Publish and verify `doc-coauthoring@1.0.0` through the same one-at-a-time release gate
- [x] Verify `project-weekly-report@1.0.0` after publication through explicit category rendering, security evidence, temporary install, hashes, creator links, and the public page
- [ ] Publish every remaining `planned` entry in `config/clawhub-release-plan.json` one at a time; advance only after a verified receipt
- [x] Add a machine-readable release plan for the remaining 16 skills with explicit categories, remote baselines, target versions, tags, and changelogs
- [x] Add a fail-closed single-skill preflight and publish script that requires a clean pushed source commit and an explicit live confirmation
- [x] Add a state-change-only release watcher that verifies public metadata, exact installation, source hashes, security signals, and the generated Skill Card
- [x] Validate the optimized workflow locally and with a real ClawHub dry-run before continuing to the fifth live release
- [x] Add three to five explicit ClawHub Topics to every ready skill while keeping version tags separate
- [x] Pass Topics through dry-run and live publication, then preserve the requested catalog metadata in receipts
- [x] Verify Topics through ClawHub's public skill API and page before finalizing a release
- [x] Record the pilot's submitted state and the `redbook-cards-skill` license block in the release ledger
- [ ] Update the release ledger with verified versions, timestamps, URLs, and any later skill-specific blocks

## Ready Skills

- `skills/work/resume-interview-generator`
- `skills/work/project-weekly-report`
- `skills/work/create-plan`
- `skills/work/doc-coauthoring`
- `skills/content/zhihu-topic-hunter`
- `skills/content/xiaohongshu-topic-generator`
- `skills/content/long-to-cards`
- `skills/content/cards-to-images`
- `skills/content/resilient-imagegen`
- `skills/content/chatgpt-image-handoff`
- `skills/content/wechat-to-cards`
- `skills/content/article-to-illustrations`
- `skills/content/wenchang-orchestrator`
- `skills/content/wenchang-router`
- `skills/content/storm-research`
- `skills/content/wenchang-research`
- `skills/content/wenchang-wechat-writer`
- `skills/content/wenchang-review`
- `skills/content/wenchang-publish-check`
- `skills/publishing/md-img-r2`

## Candidate Pool

- `skills/content/redbook-cards-skill` (incubating; resolve third-party MIT attribution before ClawHub publication)
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

- 2026-07-23: Added ClawHub Topics as first-class release metadata before the fifth live release. Release-plan schema v2 now assigns five ordered, lowercase kebab-case Topics to all 20 ready skills, enforces ClawHub's five-topic and 48-character limits plus reserved-topic rules, keeps version Tags separate, and blocks plan/ledger drift. The runner passes `--topics` in dry-run and live modes and writes a v2 preflight receipt containing the exact Categories, Topics, Tags, changelog, source commit, and ClawHub result. Because CLI 0.23.1 strips Topics from `inspect`, the watcher now checks all five against ClawHub's public skill API and checks the first four rendered by the current page UI. A real read-only regression against the manually updated `doc-coauthoring@1.0.0` passed Categories, all five API Topics, four page Topics, exact installation, hashes, security, and Skill Card; this also caught and corrected the page's four-topic display limit. From pushed source `3c1ee3c`, `storm-research@1.0.0` again returned `would-publish` for four files with fingerprint `ae3fe382...`, now carrying `deep-research`, `source-synthesis`, `citation-workflow`, `contradiction-mapping`, and `research-brief`. No fifth skill was published.

- 2026-07-23: Replaced the repetitive manual ClawHub release loop with a fail-closed, single-skill pipeline. Added a machine-readable plan covering all 20 ready skills (4 verified, 16 planned), explicit categories and discovery tags, remote version baselines, and `md-img-r2` target `1.0.4`. The release runner now requires the first planned slug, a clean pushed `main`, matching publisher identity and remote baseline, a successful dry-run, explicit `--publish --yes`, and an atomic live-publish lock. The state-change-only watcher was proven end to end against the existing `resume-interview-generator@1.0.1`, including public metadata, exact install, source and registry hashes, security, and Skill Card; its finalizer also passed in an isolated repository. From pushed source `176c558`, the real `storm-research@1.0.0` dry-run returned `would-publish` for four files with fingerprint `ae3fe382...` and explicit `research`, `knowledge`, and `productivity` categories. A preoccupied-lock live-flag test stopped before upload as designed. No fifth skill was published.

- 2026-07-23: Published and verified `resume-interview-generator@1.0.1` as the fourth one-at-a-time ClawHub release. The existing public slug belongs to `yangchao228` and already had `1.0.0`, so the repository version and ledger target advanced explicitly to patch version `1.0.1` instead of overwriting history. Selected `productivity`, `knowledge`, and `development` from ClawHub's current public category set; all three rendered on the HTTP 200 public page instead of `Other`, and the seven existing discovery tags now point to `1.0.1`. Repository validation and the 10-file dry-run passed from clean commit `7cecaef` with fingerprint `4db750e5...`. Final `clawhub skill verify` returned `decision: pass`; static scan, VirusTotal, and SkillSpector were clean with recommendation `SAFE`, severity `LOW`, and one non-blocking note. Exact-version installation succeeded, all 10 source files matched the repository and registry SHA-256 values, the downloaded Skill Card matched registry hash `eb65927e...`, and the creator channels, homepage, anonymized fixture, scoring structure, and sensitive-contact-data boundary remained intact. No fifth skill was published.

- 2026-07-23: Completed the categorized `project-weekly-report@1.0.0` release gate. Published from clean commit `3a0b24d` with explicit `productivity`, `knowledge`, and `development` metadata after a four-file dry-run with fingerprint `a67dad09...`; the public page returned HTTP 200 and rendered all three category links instead of `Other`. Final `clawhub skill verify` returned `decision: pass` after ClawHub's asynchronous Skill Card worker completed. Static scan, VirusTotal, and SkillSpector were clean with recommendation `SAFE`, severity `LOW`, and one non-blocking note. Exact-version temporary installation succeeded, all four source files matched the repository and registry SHA-256 values, the downloaded Skill Card matched registry hash `de6184ee...`, and the creator hook, WeChat, X, GitHub, homepage, and evidence-first weekly-report contract remained intact. The first two skills remain queued for the owner's manual category edits, and no fourth skill was published during this gate.

- 2026-07-23: Published and verified `doc-coauthoring@1.0.0` as the second one-at-a-time ClawHub release. The committed four-file source passed repository validation and dry-run with fingerprint `4c586b14...`; ClawHub then completed pre-publication review and exposed the public page. Exact-version temporary installation succeeded, all four source files matched repository and registry SHA-256 values, the public page returned HTTP 200, and the creator description hook, WeChat, X, GitHub, and homepage were present. Initial `clawhub skill verify` failed only with `card.missing` while ClawHub's asynchronous Skill Card worker caught up; after the card was generated, verification returned `decision: pass`. Static scan, VirusTotal, and SkillSpector were clean with recommendation `SAFE`, severity `LOW`, and three non-blocking scope/display notes. No third skill was published during this release gate.

- 2026-07-23: Completed the public `create-plan@1.0.0` pilot gate after ClawHub finished pre-publication review. `clawhub skill verify` returned `decision: pass`; static scan, VirusTotal, and SkillSpector were clean, with recommendation `SAFE`. An exact-version install into an isolated temporary workdir produced the expected four source files plus ClawHub-managed metadata and `skill-card.md`; the four source files matched the committed repository copies byte-for-byte and by registry SHA-256. The installed skill preserved the canonical description hook, WeChat, X, GitHub, and homepage entries. The public ClawHub page returned HTTP 200 and contained all three creator channels. The minimal-input fixture still maps to the required read-only planning contract. No second skill was published during pilot verification.

- 2026-07-23: Implemented the ClawHub one-by-one release foundation. Committed the reviewed 35-file/8-asset baseline as `ee3e8c1`, added and pushed canonical creator metadata, the release ledger, owner-qualified install docs, and stricter release validation as `cbe3c92`, installed ClawHub CLI 0.23.1, and verified publisher `yangchao228`. All 20 releasable skills passed repository validation and explicit `1.0.0` ClawHub dry-runs. Submitted only the `create-plan` pilot; ClawHub accepted the four-file artifact with fingerprint `41976a1c...`, and its registry scan reports clean with engine `v2.4.26`, but the version remains hidden as `pending.publication`. Twenty bounded inspect polls found no state change, and the official pre-publication GitHub Actions worker started no new run during that window, so the required inspect/install gate could not complete and the remaining 19 skills were not uploaded. `redbook-cards-skill` remains blocked from ClawHub because its preserved third-party MIT attribution cannot be represented safely by ClawHub's MIT-0 package license.

- 2026-07-22: Copied `redbook-cards-skill` from the local Claude skills directory into `skills/content/redbook-cards-skill`, preserved the original skill guide, prompt, example, demo HTML, and MIT license, then added repository `skill.json` metadata plus minimal and expected-output examples. Adjusted output-length wording so the public validation keyword scan can pass. Updated the root and content READMEs, catalog, ready-skill list, and this TODO entry. No external upload, platform publication, commit, or push was performed.

- 2026-07-20: Applied the reviewed WeChat long-form R2 plan after explicit user confirmation. Uploaded two 1600×900 PNG files under `my-open-skills/theme-01/longform-v2`, replaced both local references in `wechat-draft.md`, retained an ignored local backup and replacement report, and verified both public `images.reai.group` URLs with `HTTP 200` and `Content-Type: image/png`. Updated the manifest and release state to `wechat=verified`, `zhihu=planned`. No Zhihu R2 upload or platform publication was performed.

- 2026-07-20: Completed the remaining Theme 01 ChatGPT-native cards through ordinary Chat. The confirmed four-image ZIP request first proposed programmatic drawing, then the native-only retry was misclassified as editing missing source images and produced no archive. Documented ZIP delivery as an optional capability rather than a default, removed any requirement for a named Chrome profile or Work mode, and added an explicit batch-failure state before serial fallback. Generated and imported `CARD-05` through `CARD-08` individually. Strict QA caught and corrected unapproved step numbers on `CARD-05` and a rendered meta-instruction on `CARD-08`; `CARD-06` and `CARD-07` passed directly. All eight Theme 01 images now have stable local outputs and passed visual QA; `CARD-02` through `CARD-08` remain pending human confirmation. No valid ZIP import, R2 upload, platform publication, commit, or push was performed.

- 2026-07-20: Submitted the confirmed four-image ZIP batch in a normal authenticated ChatGPT chat. ChatGPT assessed the image tools but explicitly chose local programmatic drawing after the native image generator misclassified the request as an edit. Stopped accepting that route because it violates the user's ChatGPT-native generation requirement, recorded `CARD-05` through `CARD-08` as `failed / native_generator_bypassed`, and prepared a replacement native-only batch. Tightened the public ZIP contract to reject Python, Pillow, SVG, HTML, Canvas, deterministic drawing, screenshots, and placeholders; missing native images must remain resumable. No ZIP, image import, human approval, R2 upload, platform publication, commit, or push was completed.

- 2026-07-20: Prepared the public release candidate without external writes. Added ignore rules for project-local agent installs, image-generation state, caches, the abandoned screen-print preview, the isolated CARD-02 repair plan, and the superseded Xiaohongshu R2 plan. Froze the delivery policy so only four WeChat and Zhihu long-form illustrations enter R2; WeChat inline cards, Xiaohongshu cards, and Zhihu Idea images remain local manual uploads. Updated the series count to 20 ready skills, aligned the Case Pack, manifests, compact state, run report, publish check, and platform drafts, and made the Theme 01 renderer portable through common-font discovery plus explicit overrides. No private absolute paths, credentials, tokens, account state, or symlinks were found in the candidate. Five single-skill checks, Python compilation, JSON, YAML, repository validation, image-dimension inspection, `git diff --check`, and validation from a clean copied candidate passed. R2 apply, Markdown URL rewriting, staging, commit, push, and platform publication remain untouched.

- 2026-07-19: Revised `CARD-02` again after the user preferred the original full-card ChatGPT composition over the text-free-background variant. Human review found that the strong title, archive cabinet, asset counts, real filenames, `MASTER`, `MANIFEST`, `已归档`, and `可追溯 / 可复查` labels were semantically useful and should remain; the actual failure was localized to the bottom `CHECKSUM / SHA256 / BLAKE3` strip and invented values. Preserved the original source checksum `03bd2ae3...` and replaced only that footer with a truthful `TRACE LOG` containing `SOURCE  1 审核母稿 / 4 种发布形态` and `OUTPUT  20 张本地成图 / 4 份 MANIFEST`. The repaired 1080x1440 output was imported under the stable filename with `generation_backend=mixed`; requested strategy remains `generative`, so provenance records the full-card ChatGPT attempt and local repair separately. Updated the public skill to prefer human-reviewed localized repair when failures are isolated, reserving text-free backgrounds for widespread failures. Visual and strict text-policy QA passed; human confirmation remains pending, and `CARD-03`, R2 upload, platform publication, commit, and push remain untouched.

- 2026-07-19: Reopened `CARD-02` after the user rejected the prior mixed output for visual drift. The prior result was correctly moved back to `needs_revision`: its strong blur and near-opaque tint erased ChatGPT's visual contribution and made the card read as deterministic. Submitted a new text-free background request to the original ChatGPT series conversation, downloaded and preserved the distinct `file_000000009dcc...` result with source checksum `2b29ea48...`, and verified that its archive cabinet, paper grain, registration marks, and red-yellow-blue Risograph system continue `CARD-01`. Rebuilt the overlay plan with zero blur and zero global tint, added only the eleven approved strings, imported the final 1080x1440 image under the stable filename with checksum `6855a87d...`, and passed visual plus strict text-policy QA. Updated the public skill contract so `mixed` requires a materially visible generated composition and prefers text-free backgrounds for fact-sensitive cards. Human visual confirmation remains pending; `CARD-03`, R2 upload, platform publication, commit, and push remain untouched.

- 2026-07-19: Solved the recurring `CARD-02` checksum hallucination by converting the job from an explicit generative override to the recommended `mixed` strategy. Added a reusable checksum-locked `render_mixed_overlay.py` renderer that can normalize matching-ratio sources, blur and tint existing readable source text into an unreadable background, reject every text element outside the allowlist, and require the approved strings to appear exactly once. Added the reviewed Theme 01 overlay plan, imported the new 1080×1440 output under the stable filename with `generation_backend=mixed`, and passed visual plus strict text-policy QA while leaving human confirmation pending. The new output checksum is `42c8ac64...`; the old `CHECKSUM`, `SHA256`, and `BLAKE3` footer is gone. Independent forward testing reproduced the same output checksum from the raw 1086×1448 source and correctly rejected both an unapproved `UNAPPROVED` label and a wrong source checksum. Skill quick validation, Python compilation, JSON parsing, repository validation, and `git diff --check` passed. No ChatGPT submission, R2 upload, platform publication, commit, or push was performed.

- 2026-07-19: Inspected the newly visible `CARD-02` result after the user reported completion. The page was on the original conversation branch: it contained only the legacy `CARD-02` prompt and no readable-text policy or forbidden-pattern block. The newly discoverable asset normalized to the exact prior output checksum (`a0c0ebdb...`) and still visibly contained `CHECKSUM`, `SHA256`, and `BLAKE3`. The importer preserved the existing stable output and strict `needs_revision` QA state; no false pass, human approval, or `CARD-03` transmission was recorded.

- 2026-07-19: Retried the `CARD-02` browser preflight after the user attributed the prior stall to networking. The retained in-app tab still resolved to a local `ERR_CONNECTION_CLOSED` error document, and Browser Use blocked navigation from that error-page URL. No workaround was attempted: the strict prompt was not retransmitted, the job remained `failed / timeout_or_stall` at two attempts, the existing imported image stayed untouched, and `CARD-03` remained unsent. The tab was preserved for the user to reopen ChatGPT manually.

- 2026-07-19: Submitted the strict `CARD-02` revision to the existing ChatGPT batch after the user confirmed continuation. The task remained at `正在思考` without producing a new image asset, so the UI recovery policy recorded attempt 2 as `failed` with `timeout_or_stall`; the original imported image and revised prompt were preserved. Stopping the stalled response did not change the page state, and refreshing the conversation then hit the browser URL policy, so no workaround, replacement import, visual-QA pass, human approval, or `CARD-03` transmission was performed. The live conversation was retained for handoff.

- 2026-07-19: Upgraded `chatgpt-image-handoff` to schema v3 after the real `CARD-02` run exposed invented checksum text. Added per-job fact sensitivity, requested/selected/recommended render strategies, readable-text allowlists, forbidden patterns, extra-text rejection, mixed-mode overlay plans, safe pending-prompt refresh, and a required `text_policy_qa` gate before strict images can pass. Migrated the ignored Theme 01 run without changing the two imported image checksums or `CARD-01` approval; recorded `SHA256` and `BLAKE3` as the `CARD-02` failure evidence. Theme 01 keeps an explicit strict-generative retry for `CARD-02`, while high-density pending cards default to mixed rendering. Legacy specs, strict generative prompts, automatic mixed routing, resume preservation, invalid-input rejection, strict-QA rejection/pass paths, single-skill validation, repository validation, Python compilation, JSON checks, and `git diff --check` passed. An independent forward run selected mixed rendering and produced the expected overlay plan. No new ChatGPT prompt, browser action, upload, publication, commit, or push was performed.

- 2026-07-19: Generated and imported `CARD-02` through the Codex in-app browser. The requested title, four asset counts, four Markdown filenames, and `02 / 08` page marker are accurate, but visual QA found invented readable `SHA256` / `BLAKE3` values in the footer. Marked the job `needs_revision`, preserved the output for review, and did not transmit `CARD-03`.

- 2026-07-19: Completed the first live `chatgpt-image-handoff` trial through the Codex in-app browser. `CARD-01` was generated once, downloaded, normalized to 1080×1440, imported under its stable filename, and passed visual QA. Human confirmation remains pending; `CARD-02` through `CARD-08` were not transmitted.

- 2026-07-19: Switched the live `CARD-01` preflight from Chrome to the Codex in-app browser at the user's request. The isolated ChatGPT page loaded and exposed the normal chat composer, but the session is signed out. Recorded `chatgpt_session=login_required` and kept all eight jobs untouched. The ChatGPT tab is being handed to the user for sign-in; no prompt, file, or private browser data was transmitted.
- 2026-07-19: Began the first live `CARD-01` preflight. Verified the queued eight-job pack, exact master prompt, `CARD-01` prompt, empty reference list, and absence of new matching downloads. Migrated the ignored local run state from the legacy manual mode to adaptive schema v2. Computer Use is available, but Chrome remained focused on an actively changing internal work page and twice reported concurrent user changes when an isolated tab was opened, so ChatGPT authentication could not be checked safely. Recorded `chatgpt_session=unknown` and `run_status=awaiting_capability_check`; no prompt was typed or submitted.
- 2026-07-19: Promoted the ChatGPT image workflow into public `chatgpt-image-handoff` with `backend=auto`, runtime capability recording, Computer Use, built-in ImageGen, manual ChatGPT, mixed, and deterministic routes. Ported resumable pack preparation, download detection, stable import, contact-sheet, overwrite protection, visual QA, and human-confirmation state; integrated it with `resilient-imagegen`, `cards-to-images`, and `wenchang-orchestrator`; updated the bilingual indexes, catalog, Theme 01 spec, smoke path, and publishing-risk review. Local simulation verified all four usable backend routes, an incomplete-capability stop, idempotent re-import, ratio failure, explicit replacement protection, confirmation recording, and the visual contact sheet. Single-skill validation, Python compilation, repository validation, JSON checks, and `git diff --check` passed. The project-private predecessor now redirects to the public source of truth. No ChatGPT submission, reference upload, R2 write, platform publication, commit, or push was performed.
- 2026-07-19: Added a project-private, git-ignored `run-chatgpt-image-handoff` Skill that turns ChatGPT browser generation into a resumable job queue. Added deterministic pack preparation, download detection, stable image import, checksum and dimension recording, contact-sheet generation, QA states, overwrite protection, and Computer Use recovery rules. Prepared the real eight-job Theme 01 spec and an ignored local run pack. A local simulation caught and fixed QA reset on idempotent re-import and verified ratio-mismatch routing to `needs_revision`. No ChatGPT prompt submission, reference upload, account action, R2 upload, platform publishing, commit, or push was performed.
- 2026-07-15: Replaced the stalled ImageGen branch with deterministic local Pillow rendering under the same Archive Signal screen-print direction. Generated and inspected three 1080 x 1440 previews plus a contact sheet; QA found and fixed a footer collision on the two-path card before all three images passed. Added a Cards Manifest and deterministic handoff record. No ImageGen, paid API, Figma write, R2 upload, URL rewrite, platform publishing, commit, or push was used.
- 2026-07-15: Resumed the Theme 01 screen-print anchor job after verifying that no delayed image existed. A third built-in ImageGen call again stalled without producing a file. Also checked the installed Figma connector: the authenticated account is on the free Starter tier with a View seat, while the connector exposes no independent image-generation backend and its required design-write guidance was unavailable. Updated the run manifest and kept both paid API fallback and external Figma writes untouched.
- 2026-07-15: Installed `baoyu-xhs-images` only under this project's `.agents/skills`, saved project-scoped no-watermark and built-in-backend preferences, and prepared a three-card Theme 01 screen-print preview with source excerpt, analysis, outline, and one prompt per image. The first anchor image stalled twice in built-in ImageGen and produced no file, so the remaining two jobs were skipped to preserve the required anchor chain. Recorded the recoverable run manifest and did not use CLI/API fallback, third-party paid generation, R2 upload, URL rewriting, or platform publishing.
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
- 2026-07-12: Publicized `md-img-r2` as a safe derivative for Markdown local-image discovery, dry-run planning, reviewed URL-map replacement, and explicitly confirmed R2-compatible uploads. Validated it against a local Markdown fixture without external writes.
- 2026-07-12: Reframed `我亲手打造的 Skills` around theme-level content chains. The first source article, Loop Engineering handbook introduction, passed a read-only image-state check with three existing public URLs and no local upload work; product and version claims remain a fact-check gate before cross-platform drafting.
- 2026-07-14: Confirmed the Theme 01 source facts and public links with the author, then produced separate Zhihu and Xiaohongshu drafts. The public Case Pack now records the confirmed state, source-image boundary, and the two platform assets; image production and external publishing remain human-confirmed steps.
- 2026-07-14: Added the Theme 01 WeChat anchor draft. It promotes the open Skills package through a real multi-platform distribution case and treats `md-img-r2` plus R2-backed public URLs as the reusable image-asset layer; platform-specific uploads and final publishing remain human-confirmed steps.
- 2026-07-14: Ran Theme 01 as a real public case. Produced and visually reviewed eight 1080×1440 Xiaohongshu cards using the Open Weave visual philosophy, kept the Zhihu draft ready for layout, and generated an eight-image `md-img-r2` plan for `images.reai.group` with zero issues and no external writes. R2 upload and platform publishing remain explicit user decisions.
- 2026-07-14: Completed the multi-platform publishing workflow V2. Added `article-to-illustrations`; split `wenchang-publish-check` into preflight and final modes; centralized WeChat, Zhihu, and Xiaohongshu publish metadata; added freshness-aware hot-tag handling; clarified optional card and image-transport branches; and forward-tested Theme 01 through a one-image `md-img-r2` dry-run with zero issues and no external writes. `quick_validate.py`, `./scripts/validate-skills.sh`, JSON validation, and `git diff --check` all passed.
- 2026-07-14: Continued Theme 01 through formal long-form image production. Reused Open Weave as a shared visual master, rendered two 1600×900 WeChat diagrams and two 1080×1440 Zhihu diagrams, inserted all four with relative Markdown paths and ALT text, and produced two `md-img-r2` plans totaling four images with zero issues and no external writes.
- 2026-07-14: Completed the publish-ready card image pipeline. Added `cards-to-images`; made `long-to-cards` default to `publish_ready`; routed Xiaohongshu, WeChat inline cards, Zhihu Idea, and generic carousels through real local image production, per-image QA, a cards manifest, and human confirmation. Forward-testing Theme 01 found and fixed mixed-font missing glyphs on cards 4 and 5, preserved the other six card checksums, refreshed the eight-image R2 plan with zero issues, and passed single-skill validation, JSON checks, image-dimension checks, `./scripts/validate-skills.sh`, and `git diff --check`. No R2 upload, URL rewrite, platform publishing, commit, or push was performed.
- 2026-07-14: Completed the Theme 01 asset-matrix refresh. Added a three-image `wechat-inline` package and a five-image Zhihu Idea package, each with real local PNGs, per-image QA, and a Cards Manifest; rebuilt the eight Xiaohongshu promotion cards around four real release forms, twenty formal images, four manifests, two production branches, conditional R2 handling, and a copyable reproduction prompt. QA caught and fixed connector crossings, a WeChat safe-area overflow, and mixed-font missing glyphs before all sixteen card-branch images passed. Refreshed the Xiaohongshu R2 plan with `planned=8`, `issues=0`, and no external writes. Repository, JSON, YAML, image-count, dimension, and diff validation all passed. External upload, Markdown URL rewrite, article insertion, platform publishing, commit, and push remain untouched.

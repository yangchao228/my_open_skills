# Expected Output Notes

- Return a separate `required`, `recommended`, or `skip` decision for each target platform.
- Tie every image slot to a stable body anchor and reader purpose.
- Record factual constraints, source anchors, dimensions, prompts, and alt text.
- Pause before multi-image generation unless the current request already approves the plan.
- Insert only reviewed local images with relative Markdown paths.
- Produce an image manifest with R2 state and hand off to `md-img-r2` plan mode.
- Keep ordered social-card packages on the separate `long-to-cards -> cards-to-images` path.
- Do not upload, rewrite public URLs, or publish externally.

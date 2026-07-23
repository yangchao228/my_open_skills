# Publishing Skills

[中文版本](README.zh-CN.md)

Risk review: [Publishing Risk Review](../../docs/publishing-risk-review.md)

## Ready

- [md-img-r2](md-img-r2): prepares local Markdown images for public R2 or S3-compatible URLs. It defaults to a dry-run plan; upload and rewriting each require an explicit confirmation gate.

## Remaining candidates

- `bilibili-video-publisher`: private source. Publicize only a metadata package and pre-publish checklist derivative.
- `superman-blog-publisher`: private source. Publicize only a generic Markdown blog importer derivative after removing site-specific assumptions.

Use the publishing layer after `article-to-illustrations` or another reviewed production step has inserted local images into Markdown. Plan first, apply only after confirmation, verify public URLs, and return the report to the final publish check. Keep account-specific configuration and unreviewed external writes outside this repository.

## ClawHub

Publishing helpers are released after lower-risk skills and still preserve their action-time confirmation gates. Check the [release ledger](../../docs/clawhub-releases.md) before installing `@yangchao228/md-img-r2`.

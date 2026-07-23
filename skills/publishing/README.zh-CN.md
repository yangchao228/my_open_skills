# Publishing Skills

[English](README.md)

风险审查：[Publishing Risk Review](../../docs/publishing-risk-review.md)

## 已公开

- [md-img-r2](md-img-r2)：为 Markdown 本地图片准备 R2 或兼容对象存储的公网 URL。默认只生成 dry-run 计划；上传和写回都需要明确确认。

## 其余候选

- `bilibili-video-publisher`：保持私有源。公开版只适合做发布信息包和出刊前检查，不公开真实浏览器发布自动化。
- `superman-blog-publisher`：保持私有源。公开版只适合抽象成通用 Markdown 博客导入器，并移除个人站点假设。

当 `article-to-illustrations` 或其他经过审核的生产步骤把本地图片插入 Markdown 后，再使用发布层生成 dry-run 计划。得到确认后才能写入，完成后验证公网 URL，并把报告交回最终发布检查。账号配置和未经审核的外部写入继续留在仓库外。

## ClawHub

发布辅助 skills 排在低风险 skills 之后发布，并继续保留操作前确认门禁。安装 `@yangchao228/md-img-r2` 前先查看 [发布台账](../../docs/clawhub-releases.md)。

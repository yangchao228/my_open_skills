# My Open Skills

[English](README.md)

这个仓库收集从本地工作流中清理、泛化并沉淀出来的公开 AI Agent Skills。

这个仓库按工作流领域长期维护，承载的是一组公开 skills，并非单个 skill 发布包。

## 为什么有这个仓库

好的 agent 工作依赖可复用流程，而不是一次性 prompt。这个仓库收集反复有用的工作流，包括：

- 从选题到发布检查的内容创作
- 面试准备等结构化工作产出
- 后续工程、发布和验证工作流

每个公开 skill 都应该让新用户能看懂、能安全分享，并能用一个小示例测试。

## 我亲手打造的 Skills 公开系列

这是一个面向知乎和小红书的中文公开构建系列。每一期都从一个公开输入出发，保留实际输出、设计判断、能力边界和复现路径，用真实案例介绍仓库里的 skills。

- [第一季规划](docs/series/handcrafted-skills/series-plan.md)
- [Case Pack 模板](docs/series/handcrafted-skills/case-pack-template.md)
- [主题 01：一篇长文怎样成为跨平台内容资产](docs/series/handcrafted-skills/themes/01-content-asset-pipeline/case-pack.md)
- [第 01 期：小红书选题生成器](docs/series/handcrafted-skills/season-01/01-xiaohongshu-topic-generator/case-pack.md)

## Skill 分类

### Content

第一个公开工作流是 `Wenchang`。它是一套内容创作系统，可以把选题、草稿或外部材料路由到研究、采证、起稿、诊文、平台适配、长文插图、可恢复生图后端、publish-ready 卡片成图和发布检查。

推荐入口：

- [wenchang-orchestrator](skills/content/wenchang-orchestrator) - 完整工作流总控
- [wenchang-router](skills/content/wenchang-router) - 轻量阶段路由

核心内容 skills：

- [zhihu-topic-hunter](skills/content/zhihu-topic-hunter)
- [xiaohongshu-topic-generator](skills/content/xiaohongshu-topic-generator)
- [long-to-cards](skills/content/long-to-cards)
- [redbook-cards-skill](skills/content/redbook-cards-skill)
- [cards-to-images](skills/content/cards-to-images)
- [resilient-imagegen](skills/content/resilient-imagegen)
- [chatgpt-image-handoff](skills/content/chatgpt-image-handoff)
- [wechat-to-cards](skills/content/wechat-to-cards)
- [article-to-illustrations](skills/content/article-to-illustrations)
- [storm-research](skills/content/storm-research)
- [wenchang-research](skills/content/wenchang-research)
- [wenchang-wechat-writer](skills/content/wenchang-wechat-writer)
- [wenchang-review](skills/content/wenchang-review)
- [wenchang-publish-check](skills/content/wenchang-publish-check) - 生成发布预检包并执行最终发布门禁

详见 [skills/content/README.md](skills/content/README.md)。

### Work

可复用的结构化工作产出。

- [resume-interview-generator](skills/work/resume-interview-generator) - 根据简历和岗位生成结构化面试题、追问路径、评分标准和风险验证点。
- [project-weekly-report](skills/work/project-weekly-report) - 基于本地仓库历史、标签、文档和产物生成有证据链的项目周报。
- [create-plan](skills/work/create-plan) - 在代码、文档、仓库或工作流变更前生成简洁实施计划。
- [doc-coauthoring](skills/work/doc-coauthoring) - 引导重要文档完成上下文对齐、分节起草、读者测试和最终检查。

详见 [skills/work/README.md](skills/work/README.md)。

### Engineering

工程工作流 skills 后续发布。详见 [skills/engineering/README.md](skills/engineering/README.md)。

### Publishing

发布和分发辅助 skills 用于把内容资产整理成可公开引用、可跨平台交付的形态。

- [md-img-r2](skills/publishing/md-img-r2) - 扫描 Markdown 本地图片、先生成 dry-run 公网 URL 计划，再在明确确认后写入 R2 或兼容对象存储的替换结果。

详见 [skills/publishing/README.md](skills/publishing/README.md)。

## 安装

仓库级说明见 [安装与试用](docs/install-and-trial.md)。

包安装命令按 skill 分别维护。目前已记录的包命令属于 `resume-interview-generator`：

```bash
npx @skills-hub-ai/cli install resume-interview-generator-2
```

```bash
clawhub install resume-interview-generator
```

本地开发时，克隆本仓库，并把需要的 skill 文件夹链接或复制到你的 agent runtime 使用的 skill 目录中。

没有明确记录包安装命令时，先阅读对应 skill 的 `SKILL.md`、`examples/minimal-input.md` 和 `examples/expected-output-notes.md`。公开系列的 Case Pack 会补充端到端复现路径，但不承诺所有运行环境都支持统一的一键安装。

## 校验

```bash
./scripts/list-skills.sh
./scripts/validate-skills.sh
```

校验会检查 skill 元数据、路径、示例、JSON、README 中文版本和常见私有内容泄漏。

第一个文昌工作流端到端 smoke 记录在 [docs/examples/wenchang-end-to-end-smoke.md](docs/examples/wenchang-end-to-end-smoke.md)。

## 公开边界

本仓公开 skills 不应包含私有文件、本地绝对路径、凭据、真实账号信息、私有内容输出或私有成书/素材系统。

本地工作流只作为经验来源。进入本仓前，公开 skill 必须重写并泛化。

详见 [docs/publishing-policy.md](docs/publishing-policy.md)。

## 许可证

MIT。详见 [LICENSE](LICENSE)。

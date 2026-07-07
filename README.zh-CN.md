# My Open Skills

[English](README.md)

这个仓库收集从本地工作流中清理、泛化并沉淀出来的公开 AI Agent Skills。

这不是一个单独 skill 的发布包，而是一个按工作流领域长期维护的开放技能库。

## 为什么有这个仓库

好的 agent 工作依赖可复用流程，而不是一次性 prompt。这个仓库收集反复有用的工作流，包括：

- 从选题到发布检查的内容创作
- 面试准备等结构化工作产出
- 后续工程、发布和验证工作流

每个公开 skill 都应该让新用户能看懂、能安全分享，并能用一个小示例测试。

## Skill 分类

### Content

第一个公开工作流是 `Wenchang`。它是一套内容创作系统，可以把选题、草稿或外部材料路由到研究、采证、起稿、诊文和发布检查。

推荐入口：

- [wenchang-orchestrator](skills/content/wenchang-orchestrator) - 完整工作流总控
- [wenchang-router](skills/content/wenchang-router) - 轻量阶段路由

核心内容 skills：

- [zhihu-topic-hunter](skills/content/zhihu-topic-hunter)
- [xiaohongshu-topic-generator](skills/content/xiaohongshu-topic-generator)
- [long-to-cards](skills/content/long-to-cards)
- [storm-research](skills/content/storm-research)
- [wenchang-research](skills/content/wenchang-research)
- [wenchang-wechat-writer](skills/content/wenchang-wechat-writer)
- [wenchang-review](skills/content/wenchang-review)
- [wenchang-publish-check](skills/content/wenchang-publish-check)

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

发布和分发辅助 skills 后续发布。详见 [skills/publishing/README.md](skills/publishing/README.md)。

## 安装

当前公开包名按 skill 分别维护。`resume-interview-generator` 现有安装命令保留：

```bash
npx @skills-hub-ai/cli install resume-interview-generator-2
```

```bash
clawhub install resume-interview-generator
```

本地开发时，克隆本仓库，并把需要的 skill 文件夹链接或复制到你的 agent runtime 使用的 skill 目录中。

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

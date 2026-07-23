# Install and Trial

This repository has two supported usage paths.

## 1. Package Install

Use a package command only when a skill documents that exact command.

ClawHub skills are released one at a time under `@yangchao228`. Check the [release ledger](clawhub-releases.md) for verified slugs, then use an owner-qualified command:

```bash
clawhub install @yangchao228/create-plan
```

Current additional package command:

| Skill | Runtime | Command |
| --- | --- | --- |
| `resume-interview-generator` | Codex / Claude Code | `npx @skills-hub-ai/cli install resume-interview-generator-2` |

Do not treat a prepared or blocked ledger row as a verified marketplace release.

## 2. Local Trial

For any ready skill, use this repository-first path:

1. Clone the repository.
2. Open the target skill folder under `skills/<category>/<slug>/`.
3. Read `SKILL.md`.
4. Run or paste `examples/minimal-input.md` in a clean agent context.
5. Compare the result with `examples/expected-output-notes.md`.
6. Record what runtime you used, what input you gave, and where the output differed from the expected contract.

This is the default trial path for content, work, engineering, and publishing skills unless a skill README says otherwise.

## 3. Runtime Copy Or Link

If your agent runtime discovers skills from a local directory, copy or link only the skill folder you want to test.

Example shape:

```text
skills/content/xiaohongshu-topic-generator/
├── SKILL.md
├── skill.json
└── examples/
```

Do not copy private local source folders into this repository or into a public trial bundle.

## 4. Public Case Packs

The public series under `docs/series/` provides reproducible case packs. A case pack is not an installer. It is a frozen example containing:

- public input;
- actual output;
- design decisions;
- boundaries;
- a reproduction path.

Use case packs when you want to understand what a skill should produce before installing it in your own runtime.

---

# 安装与试用

本仓库支持两种使用路径。

## 1. 包安装

只有当某个 skill 明确记录了安装命令时，才使用对应包命令。

ClawHub skills 以 `@yangchao228` 为发布者逐项发布。先查看 [发布台账](clawhub-releases.md) 中已经验证的 slug，再使用带发布者限定的命令：

```bash
clawhub install @yangchao228/create-plan
```

当前额外保留的包安装命令：

| Skill | Runtime | 命令 |
| --- | --- | --- |
| `resume-interview-generator` | Codex / Claude Code | `npx @skills-hub-ai/cli install resume-interview-generator-2` |

不要把台账中的 `prepared` 或 `blocked` 当成已经验证的 marketplace release。

## 2. 本地试用

任何 ready skill 都可以先走仓库优先的试用路径：

1. 克隆本仓库。
2. 打开 `skills/<category>/<slug>/` 下的目标 skill 文件夹。
3. 阅读 `SKILL.md`。
4. 在干净 agent 上下文中运行或粘贴 `examples/minimal-input.md`。
5. 对照 `examples/expected-output-notes.md` 检查结果。
6. 记录运行环境、输入内容，以及输出与预期合同的差异。

除非某个 skill README 单独说明，content、work、engineering 和 publishing skills 默认都按这一路径试用。

## 3. 复制或链接到运行环境

如果你的 agent runtime 会从本地目录发现 skills，只复制或链接你要测试的单个 skill 文件夹。

示例结构：

```text
skills/content/xiaohongshu-topic-generator/
├── SKILL.md
├── skill.json
└── examples/
```

不要把私有本地源目录复制进本仓库，也不要放进公开试用包。

## 4. 公开 Case Packs

`docs/series/` 下的公开系列提供可复现 Case Packs。Case Pack 不是安装器，而是一份冻结示例，包含：

- 公开输入；
- 实际输出；
- 设计判断；
- 能力边界；
- 复现路径。

当你想先理解某个 skill 应该产出什么，再决定是否装进自己的运行环境时，优先看 Case Pack。

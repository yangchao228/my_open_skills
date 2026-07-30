# Loop Builder X/Twitter 发布计划

## 判断

`loop-builder` 适合用一个连续四帖的小型发布序列介绍。核心叙事不是“无限自动化”，
而是如何把模糊任务变成可观察、可停止、可纠错，并保留人工判断权的 Agent Loop。

这份计划作为现有 12 周内容日历的发布建议，不直接修改已经排好的帖子。用户在每个
发布槽位前完成最终事实复核，并决定是否替换原稿。

## 发布门禁

第一帖发布前必须同时满足：

- GitHub `main` 已包含 `skills/engineering/loop-builder`；
- ClawHub 页面可以公开访问并安装 `@yangchao228/loop-builder@1.0.0`；
- 仓库校验、ClawHub exact-version 安装和源文件哈希核对通过；
- 帖子中的链接、命令和版本号在发布当天重新检查；
- 不使用下载量、安装量或“用户成功”等未经验证的效果表述。

## 推荐排期

| 槽位 | UTC 时间 | 角色 | 核心信息 | 建议动作 |
| --- | --- | --- | --- | --- |
| W01-SAT | 2026-08-01 14:00 | Launch / Trial | 发布 `loop-builder` 与五分钟试用入口 | 建议替换原 `create-plan` 试用稿 |
| W02-TUE | 2026-08-04 14:00 | Build Log | 一个 Loop 在第一次迭代前需要哪些合同 | 建议替换原 CI 扩展名稿 |
| W02-THU | 2026-08-06 14:00 | Human3.0 Framework | 四个停止与人工判断机制 | 与原“四个人工门禁”主题合并 |
| W02-SAT | 2026-08-08 14:00 | Case Study | 用 UI 视觉复刻说明反馈与停止规则 | 建议替换原公开/私有边界稿 |

若 ClawHub 在 2026-08-01 前仍未达到公开可安装状态，顺延整组计划，不把
`submitted` 写成“已发布”。

## 英文帖子草案

### 1. Launch / Trial

```text
I built loop-builder for tasks that should improve through feedback—but must still know when to stop.

It turns a rough task into a checked Agent Loop with inputs, feedback signals, stopping rules, and human gates.

Try it:
clawhub install @yangchao228/loop-builder
```

唯一 CTA：安装后回复 runtime、输入和第一个失败步骤。

证据附件：ClawHub 公开页与精确安装命令；如使用终端截图，隐藏本地用户名和绝对
路径并补英文 Alt Text。

### 2. Build Log

```text
Most agent loops fail before iteration begins.

The missing step is not retry logic. It is deciding:
• what evidence is required
• what can change
• how improvement is measured
• when the loop must stop

loop-builder makes that contract explicit.
```

唯一 CTA：询问读者最常缺失的是哪一项。

证据附件：公开 `SKILL.md` 中 Context Gate、反馈信号和停止规则的短截图。

### 3. Human3.0 Framework

```text
An Agent Loop should not mean “run forever.”

My default design has four brakes:
1. logic confirmation
2. max iterations
3. no-improvement breaker
4. human approval for risky actions

Automation prepares evidence. A person keeps the final judgment.
```

唯一 CTA：询问哪个动作必须由人批准。

证据附件：一张四门禁简图；只使用本 skill 的公开规则，不制作虚构运行数据。

### 4. UI Visual-Match Case

```text
Example: UI visual matching.

target → implement → screenshot → list differences → fix the top 3 → screenshot again

No target image? Stop.
No measurable improvement? Stop.
Publish or overwrite? Ask.

That is the kind of loop-builder workflow I want tested.
```

唯一 CTA：邀请读者提供一个可公开的 UI 复刻样本或第一个失败点。

证据附件：`examples/generate-ui-visual-match-loop.md` 的公开流程片段；不要暗示
skill 已经亲自修改或发布页面。

## 发布后互动

- 第一帖发布后 24 小时内，只做针对安装、运行环境和输入合同的具体回复。
- 在 Agent Loop、Agent Harness、human-in-the-loop 和 evaluation 相关讨论中，
  选择五条真正相关的帖子回复，不群发同一链接。
- 只有仓库内容确实回答对方问题时才带 GitHub 或 ClawHub 链接。
- 将“表达兴趣”“开始安装”“独立完成”和“提出具体失败”分别记录。

## 七天判断门

发布满七天后，按真实数据做一次判断：

| 信号 | 目标 | 下一步 |
| --- | ---: | --- |
| 外部试用尝试 | 至少 3 次 | 不足时先检查安装和首个输入是否过重 |
| 独立完成 | 至少 1 次 | 没有完成时观察第一个失败步骤 |
| 有效问题或失败报告 | 至少 2 条 | 把共性问题转成 issue 或最小修订 |
| 可执行改进项 | 最多选择 1 项 | 只改影响试用转化最大的阻塞点 |

这些是实验目标，不是发布时可以宣称的结果。没有达到目标时保留真实结论，不补写
用户案例或效果数据。

## 需要回填

用户人工发布后，把实际 URL、UTC 时间和 36 小时后的数据回填到：

- `docs/social/x/editorial-calendar.md`
- `docs/social/x/metrics.csv`
- `docs/social/x/operations-status.md`

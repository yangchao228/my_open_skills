# 用 loop-builder 生成 UI 视觉复刻专用 Skill

这个示例说明：`ui-visual-match-loop` 不是凭空手写的普通 skill，而是由 `loop-builder` 根据一个高频真实任务生成的专用 Loop Skill。

## 用户原始需求

```md
我用 Codex 复刻指定 UI 视觉稿，经常来回改很多轮还是不像。

我希望把这个过程做成一个 Loop：
目标图 -> 实现 UI -> 截图 -> 对比差异 -> 继续修 -> 达标或停止。

请使用 loop-builder，帮我判断这个任务是否适合做成专用 Loop Skill。
如果适合，请生成一个可以全局安装的 Skill，名字叫 ui-visual-match-loop。
```

## loop-builder 的适配判断

- 结论：适合生成专用 Loop Skill。
- 主模式：Plan-Execute-Verify。
- 辅助模式：Retry Loop、Human-in-the-Loop。
- 原因：
  - 有明确目标视觉稿。
  - 有当前页面截图作为反馈信号。
  - Maker 可以逐轮修正差异。
  - Screenshot Checker 可以生成验收截图。
  - Visual Evaluator 可以输出 Top 差异。
  - Evaluator 可以判断继续、停止或等待人工确认。

## 为什么这是完整 Loop

```text
目标视觉稿
-> Planner 拆解视觉目标
-> Maker 实现或修正 UI
-> Screenshot Checker 截图
-> Visual Evaluator 对比差异
-> Evaluator 判断继续 / 停止 / 人工确认
-> 下一轮 Maker 只修 Top 3 差异
```

它和一次性 Prompt 的区别：

- 一次性 Prompt 只能“按图写一版”。
- Visual Match Loop 每轮都有截图反馈。
- 每轮差异有优先级。
- 有最大轮次、越界动作和人工确认节点。

## 生成前必须先输出协议

不要直接生成专用 Skill。`loop-builder` 必须先输出：

1. 场景工作流分析。
2. Skill 协议草案。

其中 UI 视觉复刻的协议草案要明确：

- 角色是高级前端还原工程师，不是自由发挥的设计师。
- 第一阶段只读分析设计稿，不写代码。
- 必须拆页面结构、组件树、颜色变量、字体、间距、圆角、阴影、图片和图标资产。
- 实现按 layout / header / hero / card-list-form / responsive 分阶段推进。
- 每阶段运行页面并截图。
- 每轮只修 Top 3 视觉差异。
- 不确定 CSS 值必须标注。
- 不自动改业务逻辑、不自动提交、不自动发布。

用户确认协议后，`loop-builder` 才生成：

```text
content/ui-visual-match-loop/
  SKILL.md
  skill.json
```

其中：

- `SKILL.md` 定义 UI 视觉复刻闭环流程。
- `skill.json` 定义 Codex 可识别的 skill 元数据。

## 专用 Skill 的用户入口

安装后，在任意前端项目中可以这样用：

```md
请使用 ui-visual-match-loop，帮我按目标视觉稿复刻当前页面。

目标图：
<图片路径>

当前页面：
<本地 URL、路由或启动命令>

技术栈：
<React/Vue/Next/Vite/其他>

viewport：
<例如 1440x900>

禁止动作：
不改业务逻辑，不引入新 UI 库，不自动提交，不自动发布。
```

## 安装方式

从本仓库安装到 Codex 全局 skill 目录：

```bash
cp -R content/ui-visual-match-loop ~/.codex/skills/
```

如果也要在其他项目里继续用 `loop-builder` 生成新专用 Skill：

```bash
cp -R content/loop-builder ~/.codex/skills/
```

## 反哺边界

`ui-visual-match-loop` 可以记录 UI 复刻过程中的有效规则，例如：

- 每轮只修 Top 3 差异。
- 截图必须非空且无遮挡。
- 剩余差异进入主观审美区时交给用户。

但这些规则不能自动回写 `loop-builder`。只有用户确认它们具有通用价值，才进入 `loop-builder` 的 Skill 维护流程。

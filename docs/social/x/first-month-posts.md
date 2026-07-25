# X 首月英文发布文案

代码块内是准备发布到 X 的英文文案，并按标准 280 字符帖子设计。代码块外的
标题、证据说明和操作要求使用中文，不要复制到 X。最终事实复核、附件选择、
发布和回复仍由用户人工完成。

## 五帖置顶 Thread

### Pin 1 — 我是谁

```text
I’m Sundy Yang, an AI builder and open-source practitioner.

I turn workflows I actually use into small, inspectable systems—then publish the parts other builders can reproduce.

This thread explains what I’m building, why Human3.0 matters, and where to start.
```

### Pin 2 — Human3.0 是什么

```text
Human3.0 is my working thesis for the AI era:

Define the system.
Keep judgment visible.
Turn repeated work into durable assets.

The goal is not maximum automation. It is more agency, clearer boundaries, and systems a person can still inspect and change.
```

### Pin 3 — 我构建了什么

```text
My current proof: 20 verified Agent Skills and Wenchang—an open content workflow built from composable Agent Skills.

Each verified release has a public page, exact-version install, source-hash checks, security evidence, and a generated Skill Card.
```

### Pin 4 — 五分钟试用

```text
Try one in five minutes:

clawhub install @yangchao228/create-plan

Give it one messy task. Check whether the plan respects scope, evidence, and decisions that should remain human.

Source and examples:
https://github.com/yangchao228/my_open_skills
```

### Pin 5 — 反馈要求

```text
If you try it, tell me:

1. your runtime
2. the input you used
3. the first step that failed
4. what you expected instead

Try one skill and tell me where it breaks. That evidence will shape what I improve next.
```

Thread 发布前检查：

- 确认 `config/clawhub-release-plan.json` 仍有 20 条 `verified`。
- 在未登录浏览器中打开仓库和 ClawHub 试用链接。
- 按顺序把 1–5 发布为同一个 Thread。
- 五帖和链接全部可见后，再置顶第 1 帖。

## 第一周：定位和证明

### W01-TUE — Verified 代表一条证据链

```text
I open-sourced 20 Agent Skills and verified every release.

“Verified” means the public page, exact-version install, source hashes, security checks, and Skill Card all passed.

The useful part is the evidence chain, not the count.
https://github.com/yangchao228/my_open_skills
```

证据附件：

- 截取显示 `20 verified` 的 release plan 终端输出；
- 截图中不能出现私有路径、Token 或本地账号状态。

回复问题：

> What would you require before trusting a community Agent Skill?

### W01-THU — Human3.0 主张

```text
Most AI advice begins with better prompts. I think the bigger shift is learning to define the system around the model.

Human3.0 means preserving judgment while turning repeatable work into durable assets.

What part of your workflow should remain yours to decide?
```

证据附件：

- 不配图，保持为纯观点帖；
- 如果有人询问 `durable assets`，在回复中给出一个真实工作流案例。

### W01-SAT — 五分钟试用

```text
Want to test an open Agent Skill in five minutes?

Run:
clawhub install @yangchao228/create-plan

Give it one messy task. Check scope, evidence, and human decisions.

If it fails, send me the first failing step.
https://clawhub.ai/yangchao228/skills/create-plan
```

证据附件：

- 一张包含安装命令和示例输入的终端截图；
- 发布前在干净临时环境中重新执行一次安装。

## 第二周：工程可信度

### W02-TUE — 不支持的文件扩展名

```text
One file named config.example kept breaking my GitHub Action.

The registry omitted that unsupported extension. My verifier compared whole directories, so it reported false drift.

Fix: trust the registry manifest, verify declared hashes, and reject undeclared files.
```

证据附件：

- 使用 commit `3a86437` 的小范围 diff；
- 同时展示失败日志和通过的回归测试，并保留公开仓库路径。

### W02-THU — 四个人工门禁

```text
I use four human gates in AI workflows:

1. scope approval
2. external-write approval
3. factual review
4. final publication

Automation can prepare evidence for each gate. It should not quietly cross them.

Where does your agent need a stop button?
```

证据附件：

- 使用现有 human-gate 卡片：
  `docs/series/handcrafted-skills/themes/01-content-asset-pipeline/assets/07-human-gate.png`;
- 人工上传时补充英文 ALT。

### W02-SAT — 公开与私有边界

```text
My open-source test:

Share the reusable method, fixtures, and failure boundaries.

Keep credentials, account sessions, private source material, and irreversible publishing controls private.

Risk defines the boundary—not how easy a file is to copy.
```

证据附件：

- 截取 `docs/publishing-policy.md` 的公开边界部分；
- 不使用任何私有文件名作为示例。

## 第三周：产品和工作流

### W03-TUE — 一个来源，四种资产

```text
One long-form article became four reusable assets:

• newsletter article
• long-form essay
• carousel
• visual post

The key was one reviewed source plus platform-specific delivery contracts.

Every output kept a manifest.
```

证据附件：

- `docs/series/handcrafted-skills/themes/01-content-asset-pipeline/assets/01-cover.png`
  或本地 contact sheet；
- 对外只使用帖子中的全球化内容形态名称，不直接解释中文平台规则。

### W03-THU — Skill 不只是 instructions

```text
A good Agent Skill needs more than instructions.

It needs:
• a clear trigger
• explicit inputs
• an output contract
• examples
• failure boundaries
• verification

A prompt can produce an answer. A skill should produce a repeatable result.
```

证据附件：

- 一张显示 `SKILL.md`、`skill.json` 和 `examples/` 的小型仓库树；
- 使用一个真实公开 Skill，不制作虚构结构图。

### W03-SAT — 文昌内部结构

```text
Wenchang is an open content workflow built from composable Agent Skills.

Research, drafting, review, adaptation, images, and publish checks stay separate and inspectable.

Small skills make failures easier to locate—and human decisions easier to preserve.
```

证据附件：

- 从下面文档整理一张简单英文工作流图：
  `docs/examples/wenchang-end-to-end-smoke.md`;
- 不暗示平台发布已经自动化。

## 第四周：透明复盘

### W04-TUE — 数字能证明什么

```text
Current ClawHub snapshot: 2,206 downloads, 39 installs, 1 star.

That shows distribution activity. It does not prove user success, retention, or value.

The metric I care about next: can someone complete a trial without my help?
```

发布前检查：

- 使用当天 ClawHub API 结果替换三个数字；
- 即使数字上涨，也保留原有局限说明；
- 没有有效分母和解释时，不增加百分比。

### W04-THU — Release cycle 经验

```text
Publishing 20 Agent Skills taught me this:

The upload is the easy part.

The real work is metadata, source identity, install verification, security evidence, async states, and recovery when the platform behaves differently from your machine.
```

证据附件：

- 一张包含状态流转的 release ledger 截图；
- ALT 中使用真实 verifier 或 reconciler 文件名。

### W04-SAT — 根据反馈决定下一步

```text
I have 20 verified Agent Skills. The next release should be driven by use, not inventory.

Try one and tell me:
1. where you got stuck
2. what you expected
3. what evidence would make you trust it

I’ll build the next iteration from real trial feedback.
```

证据附件：

- 不使用发布宣传图；
- 如果主帖字符不足，在第一条回复中补充仓库链接。

## 试用反馈记录

每一次真实试用对话都记录：

- X 帖子 URL；
- 只有对方已经公开互动时，才记录参与者 Handle；
- Runtime；
- Skill slug；
- 试用状态：`attempted`、`completed_with_help` 或
  `independent_completion`;
- 首个失败步骤；
- 预期行为；
- 引用反馈或制作案例前的授权状态。

不能把 Like、Download、Install 或模糊的正面回复记录为已完成试用。

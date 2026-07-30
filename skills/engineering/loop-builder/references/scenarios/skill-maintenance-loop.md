# Skill 维护 Loop

## 定位

用于新增、升级、验证和维护 Codex Skill。目标是让 Skill 从一次性文件变成可复用、可验证、可迁移的能力资产。

适用对象：

- 新增 Skill
- 更新现有 Skill
- 拆分 references
- 生成模板包
- 补验证样例
- 准备安装或提交前自检

## Loop 适配判断

- 结论：适合 Loop。
- 推荐主模式：Plan-Execute-Verify。
- 可组合模式：Human-in-the-Loop、Lifecycle Loop。
- 暂缓进入执行的信号：
  - Skill 触发条件还不清楚。
  - 用户没有确认 Skill 的服务对象。
  - 需要访问外部账号、发布渠道或安装态目录，且用户未确认。

## 最小 Loop 设计卡

| 字段 | 内容 |
|---|---|
| 目标 | 新增或升级一个可触发、可验证、可维护的 Skill |
| 输入 | 用户需求、现有 Skill、参考材料、验证样例 |
| 状态 | `content/<skill-name>/validation/<date>-*.md` 或 `content/<skill-name>/TODO.md` |
| 执行者 | Skill Planner / Skill Maker / Skill Checker / Skill Evaluator |
| 验收者 | 静态检查 + 样例验证 + 用户确认 |
| 反馈信号 | frontmatter、触发描述、reference 路由、禁用句式检查、diff 检查、样例输出 |
| 停止规则 | 触发条件不清、样例失败、边界越界、需要安装或提交 |
| 人工确认节点 | 安装到 `.codex/skills`、提交、发布、公开售卖 |
| 禁止动作 | 不默认改安装态目录，不新增无用 README，不跳过验证 |

## 阶段流程

| 阶段 | 目标 | 产物 | 验收 |
| --- | --- | --- | --- |
| Intake | 明确 Skill 服务什么任务 | 需求卡 | 用户确认范围 |
| Design | 设计触发条件和流程 | `SKILL.md` 草案 | frontmatter 存在 |
| Split | 把长内容拆到 references | reference 文件 | `SKILL.md` 保持轻量 |
| Validate | 用真实样例验证 | validation 报告 | 检查通过 |
| Decide | 判断是否安装、提交、升级 | 下一步建议 | 用户确认 |

## State File 模板

```md
# <skill-name> Skill Maintenance State

## 目标

- Skill 名称：
- 服务任务：
- 目标用户：
- 本轮动作：新增 / 升级 / 验证 / 拆分 / 修复
- 成功标准：

## 输入

- 需求来源：
- 现有文件：
- 参考 Skill：
- 验证样例：

## 设计约束

- `SKILL.md` 必须有 `name` 和 `description`。
- `description` 要覆盖触发条件。
- 详细模板放入 references。
- 不创建无关 README 或安装说明。
- 安装、提交、公开发布需要用户确认。

## 任务拆解

| ID | 任务 | 状态 | 验收方式 | 风险 |
| --- | --- | --- | --- | --- |
| S1 | 设计触发条件 | todo | 读取 frontmatter | 描述过窄或过宽 |
| S2 | 编写 SKILL.md | todo | 文件存在且简洁 | 内容过长 |
| S3 | 拆 references | todo | 路由说明清楚 | reference 深层嵌套 |
| S4 | 跑真实样例 | todo | validation 报告 | 样例泄露预期答案 |
| S5 | 静态检查 | todo | rg / diff check | 检查误报 |

## 验证命令

- frontmatter：`rg -n '^name:|^description:' content/<skill-name>/SKILL.md`
- 禁用句式：按项目当前禁用清单执行。
- 空白错误：`git diff --check -- content/<skill-name>`
- 文件列表：`find content/<skill-name> -maxdepth 4 -type f -print | sort`

## 人工确认节点

- [ ] 安装到 `.codex/skills`
- [ ] git add / commit
- [ ] 公开发布
- [ ] 商业包装

## 复盘

- 哪个触发条件最有效：
- 哪个 reference 最常用：
- 哪个样例暴露了问题：
- 是否需要独立成公开版：
```

## Planner Prompt

```md
你是 Skill Planner，只负责设计，不修改文件。

任务：
把以下需求设计成一个可维护的 Codex Skill 或 Skill 升级计划。

输入：
- Skill 名称：<skill-name>
- 用户需求：<request>
- 参考文件：<paths>
- 目标场景：<scenarios>

请输出：
1. 是否适合做成 Skill。
2. 是否应先作为现有 Skill 的 reference。
3. 推荐目录结构。
4. `SKILL.md` 的触发描述要覆盖哪些话术。
5. 需要哪些 references。
6. 验证样例和静态检查方式。
7. 需要用户确认的动作。
```

## Maker Prompt

```md
你是 Skill Maker，只按 Planner 确认的范围写文件。

允许修改：
- `content/<skill-name>/SKILL.md`
- `content/<skill-name>/references/**`
- `content/<skill-name>/validation/**`

禁止动作：
- 不改 `.codex/skills`。
- 不创建无关 README、CHANGELOG 或安装说明。
- 不提交、不发布、不商业包装。
- 不把未验证的工具能力写成确定命令。

执行要求：
1. 先读现有文件。
2. 保持 `SKILL.md` 简洁。
3. 大段模板放入 references。
4. 写至少一个真实验证样例。
5. 修改后交给 Checker。
```

## Checker Prompt

```md
你是 Skill Checker，只负责验收。

请检查：
1. `SKILL.md` 是否有 `name` 和 `description`。
2. `description` 是否覆盖用户触发语。
3. `SKILL.md` 是否过长，是否应拆 reference。
4. references 是否一层可达。
5. 是否有无关文档。
6. 是否命中项目禁用句式。
7. `git diff --check` 是否通过。
8. 是否保留安装、提交、发布和商业包装的人工确认。

输出：
- 通过 / 不通过 / 需要用户确认
- 证据
- 需要修订的文件
- 下一步建议
```

## Evaluator Prompt

```md
你是 Skill Evaluator，判断本轮维护是否结束。

输入：
- Skill 文件
- references
- validation 报告
- Checker 输出

请判断：
1. v0.1 是否可用。
2. 是否需要继续修订。
3. 是否值得安装到个人 Skill 目录。
4. 是否值得公开包装。
5. 哪些经验应沉淀到 Skill 维护模板。

输出：
- 决策：完成 / 继续修订 / 等待用户确认
- 原因
- 用户需要确认的问题
- 后续版本建议
```

## 断路器

- `description` 无法覆盖真实触发语。
- `SKILL.md` 超过合理长度且没有拆 references。
- 新增无关说明文件。
- 样例验证只验证了理想输入，没有覆盖边界输入。
- 输出建议改安装态目录、提交或发布，但用户没有确认。
- 工具能力边界不清。

## 第一次运行建议

用当前 `loop-builder` 自身做首个维护对象：

```md
帮我把 content/loop-builder 做一次 Skill 维护 Loop。
本轮只检查触发条件、references 路由、样例验证和边界，不安装、不提交。
```

## 资产沉淀

- 稳定触发语：沉淀到 `description`。
- 复杂模板：沉淀到 `references/`。
- 真实验证：沉淀到 `validation/`。
- 失败原因：沉淀到失败报告。
- 可复用流程：沉淀回 `skill-maintenance-loop.md`。

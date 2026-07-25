# Sundy Yang X 个人品牌规范

## 定位

**公开承诺：** Sundy Yang 构建开放的 AI 系统，同时保留人的判断权，并把
有效工作流沉淀为可复用资产。

**简短定位：** `AI Builder for Human3.0`

**目标受众：** 全球 AI builders、agent developers、indie hackers 和
open-source contributors，尤其是关注可复现系统的人。

**90 天核心目标：** 获得外部试用、独立复现、具体问题和可执行产品反馈。

粉丝量、曝光量、下载量和安装量只是辅助分发信号，不能代替独立复现。

## 品牌层级

| 层级 | 公开角色 | 使用位置 |
| --- | --- | --- |
| Sundy Yang | 对构建结果负责的个人 | Display name、回复、构建判断和复盘 |
| AI Builder × Human3.0 | 长期主张 | 系统设计与人的判断权之间的关系 |
| Wenchang | 产品和工作流 | 由可组合 Agent Skills 构成的开放内容工作流 |
| `my_open_skills` | 公开证据库 | 源码、示例、验证、Case Packs 和 Issues |
| 20 verified Agent Skills | 带日期的证明信息 | 只有完成实时复核并解释验证口径后才使用 |
| AI生命克劳德 | 中文内容品牌 | 不进入 X 主显示名称和日常英文内容 |

`Human3.0` 的固定解释是：人在 AI 时代保留判断权，同时把重复工作沉淀为
系统和长期数字资产。在一次对话中首次出现时，用一句话解释，不默认海外读者
已经理解。

## Profile 固定口径

| 字段 | 批准内容 |
| --- | --- |
| Display name | `Sundy Yang | AI Builder` |
| Handle | `@yangchao228` |
| Avatar | 保留当前人物头像 |
| Website | `https://github.com/yangchao228/my_open_skills` |
| Header | 使用 [`ChatGPT 完整提示词`](assets/header/chatgpt-header-prompt.md)生成并人工审核升级候选图；[`x-header-1500x500.png`](assets/header/x-header-1500x500.png)保留为确定性兜底 |
| Bio | `AI builder turning real workflows into open systems. Building Wenchang & 20 verified Agent Skills. Exploring Human3.0 and cognitive sovereignty.` |

Bio 共 144 个字符，低于 X 官方记录的 160 字符上限。X 推荐 Header 使用
1500×500，并支持置顶帖子。手动修改后需要同时检查 Header 裁剪和置顶
Thread。来源：[X Profile 官方说明](https://help.x.com/en/managing-your-account/how-to-customize-your-profile)。

## Header 合同

画布：1500×500 PNG。

最终可见英文：

- `AI Builder for Human3.0`
- `Building open systems for cognitive sovereignty`
- `20 VERIFIED AGENT SKILLS · WENCHANG · BUILD IN PUBLIC`

目标画面使用深海军蓝、克制青色、分层开放系统架构和一个暖色判断节点。暖色
节点表示人在可检查机器系统中的最终判断。整体应接近开放 AI 实验室的定制
编辑视觉，通过材料、光线和空间层建立深度，避免堆叠界面组件。

重要文字必须避开左下头像遮挡区和外侧裁剪区。生成图无法保证精确英文或安全
裁剪时，继续使用确定性版本，不为了视觉效果牺牲可读性。

## 内容支柱

| 内容支柱 | 比例 | 给读者的价值 | 必须提供的证据 |
| --- | ---: | --- | --- |
| Build in Public | 55% | 工程判断、失败、CI、发布机制和真实结果 | Commit、diff、日志、截图、测量结果或明确限制 |
| Agent Skills Playbooks | 25% | 复现路径、Skill 设计、Case Pack 和开源边界 | 公开源码、示例、输出合同或可执行试用 |
| Human3.0 | 20% | 认知主权、人机边界、个人系统和长期资产 | 一个具体工作流和一个明确的人类判断边界 |

## 写作合同

每一条帖子都需要：

- 面向全球读者重新写作，不逐句翻译中文稿；
- 只保留一个主张、一条证据路径和一个 CTA；
- 使用短句和具体名词；
- 用普通语言解释陌生项目名；
- 在给出结果时同步说明限制；
- 不虚构用户、效率提升、收入、热度或产品效果；
- 解释中文平台交付形式时，使用 `newsletter`、`long-form essay`、
  `carousel` 或 `visual post`。

推荐结构：

- **Build Log：** Problem → Decision → Evidence → Limitation → CTA
- **Framework：** Observation → Model → Example → Human boundary → Question
- **Case Study：** Input → Workflow → Output → Failure boundary → Reproduction

避免：

- 没有产物和证据的泛泛激励；
- 一条帖子同时讲多个无关结论；
- 互动诱导、自动回复、批量关注、互赞、群发私信和无观点转发；
- 把下载量写成用户成功。

## 语气

优先使用：

- `I built`、`I checked`、`this failed`、`the tradeoff` 这类构建者表达；
- 有证据支撑的克制自信；
- 第一人称承担判断责任；
- `Which step failed?`、`What evidence was missing?` 这类具体问题。

避免：

- 夸张的发布语言；
- 无法解释的未来主义口号；
- 暗示 AI 可以取消人的判断；
- 没有一句话解释的术语。

## CTA 轮换

每条帖子只选择一个：

1. **复现：** `Try the same step and tell me where your result differs.`
2. **检查：** `Read the source and challenge the boundary I chose.`
3. **诊断：** `Which step would block you from trying this?`
4. **判断：** `What would you keep under human control?`
5. **反馈：** `Open an Issue with the runtime, input, and first failing step.`

默认反馈问题：

> Try one skill. Send the runtime, the input you used, the first step that
> failed, and what you expected instead.

## 证据与数据规则

发布任何数字前：

1. 记录来源和 UTC 检查时间；
2. 区分仓库状态、平台分发和用户结果；
3. 保留分母；
4. 说明这个数字不能证明什么；
5. 如果实际发布日期和起草日期不同，重新刷新数字。

证据优先级：

1. 公开源码或精确命令；
2. 相关输出截图；
3. 小范围标注 diff；
4. 从已验证来源整理的图；
5. 只有观点帖或提问帖可以只用文字。

## 节奏与时间预算

| 工作 | 每周时间 |
| --- | ---: |
| 三条英文原创帖 | 135 分钟 |
| 五天定向回复 | 75 分钟 |
| 附件和链接检查 | 15 分钟 |
| 数据复盘和下周判断 | 15 分钟 |

发布节奏：

- Tuesday：Build Log
- Thursday：Framework / Human3.0
- Saturday：Case Study / Playbook
- 初始时间：`14:00 UTC`
- 每周至少 15 条实质回复
- 每周最多 1 条 Quote Post 和 1 条 Community Post

## 回复标准

实质回复至少贡献一项：

- 相关案例；
- 有理由的明确不同意见；
- 可复现失败；
- 有用来源；
- 能暴露真实设计取舍的问题。

推荐结构：

> 具体观察 → 相关经验或证据 → 一个真实问题

只有仓库内容确实能回答对方的问题时才提供链接，不把每次回复变成自我推广。

## Community 门禁

X 当前要求使用公开账号加入 Communities。Community 帖子也可能出现在
Profile、搜索和时间线中，因此需要按普通公开品牌内容审核。来源：
[X Communities 官方说明](https://help.x.com/en/using-x/communities)。

首次发布 Community Post 前：

1. 阅读 Community 规则；
2. 观察七天；
3. 找出三个反复出现的问题；
4. 先完成至少两次有价值回复；
5. 只发布直接相关的案例；
6. 不把同一份文案复制到多个 Communities。

## 数据衡量

跟踪漏斗：

`impressions → profile visits → link clicks → trial attempts → independent completions → concrete feedback`

| 现象 | 初步诊断 | 下一步实验 |
| --- | --- | --- |
| 曝光高、Profile visits 低 | 开头或定位不清 | 围绕具体问题重写前两行 |
| Profile visits 高、链接点击低 | Profile、置顶帖或 CTA 不清 | 只保留一个明确试用入口 |
| 链接点击高、试用低 | 安装或五分钟路径存在摩擦 | 观察一位新用户并删除首个阻塞点 |
| 试用成功、没有讨论 | 反馈问题过宽 | 询问 runtime、input、first failure 和 expectation |

X 官方说明：活动面板默认显示 28 天数据，CSV 使用 UTC/GMT，每次最多导出
30 天和 3,000 条帖子，数据可能需要 36 小时稳定。来源：
[X Post Activity Dashboard](https://business.x.com/en/help/campaign-measurement-and-analytics/tweet-activity-dashboard)。

## 决策门

第四周：

- 根据高质量回复和试用数延续最强内容支柱；
- 点击没有变成试用时，先重写五分钟路径；
- 不把单条高曝光帖子当成稳定内容支柱。

第八周：

- 除非测量到明确的人工瓶颈，否则继续不购买付费工具；
- 至少积累四周可比数据后再调整发布时间。

第十二周：

- 至少有一位外部用户独立复现 Theme 01 或等价 Skill 试用后，才启动
  Theme 02；
- 如果仍未出现复现，先公开摩擦、改进试用路径，不继续扩大主题库存。

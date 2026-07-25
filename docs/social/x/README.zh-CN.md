# X 英文启动包

[English](README.md)

这个目录把仓库里的真实构建证据整理成 Sundy Yang 的 90 天纯英文 X
实验。仓库负责沉淀文案、证据、节奏和数据口径；账号资料修改、发布、回复、
加入 Community 和最终事实确认仍由用户人工完成。

## 语言约定

- 直接发布到 X 的内容使用英文：Display name、Bio、Header 可见文字、
  帖子、Thread 和回复。
- 给用户看的策略、操作说明、选题解释、验收、复盘和数据解读使用中文。
- 命令、Handle、文件名、产品名和必须精确复制的英文原文保持原样。
- 给 ChatGPT 等工具的提示词优先使用中文说明；只有最终需要出现在图片或
  X 中的文字保留英文。

## 使用顺序

1. 阅读 [品牌规范](brand-system.md)。
2. 使用 [ChatGPT Header 完整提示词](assets/header/chatgpt-header-prompt.md)
   生成并审核升级候选图；当前
   [1500×500 Header](assets/header/x-header-1500x500.png)保留为确定性兜底。
3. 按 [首月英文成稿](first-month-posts.md)发布五帖置顶 Thread。
4. 按 [12 周日历](editorial-calendar.md)执行每周三帖。
5. 从 [互动观察清单](engagement-list.md)人工核对并建立 40 人私有 List。
6. 将真实帖子 URL 和每周数据写入 [数据台账](metrics.csv)。

`metrics.csv` 为了后续脚本处理保留英文列名，常用字段含义如下：

| 字段 | 中文含义 |
| --- | --- |
| `impressions` | 曝光量 |
| `engagements` | 互动量 |
| `profile_visits` | Profile 访问量 |
| `link_clicks` | 链接点击量 |
| `trial_attempts` | 明确开始试用的次数 |
| `independent_completions` | 用户没有作者协助而独立完成的次数 |
| `issues_or_feedback` | Issue 或具体反馈数 |
| `qualified_questions` | 目标受众提出的有效问题数 |
| `actionable_improvements` | 可以直接进入待办的改进项数量 |

## 人工启动清单

- [ ] Display name 更新为 `Sundy Yang | AI Builder`。
- [ ] 保留 `@yangchao228` 和当前人物头像。
- [ ] Bio 使用品牌规范中的 144 字符英文版本。
- [ ] Website 更新为 `https://github.com/yangchao228/my_open_skills`。
- [ ] Header 在桌面端和移动端检查裁剪与头像遮挡。
- [ ] 发布前刷新 ClawHub 和 GitHub 的所有公开数字。
- [ ] 置顶 Thread 五帖顺序、链接和安装命令均已复核。
- [ ] 只把最近仍活跃且确实相关的账号加入私有 List。
- [ ] 先观察 Community 七天，再人工决定是否发布案例。

## 2026-07-24 启动基线

- 仓库发布计划中有 20 个 `verified` releases；
- ClawHub 合计 2,206 downloads、39 installs、1 star、0 comments；
- GitHub 为 0 stars、0 forks、0 open Issues。

这些只是带日期的分发基线，不能证明用户成功、留存、产品价值或独立复现。
后续帖子发布时必须刷新，不能直接沿用旧数字。

## 完成边界

本目录通过本地校验，代表“发布包已准备好”。只有用户在 X 中人工完成资料
修改、发布并把真实 URL 回填台账后，才能记录为“已上线”。

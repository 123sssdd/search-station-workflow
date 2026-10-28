# 自进化机制

情报站每天把当天的问题和经验变成改进，并区分「可夜间自主落实」与「必须等用户确认」两类。依据：00:00 例会定稿（docs/decisions/daily-meeting/01-20261028-1700-final.md）、v2 公共条款、用户 2026-10-28 的要求（指令改动须用户确认）。

![例会与夜间推进](diagrams/daily-meeting.png)

## 1. 闭环

```
白天：各 bot 完成任务/装新 skill/解决问题时随手记 journal
  ↓
00:00 例会：各 bot 交日报 meetings/<YYYYMMDD>/<bot>.md（9 项格式）
  ↓
01 汇总 meetings/<日期>/summary.md；retros/<日期>.md 引用日报 ⑥经验 ⑦问题 ⑧规划与建议，写「问题→原因→解决」「经验」「可优化点」
  ↓
优化规划师出优化提案 decisions/optimizations-<日期>/优化规划师-<HHMM>.md（格式：问题 → 改法 → 影响 bot/文件 → 是否改指令）
  ↓
Brainstorm 02 评审（终审默认只看阻塞）→ BrainStorm 01 拍板 decisions/optimizations-<日期>/01-final-<HHMM>.md
  ↓
┌ 不改指令（文档、模板、架构图、skills/工具清单、配置示例）：A 类，夜间自主落实 → 推送仓库 → 记 CHANGELOG
└ 改指令（任何 bot 指令条款、轮值/门禁/权限规则）：B 类，起草 vN-draft，标「待你决定」写进早报
       ↓ 用户 10:00 后确认
     更新 bot-instructions.md → 各 bot 采用 → CHANGELOG 记版本 → 推送仓库 → Memory 写 Notion Decisions
```

要点：
- 每个 bot 每天最多 2 条优化建议，每条标明是否需改指令。
- 需改指令的一律 B 类，由优化规划师汇总、02 评审，再交用户拍板；bot 不得自己改。
- 例会时间：00:00 召集等 15 分钟 → 00:15–00:45 汇总、提案、评审、A/B 分类 → 约 00:45 进入清单循环 → 01:30 前定稿。
- 会后 01 发中文简报；夜间按默认执行的事项在早报说明。

## 2. 文件布局（共享工作目录）

```
<WORKSPACE>/
  bot-instructions.md            现行指令（唯一生效版本）
  bot-instructions-vN-draft.md   草案（未生效）
  retros/<YYYY-MM-DD>.md         每日复盘（01 汇总；末尾「追加」段并入各 bot 补交）
  retros/inputs/<YYYY-MM-DD>/<bot>.md   各 bot 复盘原始输入
  meetings/<YYYYMMDD>/<bot>.md   日报（会议日目录，文件内注明覆盖日期）
  meetings/<YYYYMMDD>/summary.md 01 汇总
  meetings/capabilities-baseline.md  能力基线（首次全量例会生成，每周一刷新）
  profiles/<bot>.md              常驻档案：角色与负责、指令版本、skills/工具/连接器（只写名字和用途）、中期规划
  decisions/<主题>/<bot>-<YYYYMMDD-HHMM>.md   意见落盘
  decisions/<主题>/01-final-<HHMM>.md        拍板
  roadmap.md                     路线图单一来源（本周/本月/长期；每条：目标、负责 bot、依赖、验收标准、状态）
  rounds/                        证据文件与锁
  standards/<domain>.md          第0步领域标准缓存（30 天）
```

- profiles/：10/29 例会全量写一次作为基线；之后改版、新 bot、新 skill/工具时立刻更新；每周一全量核对。
- roadmap.md：每周一例会由优化规划师合并各 bot 规划并去重、标依赖与冲突 → 02 评审 → 01 拍板 → Memory 写 Notion Decisions；docs/roadmap.md 推仓库属 B 类。每日例会只更新状态。
- capabilities.md 推仓库属 B 类：夜里只生成脱敏草稿，白天用户确认后推送。

## 3. 日报 9 项格式

每个有事项的 bot 交；无事项只回一行「今日无事」。每项 ≤3 行，全篇 ≤30 行。素材来自白天 journal。

1. 当前负责（一句）
2. 档案变化（指令/skills/工具，无则「无」）
3. 做了什么（附路径）
4. 未完成及原因
5. 新增 skills/工具与效果
6. 经验
7. 解决的问题（问题 → 原因 → 办法）
8. 未来规划与优化建议：分「未来 1–3 天规划」和「优化建议」（≤2 条，每条标是否需改指令）
9. 需要谁帮忙

收件人 01、02、优化规划师：消息只发路径 + 三行摘要，priority:true；Memory、Todos 读汇总文件。模板：templates/daily-report.md。

## 4. 版本与变更记录

- 每次指令修订追加到 CHANGELOG.md：日期、版本、改了什么、来源决策文件、影响角色（v3 草案拟定由 Memory 唯一写入）。
- 每个 decisions/<主题>/ 维护 INDEX.md 记录意见状态（采纳/未采纳/延后），由拍板方维护（v3 草案）。
- 草案文件必须在首行标「草案，未生效，待用户确认」。
- 用户确认前，草案不得被任何 bot 采用；确认后由 01 更新现行指令文件，Memory 归档 Decisions 并推送仓库（推送属 B 类，在用户确认的同时放行）。

## 5. 首日实例（2026-10-28）

- 复盘：retros/2026-10-28.md（P1–P8、O1–O7）。
- 提案：优化规划师 9 条 + 复盘 O1–O7 + 各 bot 可优化点 → 02 全面评审（无反对，6 处修改 + 3 处缺漏）→ 01 拍板 r2（docs/decisions/optimizations-20261028/01-final-1826.md，B 类 17 条、A 类 9 条、观察 4 条）。
- 结果：文档/模板/配置/架构图（A 类）当晚推送本仓库；指令改动汇成 v3 草案（templates/bot-instructions-v3-draft.md），待用户确认。

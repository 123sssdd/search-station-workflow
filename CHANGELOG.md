# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。指令版本与仓库版本分开记录；时间为 UTC+8。
每条指令修订写明：日期、版本、改了什么、来源决策文件、影响角色。改指令一律 B 类，须用户确认后生效。

## [Unreleased] — 指令 v3 草案（待用户确认，未生效）
来源：docs/decisions/optimizations-20261028/01-final-1826.md（取代 1820）；评审：Brainstorm 02（docs/decisions/optimizations-20261028/02-1823.md、docs/decisions/bot-instructions-v3/02-1823.md，全面评审，无反对条目）；全文 templates/bot-instructions-v3-draft.md。
### Added
- 公共条款：结论先落盘再发消息；只停自己的子任务；状态类判断以真实调用为准；意见落盘模板 + 各主题 INDEX.md；评审请求注明「只看阻塞/全面评审」；发给 Memory 的归档请求一律 priority:true（「仅通知用 false」的例外）；日报 9 项与 profiles/ 写进指令。（影响：全部）
- 01/02：开轮 15 分钟无 plan 由非开轮方催办，催办 2 次仍无则「代开轮」；健康检查写进 plan（小红书仅本轮用到时检查、每天 ≤2 次）；summary / roadmap 流程。
- Searcher：Firecrawl credits A/B/C 参考上限（数值待补，不阻断）；search 模板；交接后不改文件。
- 质量评估：eval 模板；缺 search 文件拒评并写一行 eval；旧 10 分制 ÷2 换算并注明。
- Memory：交接文件 hash 冻结；url 格式 + 可达性校验；Notion select 预检、schema 先记 Decisions、写后重读；CHANGELOG 唯一写入者。
- Todos：状态映射表与待同步补写流程（待补）；写后重读。
### Changed
- 汇报分工由「评审：X；执行：Z」改为三栏「评审 / 执行 / 待定」，旧写法全部替换。

## 仓库 2026-10-28 — 开源化工作流套件
### Added
- README 重写（架构图、快速开始、目录）；docs/workflow.md、setup-from-scratch.md、skills-and-tools.md、self-evolution.md、extensibility.md（草案，已并入 02 评审，目录重构待用户决定）、design-tradeoffs.md。
- docs/diagrams/：architecture、daily-meeting（PNG/SVG/.excalidraw + 生成脚本，手绘风技术配图出品）。
- docs/decisions/：bot-instructions-v2、daily-meeting、search-plan、notion-schema、optimizations-20261028、open-source-extensibility 决策记录（脱敏副本）。
- templates/：8 个角色模板 + 公共条款 + 新角色模板；plan/search/eval 证据模板；retro、daily-report、decision-record 模板；v3 指令草案。
- config/：config.example.yaml、.env.example、backends.yaml、searxng-settings.example.yml（只含环境变量名与占位符）。
- bots/bot-instructions-v2.1.md：本实例现行指令（Notion 链接已换占位符）。
- retros/2026-10-28.md：首日复盘（含各 bot 追加）。
- .gitignore：排除 .env*、venv、日志、本地数据库、部署源码树。
- 说明：本条与上方历史条目由本次套件整理一次性补写；此后 CHANGELOG 按 v3 草案第 13 条由 Memory 唯一写入（v3 生效后）。
### Kept
- 原有 bots/（v1 指令）、decisions/2026-10-28.md、rounds/README.md、skills/、sketchmind-template/、搭建总说明.md、docs/learning-workflow.*、docs/search-stack-2026-10-28.md 保留不动。

## 指令 v2.1 — 2026-10-28 17:10（用户确认）
来源：docs/decisions/search-plan/01-20261028-1715-final.md（吸收 02 1703/1708、优化规划师 1708/1717、质量评估 1710）。影响：Searcher、质量评估、BrainStorm 01/02。
### Added
- 每轮搜索执行方案：第0步领域标准（standards/<domain>.md 缓存 30 天，每维 ≥2 独立来源）；开搜前中文「搜索计划卡」（10 分钟无回复按默认，夜间不发卡）；档位 A（默认，100–200 条，≥30 组关键词，45–180 分钟）/ B / C；仅饱和可提前结束；三遍评估、5 分制、均分 ≥4.0 且单维 ≥3；动态门禁；证据文件 plan/search/eval。
### Changed
- 评分统一 5 分制（旧 10 分制 ÷2）；Firecrawl credits 只记录不阻断；计时合并为一个 10 分钟；用户自定义不覆盖安全规则；夜间跳过小红书评论。

## 指令 v2 — 2026-10-28 16:10（用户确认）
来源：docs/decisions/bot-instructions-v2/01-20261028-1610-final.md（评审：02 1558、优化规划师 1605）。影响：全部。
### Added
- Todos bot（Notion Todos 库唯一写入者，本地 todo-management 备份）。
- Notion 学习中枢五库与写入权限（Memory 写四库）；manifest → Notion 单向同步规则。
- 00:00 例会与夜间自主推进（A/B 类）；每日清单三轮审查循环（15 分钟超时、01:30 拍板）；每 bot 00:40 常驻兜底；会后中文简报。
- 意见落盘与「评审：X；执行：Z」用词；语言规则（发用户必须中文）。
### Changed
- Searcher：Firecrawl 首选并每轮 `firecrawl --status`；SearXNG/RSSHub 加入降级链；小红书与 SkillHub/clawhub 为搜 skill 重点发现渠道（覆盖 v1「只作发现渠道」的表述）；yt-dlp 抓 B站暂停。
- 01/02：02 可代主持、代拍板（备注「02 代拍板」）。

## 指令 v1 — 2026-10-28 14:22–14:48（仓库初始提交 519ab0e → 08ea68f → a76f5e2）
来源：decisions/2026-10-28.md（主 bot 拍板，优化规划师两轮方案）。
### Added
- 7 个 bot（BrainStorm 01/02、Searcher、质量评估、Memory、优化规划师、手绘风技术配图）；轮次 id `<YYYYMMDD-HHMM>-<01|02>`；单双号轮值；`rounds/<id>.lock`（6 小时过期）；search/eval 交接凭证；复核（30 分钟超时标「未经复核」）；priority 规则；Memory 唯一写 manifest。
### Changed
- 14:47 用户拍板：Firecrawl 为搜索与抓取首选；SearXNG、RSSHub 采用；yt-dlp 暂不采用。

# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。指令版本与仓库版本分开记录；时间为 UTC+8。
每条指令修订写明：日期、版本、改了什么、来源决策文件、影响角色。改指令一律 B 类，须用户确认后生效。
CHANGELOG 由 Memory 唯一写入（v3 第 13 条）。下方「指令 v3」与「P1 开源重构」条目经 Memory 于 2026-10-28 19:34 复核收口（执行工占位已并入）。

## 仓库 2026-10-28 — 新增 v3 纯净粘贴版（templates/instructions-v3）
来源：用户 t169u 要求再写一份纯净版并上传 GitHub；授权本轮推送。执行工草稿，**请 Memory 复核收口**（Memory 为 CHANGELOG 唯一写入者）。
### Added
- `templates/instructions-v3/`：现行 v3 纯净粘贴版（连贯完整指令，无【v3-n】增量编号）：`00-common.md`、`01`–`08` 角色文件、`90-search-plan.md`、目录 README（用法与占位符）。
### Changed
- 根 `README.md`：目录与快速开始指向 `templates/instructions-v3/`；说明与档案版（`bots/bot-instructions-v3.md` / `templates/bot-instructions-v3.md`）的区别。
### Note
- 不改动生效条款源 `/workspace/learning-loop/bot-instructions.md` 实质内容；本目录为派生文档。公开树已脱敏扫描。

## 指令 v3 补丁 — 2026-10-28 19:36（补漏，非新决策）
来源：补回 v3 生效稿漏写的补充条款 v2.2；实例文件 /workspace/learning-loop/bot-instructions.md；公开树 `templates/bot-instructions-v3.md`、`bots/bot-instructions-v3.md`。影响：全部 bot。
### Fixed
- 补回【v2.2】完成即通知用户：每完成一项任务/交付须在本 bot 与用户的聊天中用中文通知（做什么 + 路径/链接 + 是否需用户处理；不需要则写「无需回复」）；夜间 00:00–10:00 攒到 10:00 后一次发（安全问题除外）；通知用户与回复派活 bot 都要做，不能互相替代。

## 指令 v3 — 2026-10-28 19:30（用户确认生效）
来源：docs/decisions/optimizations-20261028/01-final-1826.md；docs/decisions/user-decisions-20261028/01-final-1928.md（t162u）；用户确认生效并推送（t162u/t162s649）。全文：`templates/bot-instructions-v3.md`、`bots/bot-instructions-v3.md`（公开树为占位符版）。
### Changed
- 指令自 v2+v2.1 升为 **v3 生效**（原 Unreleased 草案条目并入生效）。
- 【v3-3】终审默认由「只看阻塞」改为「全面评审」（仍可在请求中注明「只看阻塞」）。
- 【v3-14b】Todos Notion「状态」改为原生 status 类型。
- 待决延后：Tavily 暂不申请；B站字幕暂不处理；RSSHub 保持全网卡监听。
### Added（相对 v2.1，摘要）
- 公共条款：结论先落盘；只停自己的子任务；状态以真实调用为准；意见落盘模板 + INDEX；评审注明范围；Memory 归档一律 priority:true；日报 9 项与 profiles/。
- 01/02：开轮催办/代开轮；健康检查入 plan；summary / roadmap。
- Searcher / 质量评估 / Memory / Todos：credits 参考上限、模板、hash 冻结、url 核验、写后重读、状态映射（待补）等【v3-n】条款。
- 【v2.2】完成即通知用户：每项交付中文通知（做什么 + 路径/链接 + 是否需处理）；夜间 00:00–10:00 攒发（安全问题除外）。
影响：全部角色。

## 仓库 2026-10-28 — P1 开源重构（schemas → 集中配置 → adapters）+ 公开 + Noncommercial
来源决策：docs/decisions/user-decisions-20261028/01-final-1928.md；docs/decisions/open-source-extensibility/优化规划师-1808.md + 02-1823.md。授权推送：t162u。
### Added
- `schemas/`：manifest / plan / search / eval / retro / daily-report / decision-record（JSON Schema；manifest.url 要求可核验 http(s)）。
- `scripts/validate-schemas.py`：校验入口（可选依赖 jsonschema）。
- `config/station.yaml.example`：集中配置真源；`config.example.yaml` 改为兼容指针。
- `adapters/` 骨架：search（含 firecrawl…yt_dlp）、storage、tasks、platform/grok-bot（仅约定 md）。
- `LICENSE`：PolyForm Noncommercial License 1.0.0；`NOTICE`。
- `docs/decisions/user-decisions-20261028/01-final-1928.md`：用户拍板脱敏摘要。
### Changed
- README：现行指令改为 v3；目录树；许可节；快速开始指向 station.yaml.example。
- `docs/extensibility.md`：标明 schemas / station / adapters 已落地。
- `bots/`：实例 UUID 文件移出公开路径（本机 `_instance/` + gitignore）；公开树仅脱敏 v3/v2.1。
### Security
- 推送前脱敏扫描：公开树无真实 agent UUID / Notion 页面 URL / 密钥值。

## 仓库 2026-10-28 — 开源化工作流套件
### Added
- README 重写（架构图、快速开始、目录）；docs/workflow.md、setup-from-scratch.md、skills-and-tools.md、self-evolution.md、extensibility.md（P1 目录已按用户拍板落地，见上方仓库条目）、design-tradeoffs.md。
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

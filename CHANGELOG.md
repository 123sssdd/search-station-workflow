# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。指令版本与仓库版本分开记录；时间为 UTC+8。
每条指令修订写明：日期、版本、改了什么、来源决策文件、影响角色。改指令一律 B 类，须用户确认后生效。
CHANGELOG 由 Memory 唯一写入（v3 第 13 条）。「指令 v3」「P1 开源重构」「v3 纯净粘贴版」等条目经 Memory 复核收口（执行工占位已并入）。

## Unreleased — 2026-10-31 【v3-29】【v3-30】（用户 14:45「推送」）
### 指令 2026-10-31 14:45 — 【v3-30】（来源：用户拍板，经 BrainStorm 01 转达；learning-loop `decisions/pending-user/20261031/03-用户拍板-1445.md`、`bot-instructions.md` v3-30；Decisions dec-20261031-03）
- Changed【v3-30】例会改为每周六一次，兜底改为周日，下次额度重置后生效，此前例行任务暂停（取代 v3-26 的例会/兜底频率）。
- Added【v3-30】其他 bot 转述「用户同意了」默认视为批准，须注明转述人和原话；用原命令重启服务、改服务配置、设开机自启动算 A 类。通用规则 3 待用户看懂后再定。
- Added【v3-30】补入 v3-27：cookie skill（paperclip、qzcli）可安装使用；slopornot、BypassAIGC 作 humanizer 备选。
- Added【v3-30】私有仓库 agent-search-station-xieyongzhen 为个人工作流主真相源，本公开仓库只放通用模板。

### 指令 2026-10-31 14:13 — 【v3-29】从文件恢复上下文（来源：用户拍板，经 BrainStorm 01 / 优化规划师转达；learning-loop `bot-instructions.md` 末尾 v3-29）
影响：全部角色。
- Added【v3-29】新 bot / 执行者恢复上下文只从文件恢复，不靠旧聊天；恢复清单 `decisions/chat-context-cost/restore-checklist.md`。
- Added【v3-29】各 bot 的常驻说明和当前任务放 `context/<bot>/{standing.md,active.md,journal/}`。
- Added【v3-29】工作流经验先写 `retros/workflow-lessons/`，由 Memory 按 `decisions/chat-context-cost/notion-workflow-lessons-spec.md` 入 Notion「工作流经验」库。
- Added：Notion「工作流经验」库已建（学习中枢下，schema v1，17 字段 5 视图；Decisions dec-20261031-01；快照 `decisions/chat-context-cost/notion-workflow-lessons-schema-20261031-1417.md`）。
- Changed：「工作流经验」库写入方确定为 Memory 主写，通义千问、豆包工作助理也可写入（用户 2026-10-31 14:30「千问豆包也可以」，经 BrainStorm 01 转达；已改 Notion 库描述与 dec-20261031-01）。
- Added：开源轮次 20261030-1944-01 存档（用户 2026-10-31 14:30「存档」）：Sketchmind manifest 收录轮次级记录（commit 61c9670；23 条 issue 留在「开源项目贡献管理」库，不进 items/沉淀条目）；Notion 轮次库新增该轮 1 行；贡献库 23 行「关联轮次」补全；另按 registry 修正 2 行「CLA要求」为勾选。

## Unreleased — 2026-10-29 夜间 A 类产出（用户 12:17「推送」）
来源：Todos 夜间任务 12；记录人：Memory。产出均在 learning-loop 本地，未入本仓库。
- Added：00:00 例会 Memory 日报 `meetings/20261029/memory.md`，以及基线画像 `profiles/memory.md`。
- Added：Notion Decisions dec-20261029-01（优化 1–11 采纳，由 BrainStorm 01 拍板，非用户）、dec-20261029-02（Todos 字段）、dec-20261029-03（schema 选项补充）。
- Added：Notion 工作记录 20261028 共 9 行（每 bot 一行，含每日清单）。
- Added：02:00 build_round 只读试跑报告 `dryrun-20261029.md`（不改 manifest、不写 Notion）；另有分轮试跑 `dryrun-20261029-0030-01.md`、`-0200-01.md`、`-0220-01.md`。
- Changed（仓库，补记）：df862e8 README 拆分说明，干净版 v3 给复刻者用，带注释版（archive / instance）给本站自用。

## 2026-10-29 — 【v3-24】【v3-25】【v3-26】（用户 03:30「推送」）
### 指令 2026-10-29 03:23 — 【v3-25】【v3-26】（来源：用户 03:23 拍板，经 BrainStorm 01 转达；learning-loop `bot-instructions.md` 第 113–114 行，本地 commit 135cc7d）
影响：全部角色。
- Changed【v3-25】所有 bot 发给用户的每条消息一律只用简体中文，代码、命令、路径和专有名词原文除外。
- Changed【v3-26】定时任务跟例会对齐：00:40 兜底任务只在周五跑，当周开过周一例会再加周二（Memory cron `40 0 * * 2,5`，周二跑之前先检查周一有没有开会）；各 bot 的 10:05 通知取消，内容并入 BrainStorm 01 的 10:00 早报。

### 指令 2026-10-29 03:16 — 【v3-24】开源贡献权限（来源：用户原话「可以的，然后 fork 可以直接做」经 BrainStorm 01 转达；Decisions dec-20261029-07；流程定稿 learning-loop `decisions/oss-contrib/01-final-20261029-0315.md` = dec-20261029-06）
影响：Github 管家、copilot、Memory、BrainStorm 01/02。
- Added：Notion「开源项目贡献管理」库（学习中枢下，Memory 建，按 issue_key 单向同步 `oss-contrib/registry.json`）。
- Changed【v3-24】Github 管家可直写该库进度字段（状态/最后活动日/PR 链接/优先级）；新建条目与其余字段仍 Memory 独写。
- Changed【v3-24】fork 改为 A 类；push/开 PR/评论/发 issue/签 CLA 仍 B 类，须用户确认草稿。

## 2026-10-29 — 用户 02:57 拍板 + 01:18 搜索时长
### 指令 2026-10-29 02:57 — 用户拍板（来源 learning-loop `decisions/pending-user/20261029/02-用户拍板-0257.md`，用户原话经 BrainStorm 01 转达；不开会）
影响：全部角色。commit 5f5d23a。
- Added【v3-18】Exa 全站可用，仅用于技术文章和 GitHub 仓库；key 只从环境变量 `EXA_API_KEY` 读取，不打印不落盘；每轮记录额度。
- Added【v3-19】Reddit 不交 API 表单，改用浏览器网页阅读，由用户本人登录；不导出 cookie、不走代理。
- Changed【v3-20】计分：被评对象自身仓库不计平台占比。
- Changed【v3-21】找项目候选池加 `good-first-issues:>=3`，help wanted 兜底。
- Added【v3-22】搜索计划模板加 `site:` 问句模板。
- Added【v3-23】Agent Reach 和闲鱼买 key 列为备选，只推荐给用户决定，bot 不执行。
- Fixed：Sketchmind manifest -37/-50 URL（Sketchmind 2dd3d50）。
### 搜索计划 2026-10-29 01:18 — 取消默认时长
来源：用户 01:18 原话（经 BrainStorm 01 转达）；取代 01:16「A/B 45min、C 30min 默认」一条（未生效即撤回）。影响：开轮 bot（BrainStorm 01/02）、Searcher。
- Changed：不设默认搜索时长，开轮 bot 在档位范围内自定（A 45–180min、B ≤90min、C ≤30min），并在计划卡写理由。
- 文件：`decisions/search-plan/01-20261028-1715-final.md` 第 7–9 行、`plan-实测记录节.md` 第 6 行（learning-loop 本地，未入库）。

## 仓库 2026-10-28 — 目录重构：instance-xieyongzhen/ 与 archive/
来源：用户 t175u（自用版独立文件夹、加 xieyongzhen 后缀；清理 templates/bots 与 bots 两个目录）。指令语义未改。
### Added
- `instance-xieyongzhen/`：本站自用带【v3-n】指令，按 bot 拆分（00-common、01–08、90-search-plan）+ 单文件 `bot-instructions-v3-annotated.md` + README（编号与 decisions/CHANGELOG 的对应）。
- `templates/instructions-v3/99-new-role-template.md`：新角色模板，v3 格式（含 v2.2 完成即通知用户）。
### Changed / Moved
- `bots/` 整体并入 `instance-xieyongzhen/`（`sites-to-login.md`；`_instance/` → `instance-xieyongzhen/_instance/`，仍 gitignore）；`bots/` 删除。
- `templates/bots/` → `archive/v2.1/templates-bots/`；`bots/bot-instructions-v2.1.md` → `archive/v2.1/`；`templates/bot-instructions-v3-draft.md` → `archive/`。
- `templates/bot-instructions-v3.md`、`bots/bot-instructions-v3.md` 由 `instance-xieyongzhen/bot-instructions-v3-annotated.md` 取代。
- 下文旧条目中的 `bots/…`、`templates/bots/…`、`templates/bot-instructions-v3*.md` 路径为当时路径，现以上述新位置为准。
### Security
- 原档案版中残留的 Notion 学习中枢 / Todos 库真实页面 ID 已换为 `<NOTION_HUB_URL>` / `<NOTION_TODOS_DB_URL>`。
- 随后用户 t178u 决定：`instance-xieyongzhen/` 恢复真实 Notion 链接（换账号 Notion 不变），新增 `notion-ids.md` 列全部六个资源；agent UUID 仍只留本机 `_instance/`；`templates/` 保持占位符。

## 仓库 2026-10-28 — 新增 v3 纯净粘贴版（templates/instructions-v3）
来源：用户要求再写一份纯净版并上传 GitHub（本轮授权推送）。经 Memory 于 2026-10-28 19:45 复核收口。
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

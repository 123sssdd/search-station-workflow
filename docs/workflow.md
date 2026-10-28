# 情报站工作流说明

依据：现行指令 v2（2026-10-28 16:10 定稿）+ v2.1（17:10，用户确认）、v1 规则决定（decisions/2026-10-28.md）、00:00 例会定稿（docs/decisions/daily-meeting/01-20261028-1700-final.md）、搜索执行方案定稿（docs/decisions/search-plan/01-20261028-1715-final.md）、首日复盘 retros/2026-10-28.md。
时间一律为 UTC+8。

## 1. 角色与分工

| 角色 | 定位 | 主要输入 | 主要输出 | 独占写入 |
|---|---|---|---|---|
| BrainStorm 01 | 主 bot、牵头决策；单号日当值；每日 00:00 主持例会 | 用户内容、eval 文件、提案 | 关键词发散、搜索计划卡、排序清单、拍板记录、例会汇总 meetings/<日期>/summary.md | — |
| Brainstorm 02 | 主 bot、评审；双号日当值；01 缺席或 30 分钟未响应时代主持、代拍板（备注「02 代拍板」） | 同上 | 复核意见、评审文件 | — |
| Searcher | 搜索并验链 | 派活消息（带轮次 id）、plan 文件 | rounds/search-<id>.md | — |
| 质量评估 | 评分与准出门禁 | search 文件、领域标准 | rounds/eval-<id>.md | — |
| Memory | 归档、看板与知识库 | 用户确认原话、search/eval、规则决定 | manifest.json、Notion 四库、decisions 归档 | manifest.json；Notion 工作记录/轮次/沉淀条目/Decisions |
| 优化规划师 | 出方案，不直接改其他 bot | 复盘、问题、日报 | decisions/<主题>/优化规划师-<时间>.md | — |
| 手绘风技术配图 | 所有架构图/流程图 | 文档、源码 | png/svg + .excalidraw 源文件 | 仓库架构图 |
| Todos | 待办与每日清单 | 例会结论、其他 bot 的待办请求 | Notion Todos 库、本地备份 | Notion Todos 库 |

汇报分工固定写法：「评审：X；执行：Z」。转述他人立场必须附文件路径，否则标「未确认」。

## 2. 轮值、轮次 id 与锁

- 轮次 id：`<YYYYMMDD-HHMM>-<01|02>`（UTC+8），由开轮的主 bot 生成并写进每条派活消息；后缀即 owner。
- 轮值只决定谁开新一轮：单号日 01 开、双号日 02 开；一轮开始后归锁的 owner 负责到底，跨日不换人。00:00 后的夜间轮次按新日期单双号归属，另一方复核。
- 不当值时收到用户新内容：不开轮，priority:true 转给当值主 bot，并告诉用户已转交。
- 锁：开轮前检查 `rounds/` 下有无未过期 `.lock`；没有才写 `rounds/<id>.lock`（owner、开始时间、当前进度），每推进一步更新；结束改名 `.done`。**6 小时**无更新即过期，接手方须先 priority:true 告知原 owner。
- 复核：发排序给用户前，priority:true 把轮次 id 发给另一主 bot；复核方检查证据文件是否齐全、有无跳步，回「通过」或「不通过+原因」；30 分钟无回复先发用户并标「未经复核」。
- 主 bot 阅读边界：只读用户亲自发来的那一个链接/文件；其余搜索、抓取一律交 Searcher。

## 3. 证据文件

每轮 3 个证据文件（v2.1 起），模板见 `templates/evidence/`：

| 文件 | 写入者 | 内容 |
|---|---|---|
| `rounds/plan-<id>.md` | 当值主 bot | 第0步领域标准、档位、关键词组、平台、用户自定义参数、进度、降级记录 |
| `rounds/search-<id>.md` | Searcher | 条目表（字段与 manifest items 对齐）、链接核实状态、被拦来源 |
| `rounds/eval-<id>.md` | 质量评估 | 头部「动态门禁」、浅评/深评/抽检、准出结论 |

- 缺 search 或 eval，结果只算「草案」，Memory 不推送 manifest。
- 质量评估无 search 文件拒绝开评（首日 P4：缺交接文件被拦下又补交）。
- Memory 推送 manifest 还须附用户确认原话（含时间）。

## 4. 消息与意见落盘

- 需对方行动一律 priority:true；仅通知用 false。
- 设计/评审意见由发送方写 `decisions/<主题>/<bot>-<YYYYMMDD-HHMM>.md`，消息只附「路径 + 摘要」。
- 发给用户的消息必须中文；bot 之间中英文均可。
- 禁止编造链接或数据。

## 5. 00:00 例会与夜间自主推进

用户 00:00–10:00 休息。流程（定稿 01-20261028-1700-final）：

1. 00:00 01 召集，等 15 分钟；有任务或有未完成事项的 bot 交完整日报，其余不唤醒、汇总里标「今日无事」。
2. 日报写 `meetings/<YYYYMMDD>/<bot>.md`（标明覆盖日期——00:00 汇报的是前一天），9 项格式见 `templates/daily-report.md`；收件人 01、02、优化规划师，消息只发路径 + 三行摘要。
3. 00:15–00:45：01 汇总 `meetings/<日期>/summary.md`（能力矩阵、进展、经验、问题、路线图），优化规划师出优化提案，02 评审，A/B 分类。
4. 约 00:45 进入每日清单循环：Todos 写初稿 → 01、02、优化规划师审查 → Todos 修改 → 再审，最多三轮；每轮等 15 分钟未回复视为通过；01:30 未定稿由 01（缺席则 02）拍板。
5. 定稿后 Todos 写 Notion Todos 库（计划日=当天），汇总发 Memory 写工作记录，priority:true 通知每个 A 类任务负责 bot。
6. 会后 01 给用户发一条中文简报（清单链接、夜间 A 类任务与定时任务是否已建、10:00 后待用户的 B 类事项）。

**A 类（夜间可自主）**：搜索/规划/设计/沉淀草稿/整理/复核；Todos 写 Todos 库；Memory 写工作记录与 Decisions 草稿；删除自己为当日任务建的一次性定时任务。
**B 类（只准备材料，标「待用户决定」）**：关键决策、登录失效/扫码、凭据/付费、对外发消息、推送 manifest（因此夜间也不同步 Notion 轮次/沉淀库）、改 bot 指令或配置、其余删除。除安全问题外夜间不打扰用户。

## 6. 00:40 常驻兜底

建定时任务有时需用户确认，而夜里用户不在（首日 P6）。因此每个 bot 在用户在场时建好每日 00:40 常驻任务：「读 Notion Todos 库当天分配给我的 A 类任务并执行，完成后告诉 Todos 改状态」。收到 Todos 派发时，能建一次性定时任务就建并回「已创建」，不能则回「建任务待确认」，由兜底任务执行。优化规划师的兜底与例会提案时段接近，提案优先、兜底顺延。

## 7. 搜索栈与降级链

- **首选 Firecrawl**（用户拍板，不考虑积分花费）：每轮先 `firecrawl --status` 确认登录与额度并写入 plan；key 经环境变量 `FIRECRAWL_API_KEY` 加载。
- 降级顺序：SearXNG（127.0.0.1:8888）/ WebSearch → curl_cffi + MarkItDown → Jina Reader（r.jina.ai，免 key 部分）→ Crawl4AI（本地 Chromium 渲染 JS）。每次降级写进 plan。
- RSSHub（127.0.0.1:1200）只用于公开榜单/热榜（B站排行、知乎热榜等匿名可用）。
- 已知被拦（box 出口 IP）：知乎 403、B站 412；yt-dlp 抓 B站暂停，不用 cookie；B站字幕方案待用户决定。
- 原则：只读公开页面，遵守 robots/ToS，限速；不绕过验证码或登录墙。
- 验链：每条链接实际请求；404=失效，403/超时标「未能确认」；clawhub 对任意路径返回 200，需看页面内容/API 而非状态码。

## 8. 小红书 / SkillHub 搜 skill 规则

- 找 skill 时小红书与 SkillHub/clawhub 是重点**发现**渠道；结论仍须追溯到原始链接/仓库并验链。
- 小红书：box 浏览器由用户本人登录；可关键词搜索、搜 "red skill"、问点点 AI；只读低频（每轮 ≤20 帖、每帖 ≤10 条评论），不发帖/评论/私信；遇设备超限或掉线即停并报主 bot（B 类）。登录状态以「能否返回搜索结果」为准（首日 P1）。夜间按默认执行时跳过小红书评论读取。
- SkillHub：api.skillhub.cn 接口可直接取 SKILL.md；评论很少，口碑另找来源（GitHub issues）。

## 9. Notion 学习中枢五库

| 库 | 唯一写入者 | 要点 |
|---|---|---|
| 工作记录 | Memory | 日期×bot 一行，log_key=<YYYYMMDD>-<bot>；类型 日常/周复盘 |
| Todos | Todos | todo_id=todo-<YYYYMMDD>-<序号>；状态 待办/进行中/待用户决定/阻塞/已完成/已取消 |
| 沉淀条目 | Memory | 与 manifest items 1:1，manifest_id 唯一键，content_hash/synced_at/archived/raw_json |
| 轮次 | Memory | manifest_id(rounds.id)、date、topic、picked、content_hash、synced_at |
| Decisions | Memory | dec-<YYYYMMDD>-<序号>，状态 生效/废止，取代(自关联) |

同步：manifest 推送成功后单向镜像——先比对顶层 updatedAt，变了再按 manifest_id + content_hash upsert；删除只标 archived；只改属性不动正文；≤3 次/秒；不反写。写入前脱敏。完整 schema 见 `docs/setup-from-scratch.md` 第 4 步。

## 10. Sketchmind 看板与 manifest

- GitHub Pages 静态看板，数据只来自仓库根目录 `manifest.json`（模板见 `sketchmind-template/`）；不用数据库、不用 `/api/hub`。
- 只有 Memory 改 manifest.json 并 push；推送属 B 类，夜间不推。
- manifest 字段：id、title、url、type、source、category、date、summary、quality、relevance、score、round、reason、read、applied、effect、notes、tags。

## 11. 架构图

由「手绘风技术配图」bot 负责，遵循 project-diagram-studio 浅色手绘风；必须同时交 `.excalidraw` 源文件；当前图在 `docs/diagrams/`（architecture、daily-meeting）。

## 12. Todos 相关 skills

Todos 可用：leader（模糊想法→任务书）、planning-with-files（多步任务跟进，手动流程）、spec-to-implementation（需求页拆成 Notion 任务）、knowledge-capture（复盘页，只能写 Todos 库或用户指定页）、todo-management（本地备份，环境变量 TODO_DB）；todo-tracker 已装但不用。先写 Notion，成功后镜像本地；Notion 写失败先记本地标「待同步」。

## 13. 搜索执行方案 v2.1 摘要

- **第0步 领域标准**：先查 `standards/<domain>.md` 缓存（30 天有效）；新领域完整预搜 ≤30 分钟；3–8 个维度，每维 ≥2 个独立来源，单源维度标「弱」权重减半；质量评估复核；并入 plan-<id>.md。
- **搜索计划卡**：开搜前值班 BrainStorm 用中文发给用户：档位、默认时长与预计结束时间、领域、日期范围、目标条数、关键词示例 5–8 组、平台、准出要点；可「按默认开始」或「自定义」（只覆盖参数，不覆盖安全规则）。10 分钟内用户未回复且值班方无异议即按默认开搜；夜间不发卡，早报说明。
- **档位**：A 广域（默认）原始 100–200 条、去重 ≥60、关键词组 ≥30、入选 10–20、45–180 分钟；B 选型 去重 ≥20、关键词组 ≥15、≤90 分钟；C 定点 官方确认 + 2 个独立来源、≤30 分钟。单一来源 ≤40%；执行率 ≥90%。
- **提前结束**：仅饱和（最近 5 组关键词新增有效去重 <10%）；未达下限须非开轮 BrainStorm 看证据批准。
- **评估**：初筛 → 浅评全部 + 深评 5–8 → 抽检 10%（≥3 条）；5 分制，入选均分 ≥4.0 且单维 ≥3；动态门禁写 eval 头部，值班 BrainStorm 打勾。Firecrawl credits 只记录不阻断。
- **准出**：数量达标或饱和获批；URL 已核验；口碑已附（入选条目每条 ≥1 个口碑来源）；3 个证据文件齐全；时长未超。结束时向用户汇报实际用时、条数、是否饱和。

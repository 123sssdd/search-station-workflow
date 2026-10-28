# 可扩展性设计

> 状态：基于优化规划师方案 docs/decisions/open-source-extensibility/优化规划师-1808.md（2026-10-28 18:08）与 Brainstorm 02 全面评审 02-1823.md。用户 2026-10-28 19:28 拍板按「先 schemas，再集中配置，最后适配器」执行并公开仓库。
> **已落地（P1）**：`schemas/`、`config/station.yaml.example`、`adapters/` 骨架、PolyForm Noncommercial、脱敏公开树。
> **未做（后续）**：roles/ 目录迁移、protocols/ 拆分、local-md 实现代码、校验脚本与健康检查合并等。指令现行为 **v3**（已生效）。
> 目标：别人 clone 仓库后，改一份配置和几份角色文件就能跑起自己的「情报站」，不绑定特定 bot 平台、Notion 或某个搜索服务。


## 已落地（P1，2026-10-28）

- `schemas/*.schema.json` + `scripts/validate-schemas.py`
- `config/station.yaml.example`（真源）+ 保留 `backends.yaml` / `.env.example` / `searxng-settings.example.yml`
- `adapters/{search,storage,tasks,platform}/` stub（含 credits_ref_limit 占位与环境变量名）
- 许可：PolyForm Noncommercial 1.0.0
- 指令：**v3 已生效**（公开树占位符版）

## 1. 目录约定（目标结构）与当前对应

| 目标（方案） | 用途 | 当前仓库对应 |
|---|---|---|
| station.yaml | 集中配置 | **已落地** `config/station.yaml.example`（`config.example.yaml` 为兼容指针） |
| roles/<role>.md | 角色模板（纯文本指令） | templates/bots/<role>.md |
| protocols/ | 公共条款：round、lock、证据文件、A/B 分类、例会 | docs/workflow.md 第 2–6 节 |
| adapters/search/*.md | 搜索后端说明 + 调用约定 | **已落地** `adapters/search/*.md` stub；链仍由 `config/backends.yaml` 真源 |
| adapters/storage/*.md | 存储后端映射 | **已落地** `adapters/storage/*.md`；说明见本文第 4 节 |
| adapters/platform/<平台>.md | 平台差异 | **已落地 stub** `adapters/platform/grok-bot.md` |
| schemas/ | manifest、plan、search、eval、retro 等 JSON Schema | **已落地** `schemas/*.schema.json`（Markdown 模板仍在 templates/） |
| CHANGELOG.md | 版本记录 | CHANGELOG.md |

【02】迁移关系：不并存两套真源。**已迁**：config/config.example.yaml → `config/station.yaml.example`（旧文件改指针）；templates/evidence 字段 → `schemas/`；adapters/search|storage|tasks|platform stub 已建（`backends.yaml` 仍为搜索链真源，adapters 为说明层）。**未迁**：templates/bots/ → roles/；docs/workflow.md 第 2–6 节 → protocols/。

## 2. 新增或替换 bot 角色

- 角色模板固定 8 节：职责、输入文件、输出文件、触发方式（消息/定时/事件）、可用工具、禁止事项、交接对象、【02】写入权限（谁可以写哪个存储；「归档角色唯一写入 manifest 与知识库」「Todos 唯一写入任务库」作为协议级规则）。模板：templates/bots/_new-role-template.md。
- I/O 只通过文件，不依赖对话：输入是 `rounds/<id>` 相关文件和 `decisions/<主题>/`；输出写入约定路径；消息只放「路径 + 摘要」。
- 替换角色：只要满足同一份 I/O 约定即可，不必改其他角色；在配置 `roles` 中启用、停用或改名。
- 最小可运行集合：协调者（BrainStorm）+ 搜索 + 评估 + 归档（Memory）；配图、Todos、优化规划师为可选。
- 现有角色的文件契约：

| 角色 | 读 | 写 |
|---|---|---|
| 主 bot | 用户内容、eval-<id>.md、decisions/ | plan-<id>.md、<id>.lock/.done、meetings/<日期>/summary.md、decisions/<主题>/01-final-*.md |
| Searcher | plan-<id>.md | search-<id>.md |
| 质量评估 | search-<id>.md、standards/<domain>.md | eval-<id>.md |
| Memory | search/eval、用户确认原话、decisions/ | manifest.json、Notion 四库 |
| 优化规划师 | retros/、meetings/、decisions/ | decisions/<主题>/优化规划师-*.md |
| 配图 | docs、源码 | docs/diagrams/*.png/.svg/.excalidraw |
| Todos | 例会结论 | Notion Todos 库、本地备份 |

## 3. 搜索后端可插拔

- 统一接口：输入 query、时间范围、条数；输出 search 结果表（title、url、source、date、snippet、signals）。
- 配置 `search.chain` 按顺序列后端，例如 `[firecrawl, searxng, curl_cffi+markitdown, jina, crawl4ai]`，按顺序降级，每次降级写进 plan。
- 每个后端说明写明：前置检查（如 status 命令）、所需环境变量名（不写值）、限额、已知被拦站点；【02】每个后端加 `credits_ref_limit`（参考上限，不阻断，与 v2.1 一致）。见 config/backends.yaml。
- 【02】`discovery_only` 做成按平台的可选项，不默认给小红书：现行 v2 规则下找 skill 时小红书是优先渠道，结论用原始链接核实，所以示例配置写 `xiaohongshu: { discovery_only: false, verify_with_origin: true }`。

## 4. 存储可替换

- 唯一真源：仓库里的 manifest.json + Markdown 文件，由归档角色唯一写入。
- 镜像适配器：notion、obsidian、local-md、none。都是单向同步：按 manifest_id upsert；content_hash 不变跳过；删除只标 archived。
- Obsidian / 本地 Markdown：每个条目一个 .md 文件，元数据放 front-matter，用 wikilink 关联 round 和 decision。
- 看板只读 manifest.json（GitHub Pages），与镜像方式无关。
- 【02】任务库不由 manifest 派生，单独一个「tasks 适配器」（notion / local-sqlite），由 Todos 唯一写入，与「Todos 唯一写入 Todos 库」规则一致。

## 5. 配置集中

- 内容：时区、夜间窗口、例会时间、轮值规则、各档位阈值、超时、角色清单、搜索链、存储适配器、通知方式。
- 【02】必须包含：`user_language: zh`（面向用户的消息语言）；`rotation: odd → coordinator_a / even → coordinator_b`；`night_window` 附 A/B 分类清单；`score_scale: 5` 与门槛（均分 4.0 / 单维 3）。示例见 config/config.example.yaml。
- 密钥只写环境变量名；提供 .env.example，.env 加入 .gitignore。
- 建议加开轮前校验脚本：检查配置字段、必需环境变量是否存在、目录是否齐全（待补；与复盘 O1 健康检查合并考虑）。

## 6. 平台无关的纯文本指令

- 角色文件只写行为和文件约定，不写平台专属工具名；平台差异放 adapters/platform/<平台>.md（如 grok-bot、claude-code、cursor、自建 cron），说明消息、定时、优先级在各平台如何实现。
- 「priority:true」抽象成「需对方处理的通知」，由平台适配文件映射到具体实现。templates/bots/ 中仍保留 priority:true 写法，并注明此映射。

## 7. 版本与变更记录

- 语义化版本：协议改动升主版本，加条款升次版本，措辞改动升补丁版本。每个角色文件头部写 version 和 requires_protocol。
- CHANGELOG.md 每条写：日期、版本、改了什么、来源决策文件、影响的角色。【02】CHANGELOG 由 Memory 唯一写入（与优化清单第 13 条合并，不两处各写）。
- 改指令一律 B 类：起草 → 评审 → 用户确认 → Memory 推送；打 tag 后看板页脚显示当前协议版本（待补）。

## 8. 分步落地（方案建议）

- 【02 调整顺序】P1：先出 schemas（manifest 的 url 字段要求可核验）；P2：station.yaml 与 roles/ 和校验脚本；P3：local-md 实现、tasks 实现、平台适配完善。
- **P1 已落地并推送**（用户 2026-10-28 19:28 放行）：schemas + station.yaml.example + adapters 骨架 + LICENSE + 脱敏 + 公开。
- 余项：roles/ 迁移、protocols/、实现级适配器代码、开轮健康检查脚本。
- 延后（同拍板，不改运行时）：Tavily 申请、B站字幕、RSSHub 改 localhost-only（维持全网卡）。
- 【02】开源前脱敏扫描（token、cookie、个人链接、Notion 页面 ID）已做；仓库已按用户决定公开。

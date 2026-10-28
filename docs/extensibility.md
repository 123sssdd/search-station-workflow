# 可扩展性设计

> 状态：基于优化规划师方案 docs/decisions/open-source-extensibility/优化规划师-1808.md（2026-10-28 18:08）与 Brainstorm 02 全面评审 02-1823.md（同意方向，4 处必改已并入，标【02】）。**仍为草案**：P1–P3 的仓库结构调整属 B 类，等用户确认后再动。
> 目标：别人 clone 仓库后，改一份配置和几份角色文件就能跑起自己的「情报站」，不绑定特定 bot 平台、Notion 或某个搜索服务。

## 1. 目录约定（目标结构）与当前对应

| 目标（方案） | 用途 | 当前仓库对应 |
|---|---|---|
| station.yaml | 集中配置 | config/config.example.yaml（示例，字段同方向） |
| roles/<role>.md | 角色模板（纯文本指令） | templates/bots/<role>.md |
| protocols/ | 公共条款：round、lock、证据文件、A/B 分类、例会 | docs/workflow.md 第 2–6 节 |
| adapters/search/*.md | 搜索后端说明 + 调用约定 | config/backends.yaml + docs/skills-and-tools.md |
| adapters/storage/*.md | 存储后端映射 | 本文第 4 节 |
| adapters/platform/<平台>.md | 平台差异 | 待补 |
| schemas/ | manifest、plan、search、eval、retro 字段定义（JSON Schema） | 待补（现有 Markdown 模板在 templates/） |
| CHANGELOG.md | 版本记录 | CHANGELOG.md |

【02】迁移关系：目标结构落地时由现有目录迁移，不并存两套——templates/bots/ → roles/；config/config.example.yaml → station.yaml（示例）；config/backends.yaml → adapters/search/；docs/workflow.md 第 2–6 节 → protocols/；templates/evidence/ 的字段 → schemas/。迁移前保持现有结构。

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

- 【02 调整顺序】P1：先出 schemas（manifest 的 url 字段要求可核验）；P2：station.yaml 与 roles/ 和校验脚本（校验依赖 schemas）；P3：local-md 存储适配器、tasks 适配器、平台适配文件。
- 每一步推送仓库属 B 类，夜间不推，待用户决定。本次推送只新增文档、模板与配置示例，未做目录重构。
- 【02】开源前做一次脱敏扫描（token、cookie、个人链接、Notion 页面 ID）属 A 类；对外公开属 B 类。

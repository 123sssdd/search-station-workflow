# Skills、连接器与工具清单

规则：只写名字、用途、安装方式和**环境变量名**，从不写值。「新」= 2026-10-28 新增/首次投入使用（依据 retros/2026-10-28.md 第四节及各 bot 复盘输入）。版本号为本实例实测时的版本。

## 1. Skills

| Skill | 使用 bot | 用途 | 安装 | 环境变量 | 新 |
|---|---|---|---|---|---|
| firecrawl-*（firecrawl-cli / search / scrape / crawl / map 等，来自 firecrawl/cli 仓库） | Searcher | 搜索 + 正文抓取首选 | 平台 skill 商店或拷入 workflows | FIRECRAWL_API_KEY | ✅ |
| todo-management | Todos | Notion Todos 的本地 SQLite 备份 | 拷入 workflows；需 sqlite3 | TODO_DB（路径） | ✅ |
| todo-tracker | Todos | 已装，按指令不用（备选） | 同上 | — | ✅ |
| leader | Todos | 把模糊想法写成任务书 | 拷入 workflows | — | ✅ |
| planning-with-files | Todos | 多步任务跟进（task_plan/findings/progress 三文件，手动流程）；默认分支 master，main 链接 404 | 拷入 workflows | — | ✅ |
| spec-to-implementation | Todos | 需求页拆成 Notion 任务（Notion 官方插件） | Notion 官方插件 | — | ✅ |
| knowledge-capture | Todos | 复盘页写进 Notion（只能写 Todos 库或用户指定页） | Notion 官方插件 | — | ✅ |
| project-diagram-studio | 手绘风技术配图 | 手绘风规范（visual-style / review-checklist） | redskill CLI；下载超时则由用户上传压缩包解压 | — | ✅ |
| excalidraw-diagram-skill | 手绘风技术配图 | Excalidraw 图 | 仓库 skills/ | — | ✅（复盘列为在用） |
| grill-me、brainstorming | 主 bot | 追问 / 发散 | 平台 skill | — | ✅（复盘列为在用） |
| brainstorm-getting-started、export-bot-template 等 | Brainstorm 02 | 分享模板草稿、导出 bot 模板 | 平台工具 | — | ✅（待用户确认发布） |
| doc-coauthoring、internal-comms、gov-report-writing、pptx、ppt-craft-master | 通用 | 文档/汇报/PPT | 仓库 skills/ | — | 早于 10-28 |

## 2. MCP 连接器

| 连接器 | 使用 bot | 用途 | 权限约定 | 新 |
|---|---|---|---|---|
| Notion | Memory（四库写）、Todos（Todos 库写）、其他只读或不接入 | 学习中枢五库 | 写前脱敏；≤3 次/秒；relation 用裸 UUID；视图布局部分需人工 | ✅ |
| GitHub | Memory、主 bot | 仓库读写（另有 gh CLI） | manifest 只由 Memory 推 | — |
| Google Drive | 手绘风技术配图等 | 用户上传文件（如 skill 压缩包） | 只读为主 | ✅（首日用于上传 skill 包） |
| Excalidraw | 手绘风技术配图 | 可编辑 .excalidraw 源文件 | — | ✅ |
| X | Searcher | 专用读取通道 | **只读** | ✅ |
| Firecrawl MCP | （未装）| 本实例用 CLI + skills；连接器匹配结果为 0 | 需 FIRECRAWL_API_KEY | 待用户决定是否装 |
| mcp-searxng | Searcher | 把本地 SearXNG 接成 MCP（v1.16.0，`npx -y mcp-searxng`） | SEARXNG_URL | ✅ |

## 3. 本地服务

| 服务 | 地址 | 用途 | 部署 | 新 |
|---|---|---|---|---|
| SearXNG | 127.0.0.1:8888（仅本机） | 免费元搜索，Firecrawl 之后第一级降级；JSON：`/search?q=...&format=json&language=zh-CN` | 源码 master + venv，`python -m searx.webapp`；settings 见 config/ | ✅ |
| RSSHub | 127.0.0.1:1200 | 只用于公开榜单/热榜（B站排行/热门、知乎热榜/日报） | 源码 + Node 22 + pnpm，`pnpm start`（本实例监听所有网卡，建议收紧） | ✅ |

## 4. CLI / 库

| 名称 | 用途 | 安装 | 环境变量 | 状态 | 新 |
|---|---|---|---|---|---|
| firecrawl-cli | 搜索+抓取首选；每轮先 `firecrawl --status` | `npm i -g firecrawl-cli`（v1.23.3） | FIRECRAWL_API_KEY | 在用；并发上限 2 | ✅ |
| gh | GitHub 操作 | 系统包；`gh auth login` | （登录态，不入库） | 在用 | — |
| curl_cffi | 浏览器指纹的轻量抓取，读单页第一跳 | pip（0.17） | — | 在用 | ✅ |
| MarkItDown | URL/PDF/DOCX/HTML → Markdown | pip（0.1.9） | — | 在用 | ✅ |
| Jina Reader | `r.jina.ai/<url>` 读单页 | 免安装 | 免 key 部分；`s.jina.ai` 需 key（未申请） | 在用 | ✅ |
| Crawl4AI + playwright | 本地 Chromium 渲染 JS 页面 | pip（0.9.5）+ chromium | — | 在用（降级链末端） | ✅ |
| Scrapling | 选择器/自适应解析 | `pip install "scrapling[fetchers]"`（0.5） | — | 冒烟通过 | ✅ |
| yt-dlp | B站元数据/字幕 | pip（2026.10.26） | — | **暂停**（box IP 412，不用 cookie） | ✅ |
| todo-management CLI | Todos 本地备份 | 见 skill；PATH 加 ~/.local/bin | TODO_DB | 在用 | ✅ |
| sqlite-tools（静态 3.50.4） | todo-management 依赖 | 放 ~/.local/bin | — | 在用 | ✅ |
| redskill CLI | RedSkill 商店装 skill | 待补 | — | 下载域名不可达时超时 | ✅ |
| cairosvg + Python SVG 脚本 | 渲染架构图 PNG、导出 .excalidraw | pip | — | 在用（docs/diagrams/lib.py、gen_*.py） | ✅ |

## 5. 已评估但未采用 / 待用户决定

依据 rounds/eval-20261028-1606-02（旧 10 分制）：
- Playwright MCP（7.0 初筛）：是否实测 → 待用户决定。
- Tavily MCP（6.0 初筛）：是否申请 key → 待用户决定（14:47 记录为「不申请」，Todos 仍列为待用户决定，以用户最新答复为准）。
- xiaohongshu-mcp：高风险，默认不装，需用户本人明确同意且只读。
- 淘汰：SerpAPI、Serper、SearchApi.io、Perplexity Sonar、Linkup、Vane、LLocalSearch、Browserbase、Apify、Bright Data、browser-use skill、clawhub Crawl（无源码）、Spider_XHS、MediaCrawler。

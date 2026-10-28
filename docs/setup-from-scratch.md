# 从零搭建情报站（新账号）

> 按顺序执行。所有密钥只放在本机环境变量或不进仓库的 `.env` 文件里；本文只写**变量名**。
> 凡标「人工步骤」的，接口做不到，需要用户本人在界面里操作（集中清单见文末）。
> 凡标「待补」的，现有记录里没有，需要搭建者实测后补上。

## 第 1 步：建 8 个 bot

在你的 bot 平台（本实例为 Grok Bot）新建 8 个助手，名称建议与下表一致：

| # | 名称 | 指令模板 |
|---|---|---|
| 1 | BrainStorm 01 | templates/instructions-v3/01-brainstorm-01.md |
| 2 | Brainstorm 02 | templates/instructions-v3/02-brainstorm-02.md |
| 3 | Searcher | templates/instructions-v3/03-searcher.md |
| 4 | 质量评估 | templates/instructions-v3/04-quality-eval.md |
| 5 | Memory | templates/instructions-v3/05-memory.md |
| 6 | 优化规划师 | templates/instructions-v3/06-optimizer.md |
| 7 | 手绘风技术配图 | templates/instructions-v3/07-diagram.md |
| 8 | Todos | templates/instructions-v3/08-todos.md |

建完后把各 bot 的 agent id 填进 `config/config.example.yaml` 的 `roles.<role>.agent_id`（复制为你自己的 `config.yaml`，不必入库），再把模板里的 `<AGENT_ID_*>` 占位符换成实际 id。最小可运行集合：BrainStorm（至少 1 个）+ Searcher + 质量评估 + Memory；其余为可选（见 docs/extensibility.md）。

## 第 2 步：粘贴指令

1. 每个 bot 的指令 = 对应角色模板 + 模板末尾的「公共条款」。
2. 两个主 bot 的指令除第一行外完全相同，修改时必须两段一起改。
3. 把占位符替换为实际值：`<WORKSPACE>`（共享工作目录，本实例为 /workspace/learning-loop）、`<NOTION_HUB_URL>`、`<NOTION_TODOS_DB_URL>`、`<SKETCHMIND_REPO>`、`<SKETCHMIND_PAGES_URL>`、`<WORKFLOW_REPO>`。
4. 指令任何改动都属 B 类：起草 → 评审 → 用户确认 → 更新 CHANGELOG 后再让 bot 采用。

## 第 3 步：设置密钥（只写变量名）

| 变量名 | 用途 | 必需 |
|---|---|---|
| FIRECRAWL_API_KEY | Firecrawl CLI/skills 搜索与抓取（首选） | 是（否则只能走本地降级链） |
| TODO_DB | todo-management 本地 SQLite 路径（非密钥） | Todos 需要 |
| SEARXNG_URL | mcp-searxng 指向本地 SearXNG（非密钥，如 http://127.0.0.1:8888） | 用 mcp-searxng 时 |
| SEARXNG_SECRET | SearXNG settings.yml 的 server.secret_key（自行生成随机值） | 部署 SearXNG 时 |

做法（本实例）：把 `FIRECRAWL_API_KEY=...` 写进不入库的 `<WORKSPACE>/.env.firecrawl`（权限 600），在 `~/.bashrc` 加：

```bash
set -a; [ -f <WORKSPACE>/.env.firecrawl ] && . <WORKSPACE>/.env.firecrawl; set +a
```

GitHub 用 `gh auth login`；Notion、Google Drive、Excalidraw、X 通过平台连接器授权，不需要在仓库里出现任何 token。

## 第 4 步：连接 Notion 并建五库

1. 在平台里连接 Notion 连接器，授权到一个「学习中枢」页面。
2. 建库顺序：Decisions → 轮次 → 沉淀条目 → 工作记录 → Todos。
3. schema（定稿：notion-design-2026-10-28）：

**Decisions**（仅 Memory 写）：decision_id（dec-<YYYYMMDD>-<序号>）、日期、拍板人、内容、影响 bot、状态（生效/废止）、取代（自关联）。

**轮次**（仅 Memory 写）：manifest_id（= manifest rounds.id）、date、topic、picked（→沉淀条目）、content_hash、synced_at。

**沉淀条目**（仅 Memory 写）：与 manifest items 1:1 同名——manifest_id（= manifest id，唯一键）、title、url、type、source、category、date、summary、quality、relevance、score、round（→轮次）、reason、read、applied、effect、notes、tags；另加 content_hash、synced_at、archived、raw_json。

**工作记录**（仅 Memory 写）：标题、date、bot、round_id（→轮次）、summary、decisions（→Decisions）、todos_spawned（→Todos）、links、类型（日常/周复盘）、log_key（<YYYYMMDD>-<bot>，同日同 bot 追加不新建）。

**Todos**（仅 Todos 写）：标题、todo_id（todo-<YYYYMMDD>-<序号>）、状态（待办/进行中/待用户决定/阻塞/已完成/已取消）、优先级 P0–P2、截止日、计划日、来源、来源链接、来源记录（→工作记录）、负责方、领域标签、预计耗时、备注决策选项、完成日、关联沉淀（→沉淀条目）、决策方式（用户决策/例会自主，2026-10-28 16:06 新增）。视图：今日 / 待用户决定 / 状态看板 / 本周复盘 / 逾期。

扩展规则：字段只加不删（弃用改名 `_废弃_xxx`）；新类型只加 select 选项；去重键格式不改；结构变更先记 Decisions 再动手；库顶部写 schema 版本说明。

首日踩坑（来自各 bot 复盘）：
- relation 需要裸 UUID，传 `collection://` 形式会失败。
- MCP 建的关联是单向的，反向字段由对面库的写入者自己加。
- raw_json 写纯 JSON 被拒，改用「json:」前缀。
- select 缺选项会 400：批量写前先 fetch schema 预检；缺项先记 Decisions 再扩展。
- Notion 筛选没有「本周一至周日」，本周复盘视图只能用滚动 7 天；按领域统计由 Todos 在例会时计算。
- 写完要重新读取页面确认，不能只看创建返回值；限速 ≤3 次/秒。

**人工步骤**：Notion 动态视图（Feed/卡片布局、属性换行）无法通过接口完整设置——Views API 没有 Feed 布局；表格「换行」可用 Notion MCP 的 update-view（WRAP CELLS / CARD LAYOUT），Feed 需用户在 Notion 界面手动切换。

## 第 5 步：站点登录（人工步骤）

在 bot 共享的云电脑浏览器里由用户本人登录并勾选长期登录（扫码属 B 类，需用户在场）：

| 优先级 | 网站 | 原因 |
|---|---|---|
| 高 | 小红书 | 未登录几乎无法搜索和查看笔记 |
| 高 | B站 | 未登录搜索受限、风控验证，字幕/评论需登录 |
| 高 | 知乎 | 未登录频繁弹登录墙，回答被截断 |
| 中 | 微信公众号（搜狗微信） | 频繁验证码 |
| 中 | 掘金、CSDN | 登录后搜索更稳定/展开全文 |
| 低 | 抖音、Medium、LinkedIn | 搜索或文章需登录 |

登录后用一次真实搜索验证（能否返回结果），不要凭页面外观判断。只读低频，不发帖/评论/私信。

## 第 6 步：本地部署 SearXNG（127.0.0.1:8888）

本实例做法（box 无 docker，源码 + venv）：

```bash
git clone https://github.com/searxng/searxng.git <WORKSPACE>/searxng
python3 -m venv <WORKSPACE>/.venv-searx
# 按 SearXNG 官方文档安装依赖（具体命令：待补）
mkdir -p <WORKSPACE>/searx-etc
cp config/searxng-settings.example.yml <WORKSPACE>/searx-etc/settings.yml   # 填入自己生成的 secret_key
export SEARXNG_SETTINGS_PATH=<WORKSPACE>/searx-etc/settings.yml               # 变量名以官方文档为准（待补核实）
cd <WORKSPACE>/searxng && nohup <WORKSPACE>/.venv-searx/bin/python -m searx.webapp > ../searx-run.log 2>&1 &
curl 'http://127.0.0.1:8888/search?q=test&format=json&language=zh-CN'
```

要点：只绑定 127.0.0.1；formats 必须含 json；本实例 limiter 关闭（日志会提示缺 limiter.toml，可忽略）。实测 Google CSE 与 DuckDuckGo 有结果；Brave 会「Too many requests」被挂起 180s，DDG 偶发 CAPTCHA。默认未启用百度/搜狗等中文引擎，可在 settings.yml 打开后再测。
接入 MCP：`npx -y mcp-searxng`，环境变量 `SEARXNG_URL=http://127.0.0.1:8888`。

## 第 7 步：本地部署 RSSHub（127.0.0.1:1200）

本实例做法：源码 + Node 22 便携版 + pnpm：

```bash
git clone https://github.com/DIYgod/RSSHub.git <WORKSPACE>/rsshub
# 下载 Node 22 便携版（本实例 v22.23.4）并加入 PATH；RSSHub 要求 node ^22.22.2 || ^24.15.0
# corepack 默认写 /usr/local/share/corepack 会因权限失败（本实例日志 mkdir 报错），设 COREPACK_HOME 到可写目录
export COREPACK_HOME=<WORKSPACE>/.corepack
corepack enable pnpm   # 本实例 pnpm 12.15
cd <WORKSPACE>/rsshub && pnpm install && nohup pnpm start > ../rsshub-run.log 2>&1 &
curl http://127.0.0.1:1200/zhihu/hot
```

注意：本实例 RSSHub 实际监听 *:1200（所有网卡）。用户 2026-10-28 19:28 拍板**维持全网卡监听**，不改为 localhost-only。只用于公开榜单/热榜；UP 主/用户动态路由在 box 出口 IP 下被风控，不配 cookie。新实例若只需本机访问，可自行改绑定地址。

## 第 8 步：搜索与抓取工具

```bash
npm i -g firecrawl-cli          # 本实例 v1.23.3
firecrawl login                 # 或设置 FIRECRAWL_API_KEY
firecrawl --status              # 每轮开搜前必跑，结果写进 plan
python3 -m venv <WORKSPACE>/.venv-search
<WORKSPACE>/.venv-search/bin/pip install curl_cffi markitdown crawl4ai "scrapling[fetchers]"
<WORKSPACE>/.venv-search/bin/playwright install chromium   # Crawl4AI 渲染 JS 需要（具体命令：待补核实）
```

注意：免 key 的 Firecrawl 请求可能因出口 IP 被判为代理而被拒，需用自己的 API key。Scrapling 只装基础包会缺 browserforge，需 `scrapling[fetchers]`。Jina Reader 免 key 用 `https://r.jina.ai/<url>`；`s.jina.ai` 搜索需 key（未申请）。

## 第 9 步：Skills 与 Todos 本地备份

- 把仓库 `skills/` 下目录拷到 bot 的 workflows 目录（本实例 `/home/box/agent-data/workflows/<skill>/`）。手绘 bot 必装 project-diagram-studio（商店下载超时时由用户上传压缩包解压安装）。
- Todos：安装 todo-management（PATH 加 `~/.local/bin`，`TODO_DB` 指向本地库文件，本实例 /workspace/todos/todo.db）；需要 sqlite3（本实例装静态 sqlite-tools 3.50.4 到 ~/.local/bin）。注意 todo-management 只有 pending/in_progress/done/skipped 四种状态，与 Notion 六种状态对不上；create 回显 ID 为 0，以 list 结果为准。
- 完整清单见 docs/skills-and-tools.md。

## 第 10 步：看板（可选但推荐）

用 `sketchmind-template/` 建公开仓库，Settings → Pages → Deploy from branch `main` / 根目录。只有 Memory 改 `manifest.json` 并 push。

## 第 11 步：定时任务（必须在用户在场时建）

| 任务 | 谁建 | 时间 | 内容 |
|---|---|---|---|
| 例会 | BrainStorm 01 | 每日 00:00 | 召集全员复盘、清单循环、会后简报（见 docs/workflow.md 第 5 节） |
| 常驻兜底 | 每个 bot | 每日 00:40 | 读 Notion Todos 库当天分配给自己的 A 类任务并执行，完成后告诉 Todos 改状态 |

建任务可能需要用户点确认卡，夜里用户不在会过期，所以白天一次性建好。周日复盘不单独建任务，并入每日例会；路线图在每周一例会合并。

## 第 12 步：冒烟检查

1. `firecrawl --status` 显示已登录、有余额。
2. `curl 127.0.0.1:8888/search?q=test&format=json` 有结果；`curl 127.0.0.1:1200/zhihu/hot` 返回条目。
3. 小红书在浏览器里真实搜一次能出结果。
4. 跑一轮 C 档定点搜索，确认 plan/search/eval 三个证据文件齐全、lock 改名 .done。

## 人工步骤清单（集中）

- Notion：Feed/卡片等动态视图布局、视图筛选微调。
- 站点登录、扫码、设备超限后的重新登录。
- 平台连接器授权（Notion、GitHub、Google Drive、Excalidraw、X）。
- 定时任务确认卡（白天建）。
- 指令改版、manifest 推送、付费/凭据相关决定（B 类）。

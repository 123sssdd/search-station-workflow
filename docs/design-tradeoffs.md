# 关键设计取舍

每条只写来源里有的理由，并附来源。未在来源中说明的理由不写。

| # | 取舍 | 为什么 | 来源 |
|---|---|---|---|
| 1 | Firecrawl 作搜索与抓取首选，本地栈作降级 | 用户拍板「不考虑积分花费，搜索与抓取均以 Firecrawl 为首选」；Firecrawl 可 search+scrape 一步完成。免 key 请求因 box 出口 IP 被判为代理被拒，所以必须配 key，并每轮先 `firecrawl --status` | decisions/2026-10-28.md 补充（14:47）；search-stack-2026-10-28.md；retros P3 |
| 2 | SearXNG 作第一级降级 | 零费用、无 key；中文技术查询实测每次 28–30 条、相关度高；可接 mcp-searxng（约 0.9 秒） | rounds/eval-20261028-1606-02（9.0 分，旧 10 分制） |
| 3 | RSSHub 只用于公开榜单 | 榜单/热门路由匿名可用；UP 主、用户动态路由在 box IP 下被风控，需 cookie，按规则不配 | search-stack-expansion 实测段 |
| 4 | 不用 cookie、暂停 yt-dlp 抓 B站 | box 出口 IP 被 B站 412 风控，加 impersonate 仍 412；按规则不使用登录 cookie | search-stack-expansion 实测段；retros P8 |
| 5 | 小红书只读低频、风控即停 | 第三方自动化工具 ToS 风险高（可能封号）；用户本人登录后人工节奏阅读最合规 | search-stack-expansion 第二节；v2 Searcher 段 |
| 6 | Memory 是 manifest 与 Notion 四库的唯一写入者 | 单一写入者原则：保证看板与镜像一致；脱敏只在 Memory 一处统一做；推送前核对交接文件 | v1 指令；notion-design；02 v2 评审第 7 条；Memory 复盘 |
| 7 | Todos 库只由 Todos 写，Notion 为主、本地为备 | 写入方唯一；本地不反写避免冲突；Notion 写失败先记本地「待同步」 | v2 Todos 段；02 v2 评审第 4 条 |
| 8 | 看板用静态 manifest.json + GitHub Pages，不用数据库 / `/api/hub` | 搭建说明硬规则：看板只读根目录 manifest.json，不用自建数据库写路径（除非另做带 token 的 HTTP 接口） | 搭建总说明.md 第五节；手绘配图复盘（按拍板重画「无数据库 / 无 /api/hub」） |
| 9 | Notion 是单向只读镜像，不反写 manifest | 以 manifest 为真源；按 manifest_id + content_hash upsert、删除只标 archived，保证可重放 | notion-design-2026-10-28.md；02 15:24 复核 |
| 10 | 改 bot 指令属 B 类，须用户确认 | 用户要求；夜间用户不在，关键决策只准备材料标「待用户决定」；推送批准必须来自用户本人原话 | v2 公共条款；Memory 复盘「推送批准必须来自用户本人原话」 |
| 11 | 每轮必须有证据文件 + 锁 | 证据文件是交接与评估的唯一依据；缺文件不评、Memory 不推；锁防止两个主 bot 同时开轮 | v1 规则决定 1、3；retros P4 |
| 12 | 意见落盘 + 「路径 + 摘要」 | 首日「02 没参与」误会源于转述无原文；落盘后可追溯，沟通效率更高 | retros P2/P7；优化规划师复盘 |
| 13 | 00:40 常驻兜底任务 | 建定时任务需用户确认，夜里卡片会过期；常驻任务白天一次建好 | 优化规划师 v2 评审第 1 条；retros P6 |
| 14 | 评分统一 5 分制，Firecrawl credits 不作准出条件 | 10 分制与「均分 ≥4.0」口径冲突；用户说过 Firecrawl 不计成本，credits 无数值无法判定 | 02 终审 1708 两处阻塞 |
| 15 | 提前结束只认「饱和」 | 用户坚持 A 档下限（100–200 条、≥45 分钟）；未达下限须非开轮 BrainStorm 看证据批准 | search-plan 01-1715-final；优化规划师终审 |
| 16 | 静态信息进档案、日报只报增量，retro 引用日报 | 模板偏重；一处写、多处引用，避免重复 | 优化规划师例会评审第 1、3 条 |

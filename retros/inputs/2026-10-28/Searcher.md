# Searcher 今日复盘（2026-10-28）

## 进度
- 搜索栈轮次 search-20261028-1606-02：52 条，Firecrawl 条目已实测可用（16:10 余额 11,016），Memory 已推送（cc7d7f4）并同步 Notion。
- Notion Feed 轮次 search-20261028-1627-02：12 条，质量评估已出 eval；用户决定本轮不归档。结论：Views API 没有 Feed 布局，需在 Notion 界面手动切；表格换行可走官方 update-view；Playwright 作兜底。
- 1701-01 轮已取消，无文件。
- 指令 v2、搜索方案 v2.1 已存入记忆；建了每日 00:40 兜底定时任务（执行 Todos 分配的 A 类任务）。

## 搜索栈现状
- Firecrawl（CLI v1.23.3）为首选，已登录，key 放在 .env.firecrawl（变量名 FIRECRAWL_API_KEY，不写值）。余额约 11,004，并发上限 2；每轮记录消耗。
- SearXNG 自建于 127.0.0.1:8888，作为第一级降级；之后是 WebSearch → curl_cffi+MarkItDown → Jina → Crawl4AI。
- RSSHub 自建于 127.0.0.1:1200，只用于公开榜单和热榜。
- 知乎、B站在 box 上被拦（403/412）；B站暂停 yt-dlp，不用 cookie。

## 小红书登录状态误判
- 问题：曾把小红书当作「不登录、只作发现渠道」处理，实际 box 浏览器已登录，可搜关键词、搜 "red skill"、问点点 AI；早期轮次的线索靠 BrainStorm 01 只读浏览补上。
- 解决：v2 指令明确已登录状态，搜 skill 时优先用小红书，但结论仍要追溯到原始链接或仓库。
- 教训：开搜前先实测登录状态（截图或打开一页），不要凭旧规则判断；遇设备超限或掉线立即停，报主 bot（B 类）。

## 小红书 / SkillHub 搜 skill 现状
- 小红书：只读低频，每轮 ≤20 帖、每帖 ≤10 条评论；只当线索。
- SkillHub：api.skillhub.cn 接口可用，能直接取 SKILL.md（如 notion 条目）；评论很少，口碑要另找来源（GitHub issues）。clawhub 同理。

## 其他问题与教训
- 用 StopSubagent all:true 取消 1701-01 时，连带打断了 BrainStorm 01/02、Memory、质量评估的当前轮次。教训：只想停自己的子任务时，逐个停，不用 all。
- 第一版给用户的总结用了英文，已改发中文。教训：发用户前检查语言。

## 新用到的 skills / 工具
- firecrawl-cli / firecrawl-search / firecrawl-scrape（FIRECRAWL_API_KEY）
- SearXNG、RSSHub（本地服务，无密钥）
- SkillHub 接口、GitHub API、curl_cffi、MarkItDown

## 可优化点
- 每轮开搜前自动跑 firecrawl --status 并检查小红书登录态，写进 plan 文件。
- Step 0 业内标准缓存（standards/<domain>.md）尽快落地模板。
- 知乎/B站被拦的替代方案（字幕方案、Tavily key、Playwright MCP）待用户决定。

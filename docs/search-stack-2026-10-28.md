# Searcher 搜索栈评估（2026-10-28，UTC+8）
数据来源：GitHub API 于 2026-10-28 14:10 实时拉取；冒烟测试在 box 上实际运行。环境：/workspace/learning-loop/.venv-search

## Firecrawl
- 已安装的连接器中找不到 Firecrawl（GetDynamicTools 匹配 "firecrawl" 结果为 0）。目前只有 skills（firecrawl-cli/search/scrape…），没有 MCP。
- 已执行 `npm i -g firecrawl-cli`，版本 v1.23.3。`firecrawl --status` 显示 Not authenticated。
- 免 key 的 scrape 被拒，原因是 box 出口 IP 被判定为 VPN/代理，必须使用 API key。因此**搜索和抓取都还没有跑通**。
- 解决办法：用户在 firecrawl.dev 注册拿到 key（免费 1000 credits），通过 `firecrawl login` 登录或设置 FIRECRAWL_API_KEY；也可以在 Grok Bot 里把 Firecrawl 连接器装好并完成授权。

## 10 个仓库（排序按对我们的价值）
| # | 工具 | 链接 | Stars | License / 最近 push | box 可用？测试结果 | 建议角色 |
|---|---|---|---|---|---|---|
| 1 | Crawl4AI | github.com/unclecode/crawl4ai | 86,423 | Apache-2.0 / 10-26 | ✅ 0.9.5 + playwright chromium。阮一峰博客 2570 字符 md，react.dev（JS 站点）18008 字符 md | 主力本地抓取，包括 JS 页面 |
| 2 | curl-impersonate → 实际用 curl_cffi | github.com/lwthiker/curl-impersonate（7,160，MIT，最后 push 2024-07，原仓库已停更）；维护中的 fork 和 Python 绑定是 github.com/lexiforest/curl_cffi（6,787，MIT，10-27） | — | — | ✅ curl_cffi 0.17：36kr 200，阮一峰 200，小红书 explore 200（168KB，内容多为 JS 壳），知乎 403，B站视频页 412 | 轻量快速抓取的第一跳 |
| 3 | MarkItDown | github.com/microsoft/markitdown | 192,610 | MIT / 10-23 | ✅ 0.1.9，URL→md 正常（2780 字符） | 把 PDF/DOCX/HTML 转成 md |
| 4 | Scrapling | github.com/D4Vinci/Scrapling | 90,096 | BSD-3 / 10-27 | ✅ 0.5，需要装 `scrapling[fetchers]`（只装基础包会缺 browserforge）。Fetcher 抓阮一峰返回 200，CSS 选择器能取到标题 | 需要选择器、自适应解析时用 |
| 5 | Firecrawl | github.com/firecrawl/firecrawl | 196,158 | AGPL-3.0 / 10-28 | ⚠️ CLI 已装，缺 key（见上） | 托管搜索+抓取，有 key 后作为首选 |
| 6 | browser-use | github.com/browser-use/browser-use | 119,338 | MIT / 10-27 | 未测（需要 LLM key） | 多步交互 / 需要登录的 agent 流程 |
| 7 | Scrapy | github.com/scrapy/scrapy | 65,081 | BSD-3 / 10-27 | 未测 | 大批量定期爬取，现阶段用不上 |
| 8 | Crawlee | github.com/apify/crawlee | 26,279 | Apache-2.0 / 10-28 | 未测（Node 项目，另有 crawlee-python） | 和 Scrapy 二选一 |
| 9 | AutoScraper | github.com/alirezamika/autoscraper | 8,064 | MIT / 2026-07 | 未测 | 价值低 |
| 10 | scrcpy | github.com/Genymobile/scrcpy | 153,346 | Apache-2.0 / 10-26 | ❌ 没有 Android 设备，不适用 | 不用 |

## 扩展选项（链接已验证返回 200）
| 工具 | 链接 | 说明 / 测试 |
|---|---|---|
| Jina Reader | jina.ai/reader；github.com/jina-ai/reader（12,201，Apache-2.0） | ✅ 免 key 的 `r.jina.ai/<url>` 抓阮一峰 200。知乎返回"安全验证"页，B站 403（匿名访问被限）。`s.jina.ai` 搜索接口返回 401，需要 key |
| SearXNG | github.com/searxng/searxng（38,934，AGPL-3.0）；docs.searxng.org | 自托管的元搜索引擎，可以作为免费的搜索层。未部署 |
| Tavily | tavily.com；tavily-ai/tavily-python（1,422） | 面向 agent 的搜索 API，需要 key。未测 |
| Exa | exa.ai；exa-labs/exa-py（235） | 语义搜索 API，需要 key。未测 |
| MediaCrawler | github.com/NanmiCoder/MediaCrawler（68,787，license 为 NOASSERTION，仓库声明仅限学习用途、禁止商用） | 小红书/B站/知乎等平台，需要扫码登录。未测。ToS 风险高，只建议在用户本人账号下少量阅读时使用 |

## 中文平台可读性（匿名，box 出口）
- 小红书：curl_cffi 返回 200，但拿到的是 JS 壳页面，正文需要浏览器渲染或登录（本次未验证）。
- 知乎：curl_cffi 403，Jina 返回安全验证页 ❌
- B站视频页：curl_cffi 412，Jina 403 ❌（B站开放 API 未测）
- 36kr / 阮一峰等普通站点：✅

## 推荐搜索栈
1. **发现（搜索）**：先用现有的 WebSearch / firecrawl-search。有 Firecrawl key 后，用 `firecrawl search --scrape` 一步完成搜索加正文抓取。免费备选是自托管 SearXNG，或 Tavily/Exa（都需要 key）。
2. **读单页**：先 curl_cffi 加 MarkItDown（最快、零成本）。失败或内容太短时用 Jina `r.jina.ai`，再不行用 Crawl4AI（本地 Chromium 渲染 JS），最后用 Firecrawl scrape。
3. **结构化提取**：Scrapling 的选择器，或 Crawl4AI 的 schema 提取。有 key 后也可以用 firecrawl agent。
4. **交互 / 登录**：box 浏览器子代理，或 browser-use / firecrawl interact。
5. **中文封闭平台（小红书/知乎/B站）**：走 box 浏览器，由用户本人登录后人工节奏阅读。MediaCrawler 只作为最后选项，并且需要用户明确同意。
6. **原则**：只读公开页面，遵守 robots/ToS，限速；不做绕过验证码或登录墙的事。

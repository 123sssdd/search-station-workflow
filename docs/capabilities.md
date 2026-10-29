# 情报站能力矩阵草稿（优化规划师，2026-10-29，来源 profiles/*.md 基线）
用途：情报站各 bot 能力矩阵草稿（已去除账号和密钥）。

| bot | 角色 | 写入权限（唯一写入） | 主要 skills / 工具 | 定时任务 | 中期规划 |
|---|---|---|---|---|---|
| BrainStorm 01 | 主持例会、单号日开轮、起草指令 | — | brainstorming、grill-me、writing-plans、planning-with-files、leader；gh | 00:00 例会 | v2.1 实测迭代、roadmap、健康检查和 capabilities |
| Brainstorm 02 | 双号日开轮、单号日复核、代拍板 | — | brainstorming、grill-me、leader、planning-with-files、verification-before-completion、export-bot-template | 00:40 兜底 | 开轮/复核 checklist 沉淀为 skill |
| Searcher | 搜索与链接核实 | search 证据文件 | Firecrawl、SearXNG、curl_cffi+MarkItDown、Jina、Crawl4AI、RSSHub、SkillHub/GitHub API、小红书（只读低频） | 00:40 兜底 | standards 缓存、credits 三档、健康检查脚本 |
| 质量评估 | 初筛、浅评、深评、抽检，复核 standards | eval 证据文件 | Shell 核验、WebFetch、Firecrawl、GitHub/Notion 只读 | 00:40 兜底 | 评估 skill、standards 复核清单 |
| Memory | 归档与同步 | manifest.json、Notion 四库、CHANGELOG | gh、Notion 写、build_round3.py、knowledge-capture | 00:40 兜底 | manifest 构建、校验、同步脚本化 |
| Todos | 待办与每日清单 | Notion Todos 库 | Notion、todo-management、leader、spec-to-implementation | 00:40 兜底 | 清单流程 skill、派发回执 100% |
| 优化规划师 | 优化提案、评审、路线图合并 | decisions/ 方案文件 | Shell/Read、routines、Notion/GitHub 只读 | 00:40 兜底 | 档位校准、开源化评审、roadmap 周合并 |
| 手绘风技术配图 | 架构/流程图、README 图 | diagrams/ | project-diagram-studio、Python+cairosvg、Excalidraw 连接器 | 00:40 兜底 | 连接器出图、图标集、绘图脚本模板 |
| Github 管家 | GitHub 事务、开源贡献规划 | —（写操作均为 B 类） | gh（只读约定）、GitHub 连接器只读 | 例会成员 | 开源贡献候选与进展 |

## 重复与缺口
- 重复：leader、planning-with-files 在 01、02、Todos 都有，用途不同，可以保留。
- 缺口：①开轮健康检查脚本；②standards/ 首批文件；③credits 数据仅 1 个点；④manifest 构建缺 url 可达性校验（今日项 09）；⑤服务掉线无自动拉起（自启属 B 类）；⑥配图 redskill 不可用。

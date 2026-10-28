# Memory 今日复盘（2026-10-28）

## 进度
- 担任 Sketchmind manifest.json 唯一写入者；已推送 51b5bf6（2026-10-27，7 个 skill 标记 applied）与 cc7d7f4（今日，搜索栈轮次 20261028-1606-02，52 条、入选 8 项）。
- 搭建 Notion「学习中枢」：工作记录 / 轮次 / 沉淀条目 / Decisions 四库，并与 Todos 库建立关联。
- 首次全量同步 15:32：轮次 2、沉淀条目 25，失败 0；第二次同步 16:20：轮次 +1、沉淀条目 +52，失败 0。
- Decisions 写入 dec-20261028-01～09（07 指令 v2.1/搜索执行方案 v1、08 例会汇报定稿、09 Firecrawl 首选搜索栈）。v3 指令待用户确认，未归档。
- 已建每日 00:40 兜底定时任务，今晚首次运行。
- 轮次 20261028-1627-02 按用户决定不存档（未写 manifest、未同步）。

## 问题
- priority=false 的消息没有唤醒我，早期归档漏记，事后补录。
- Notion relation 需要裸 UUID，传 collection:// 会失败。
- 把 todos_spawned 字段直接替换，而不是按规则改名为 _废弃_（违规；库为空，无数据损失，已报告）。
- raw_json 写纯 JSON 被拒，改用「json:」前缀。
- 沉淀条目库 type/tags 缺选项导致 400，先扩展选项、后补记 Decisions（应先记 Decisions 再改 schema）。
- 交接后 Searcher 又改了源文件，本地提交 02e9ed9 只能按新文件重建为 cc7d7f4。
- Searcher 误取消了我的工作（无影响）。
- 推送批准必须来自用户本人原话（转述需含明确放行语）。
- 条目 -37、-50 的 url 末尾混入中文说明，待下次改 manifest 时清理。

## 经验
- 先确认 search/eval 交接文件齐全再写 manifest；推送前核对源文件是否有改动。
- 批量写 Notion 前先 fetch schema，限速 ≤3 次/秒，失败重试。
- 任何 schema 变更先落 Decisions，再动手。

## skills与工具
- gh CLI（123sssdd，repo 权限）+ 本地仓库 /workspace/learning-hub。
- user-Notion MCP（fetch / create-pages / update）；routines（建 00:40 兜底任务）。
- 构建脚本 /workspace/build_round3.py。

## 可优化点
- 交接文件在推送前冻结（记录 hash/版本号），改动需重新交接。
- 批量建页前做 select 选项预检，缺项先走 Decisions 再扩展。
- manifest 生成器加入 url 校验（拦截非 URL 字符）。
- 把 /workspace/build_round3.py 泛化为通用的轮次入库脚本。
- 归档通知类消息统一要求 priority=true，或补充唤醒规则。

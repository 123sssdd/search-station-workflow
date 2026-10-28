# Notion 学习中枢 五库定稿（草案，待用户拍板）2026-10-28
来源：优化规划师合并版（含 02、Todos 意见）
1. 工作记录：日期×bot 一行，log_key=<YYYYMMDD>-<bot>；date/bot/round_id(→轮次)/summary 要点/decisions(→Decisions)/todos_spawned(→Todos)/links/类型(日常/周复盘)。仅 Memory 写，写前脱敏。
2. Todos：标题/状态(待办/进行中/待用户决定/阻塞/已完成/已取消)/P0-P2/截止日/计划日/来源/来源链接/来源记录(→工作记录)/负责方/领域标签/预计耗时/备注决策选项/完成日/关联沉淀；todo_id=todo-<YYYYMMDD>-<序号>。仅 Todos 写。视图：今日/待用户决定/看板/本周复盘/逾期。
3a. 沉淀条目：与 manifest items 1:1 同名（id→manifest_id 唯一键, title,url,type,source,category,date,summary,quality,relevance,score,round(→轮次),reason,read,applied,effect,notes,tags）+content_hash,synced_at,archived,raw_json。
3b. 轮次：manifest_id(rounds.id),date,topic,picked(→沉淀条目),content_hash,synced_at。
   同步：manifest 推送成功后按 manifest_id upsert，hash 不变跳过，删除仅标 archived，只读镜像不反写，只改属性不动正文，≤3 次/秒。仅 Memory 写。
4. Decisions：decision_id=dec-<YYYYMMDD>-<序号>,日期,拍板人,内容,影响bot,状态(生效/废止),取代(自关联)。仅 Memory 写。
扩展：字段只加不删（弃用改名 _废弃_xxx），新类型加 select 选项，去重键格式不改，结构变更先记 Decisions，顶部 schema 版本说明。
脱敏：只记要点；正则替换密钥前缀/Bearer/key=token=password=cookie=SESSDATA=/JWT/私钥/高熵串；环境变量只写名；个人信息打码；拿不准不写；误写立即删并 priority 通知主 bot。
建库顺序：Decisions→轮次→沉淀条目→工作记录→Todos。
02 复核（15:24）：认可。补充：schema 说明写明 manifest.id = manifest_id；同步前先比对 manifest 顶层 updatedAt 整体跳过；Decisions 记一条「Todos 库写入方是 Todos」；Todos 指令后续写明 Notion 为主库、本地 skill 存储仅备份（并入统一更新指令步骤）。

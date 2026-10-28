# Notion「学习中枢」五库方案（草案，待用户拍板，未建库）
作者：优化规划师｜2026-10-28 15:20 UTC+8｜合并了 Brainstorm 02 的意见（15:15，经 01 转交）和 Todos 的需求

## 库清单
1. 工作记录：每个「日期×bot」一行。log_key=<YYYYMMDD>-<bot>，同一天同一个 bot 再写入时追加到 summary，不新建行。
   字段：标题、date、bot、round_id(→轮次)、summary、decisions(→Decisions)、todos_spawned(→Todos)、links、类型(日常/周复盘)、log_key
2. Todos：完全采用 Todos 提的字段，另加 todo_id=todo-<YYYYMMDD>-<序号>；完成日由 Todos 在把状态改为已完成时一并写入。
   视图：今日 / 待用户决定 / 按状态的看板 / 本周复盘 / 逾期
3a. 沉淀条目：和 manifest 的 items 字段同名一一对应，id 对应 manifest_id（唯一键）；另加 content_hash、synced_at、archived、raw_json
3b. 轮次：manifest_id(rounds.id)、date、topic、picked(→沉淀条目)、content_hash、synced_at
4. Decisions：decision_id=dec-<YYYYMMDD>-<序号>、日期、拍板人、内容、影响的 bot、状态(生效/废止)、取代了哪条决定(自关联)

## 写入者
Todos 库只由 Todos 写；其余四个库只由 Memory 写。周复盘由 Todos 发给 Memory，Memory 写进工作记录（类型选「周复盘」）。

## 同步（3a/3b）
manifest 推送成功后，按 manifest_id 做更新或插入；content_hash 没变就跳过；manifest 里删掉的条目只标记 archived，不物理删除；只做镜像，不写回 manifest；同步只更新字段，不动页面正文；写入不超过每秒 3 次。

## 扩展
字段只加不删，不用的改名为「_废弃_xxx」；新类型只加 select 选项；去重键格式永远不改；结构变更先写进 Decisions 再动手。

## 脱敏
只记要点；密钥前缀、token、cookie、密码、JWT、私钥、长度 ≥32 的高熵字符串都替换成 [REDACTED]；环境变量只写名字；邮箱、手机号、地址、证件号打码；拿不准的不写；发现误写立即删除并通知主 bot。

建库顺序：4 → 3b → 3a → 1 → 2

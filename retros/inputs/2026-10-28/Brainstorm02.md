# Brainstorm 02 今日复盘 2026-10-28

## 进度
- 评审：bot-instructions v2（7 条全部采纳）、每日会议格式（3 条必改 + 第 7 条采纳）、搜索方案 v2.1（2 处阻断：评分制 5 分/10 分统一、Firecrawl 额度预算未定义，已修后批准）、Notion 设计（拆分条目库/轮次库、manifest_id+content_hash upsert、只读镜像、Memory 单写）。
- 执行：todo 类 skill 检索→评估→安装 6 个（leader、planning-with-files、todo-management、todo-tracker 落 workflows；spec-to-implementation、knowledge-capture 走 Notion 官方插件）；补装静态 sqlite3 并冒烟测试。
- 生成自身分享模板草稿 + brainstorm-getting-started skill（待用户确认发布）。
- 建 00:40 兜底 routine。

## 问题
- 「02 没参与」误会：我的措辞把"评审"与"执行"混在一起，用户读成未参与。规则：
  a. 汇报时区分「评审过」与「执行过」，各列产出路径；
  b. 评审结论落 decisions/ 并写入自己 journal；
  c. 给用户的消息一律中文（曾发过一份英文报告，已重发）；
  d. 消息只带路径+摘要，正文落文件。
- clawhub 任意路径返回 200，不能用 HTTP 状态验链，需走 API。
- planning-with-files 默认分支是 master，main 链接 404。
- 模板文案初版为英文。
- Searcher 误取消我的回合（评审已落盘，无损失）。

## 经验
- 验链要看内容/API，不只看状态码。
- 先落文件再发消息，避免回合中断丢结论。

## skills / 工具
- export-bot-template、CreateBotShareJson、UpdateSkill、静态 sqlite-tools 3.50.4（~/.local/bin）。

## 可优化点
- 统一评分刻度写进指令正文。
- 给 Firecrawl 等付费工具设每轮额度上限。
- 汇报模板固定「评审/执行/待定」三栏，防误会。
- 方案文件就绪时发 priority 通知，减少轮询。

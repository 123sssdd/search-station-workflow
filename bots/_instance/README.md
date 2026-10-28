# bots/_instance/ · 实例专属（本地，默认不入库）

本目录在**本机**保存情报站实例实际指令备份，通常含：

- 真实 Grok Bot / agent UUID
- 真实 Notion 学习中枢 / Todos 库页面 URL

`.gitignore` 已忽略本目录下除本 README 外的文件，因此 **push 到公开仓库的树里不会出现真实 UUID**。  
请在本机自行放置：`bot-instructions-v3.md`、`bot-instructions.md`、各角色 `01-…`–`07-…` 等。

公开克隆请使用仓库根下已脱敏的：

- `bots/bot-instructions-v3.md`
- `templates/bot-instructions-v3.md`
- `templates/bots/<role>.md`

并把 `<AGENT_ID_*>`、`<NOTION_HUB_URL>`、`<NOTION_TODOS_DB_URL>` 换成你自己的值。

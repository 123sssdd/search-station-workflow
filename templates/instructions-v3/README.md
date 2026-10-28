# templates/instructions-v3/ · 现行 v3 纯净粘贴版

给使用者**直接粘贴到各 bot 指令框**的完整指令（连贯正文，无版本增量编号）。

## 与档案版的区别

| 文件 | 用途 |
|------|------|
| **本目录** `templates/instructions-v3/` | 纯净粘贴版：去掉 `【v3-n】` /「v1 保留」等增量话术，角色+公共条款分文件，便于复制 |
| `bots/bot-instructions-v3.md`、`templates/bot-instructions-v3.md` | 档案/对照稿：保留条款编号与决策溯源，方便 diff 与 CHANGELOG |

两套内容语义一致；改指令时先改生效源，再同步本目录与档案版。

## 如何粘贴

1. 打开本目录对应角色文件（如 `01-brainstorm-01.md`），**全文复制**。
2. 再打开 `00-common.md`，全文接在后面。
3. 若角色是 **01 / 02 / Searcher / 质量评估**，再接上 `90-search-plan.md`。
4. 把占位符换成你的实例值（见下表）。
5. 粘贴到该 bot 的系统/自定义指令框并保存。

## 占位符

| 占位符 | 含义 |
|--------|------|
| `<WORKSPACE>` | 工作区根路径（本实例常用 `/workspace/learning-loop`） |
| `<AGENT_ID_01>` … `<AGENT_ID_TODOS>` | 各 bot 的 agent UUID |
| `<NOTION_HUB_URL>` | Notion 学习中枢页 |
| `<NOTION_TODOS_DB_URL>` | Notion Todos 库 |

## 文件一览

```
README.md
00-common.md          公共条款 + 完成即通知（每个 bot 都要附）
01-brainstorm-01.md
02-brainstorm-02.md
03-searcher.md
04-quality-eval.md
05-memory.md
06-optimizer.md
07-diagram.md
08-todos.md
90-search-plan.md     搜索方案（仅 01/02/Searcher/质量评估）
```

# templates/instructions-v3/ · 复刻用纯净最终版（v3）

**给谁用：** 想复刻这套情报站的人。拿最终可运行正文即可，不需要条款编号和改动日期。

**本站自己人 / 各 bot：** 继续用带 `【v3-n】` 的档案版（见下表），方便对变更、写 CHANGELOG、例会复盘。

## 两套怎么分工

| 版本 | 路径 | 受众 | 特点 |
|------|------|------|------|
| **纯净最终版（本目录）** | `templates/instructions-v3/` | 复刻者、对外文档 | 连贯全文，无增量编号 |
| **档案版（带【v3-n】）** | `bots/bot-instructions-v3.md`、`templates/bot-instructions-v3.md`；本站生效源 `/workspace/learning-loop/bot-instructions.md` | 本站 bot 与维护者 | 保留条款编号与生效时间，便于追溯 |

两套语义一致。本站改指令：先改档案/生效源 → 你确认 → 再同步生成/更新本目录纯净版。

## 复刻者如何粘贴

1. 打开本目录对应角色文件（如 `01-brainstorm-01.md`），**全文复制**。
2. 再打开 `00-common.md`，全文接在后面。
3. 若角色是 **01 / 02 / Searcher / 质量评估**，再接上 `90-search-plan.md`。
4. 把占位符换成你的实例值（见下表）。
5. 粘贴到该 bot 的系统/自定义指令框并保存。

## 占位符

| 占位符 | 含义 |
|--------|------|
| `<WORKSPACE>` | 工作区根路径（示例：`/workspace/learning-loop`） |
| `<AGENT_ID_01>` … `<AGENT_ID_TODOS>` | 各 bot 的 agent id |
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

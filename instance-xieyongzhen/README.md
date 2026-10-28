# instance-xieyongzhen/ · 本站（xieyongzhen）自用指令

这里是**本情报站自己用**的指令档案，保留【v3-n】条款编号与生效时间。想复刻这套配置的人请用 `templates/instructions-v3/`（纯净版，语义一致、无编号）。

## 生效源与同步
- 真正生效的是本机 `/workspace/learning-loop/bot-instructions.md`；本目录是它的副本。
- **Notion ID 有意公开**（用户 2026-10-28 决定）：换 Grok 账号后 Notion 不变。全部资源见 [`notion-ids.md`](notion-ids.md)。
- **Agent UUID 只放本机**：本目录写成 `<AGENT_ID_*>` 占位符，换账号后会变。真实值在 `_instance/`（gitignored）。

## 换 Grok 账号后
1. 在新账号重建 8 个 bot，在每个 bot 的设置/详情里拿到新的 agent id（或在任一 bot 里列出自己的 bots 查看）。
2. 更新 `_instance/01-…08-*.md` 里的通讯录和 owner id（把旧 UUID 全部替换成新值），或者从本目录文件开始，把 `<AGENT_ID_*>` 填上新值。
3. 把拼好的指令粘贴给各 bot；Notion 链接不用改。新账号要重新连接 Notion 连接器，并授权访问「学习中枢」。

## 文件
| 文件 | 说明 |
|------|------|
| `bot-instructions-v3-annotated.md` | 单文件总档（v3 = v2 + v2.1 + v2.2 + 【v3-n】），对照 diff、搜编号用 |
| `00-common.md` | 公共条款 + v2.2 完成即通知用户（每个 bot 都附） |
| `01-brainstorm-01.md` … `08-todos.md` | 各 bot：角色正文（v1 铁律）+ v3 角色增量 |
| `90-search-plan.md` | v2.1 搜索执行方案（01/02/Searcher/质量评估附） |
| `notion-ids.md` | Notion 资源清单（名称、用途、URL、data source）单一参考 |
| `sites-to-login.md` | 需要登录的站点清单（无密钥） |
| `_instance/` | 含真实 agent UUID 的版本，不入库 |

粘贴顺序：角色文件 → `00-common.md` →（01/02/Searcher/质量评估）`90-search-plan.md`。本机可直接用 `_instance/<角色>.md`，已拼好。

## 【v3-n】编号怎么对应
- 编号来自 `decisions/optimizations-20261028/01-final-1826.md` 的提案序号；19:28 用户修订见 `decisions/user-decisions-20261028/01-final-1928.md`（如【v3-14b】、v3-3 终审默认全面评审）。
- 每条修订在根目录 `CHANGELOG.md` 有对应条目（日期、版本、条款、来源决策、影响角色），由 Memory 唯一写入。
- 例会/提案里用编号指代条款（如「改 v3-4」）；用户批准后：01 改生效源与本目录 → Memory 记 CHANGELOG 并推送 → 重新生成 `templates/instructions-v3/` 纯净版。

历史版本：`archive/v2.1/`、`archive/bot-instructions-v3-draft.md`。

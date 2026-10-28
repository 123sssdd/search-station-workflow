# adapters/platform/grok-bot

> stub：Grok Bot / Cursor Agent 平台差异映射。角色模板保持平台无关；此处说明消息、定时、优先级如何落地。

## 输入 / 输出
- 输入：角色模板中的「需对方处理的通知」、定时窗口（例会 00:00、兜底 00:40）、文件路径约定
- 输出：平台消息（含 priority 映射）、routines/定时任务、子 agent 派发

## 环境变量名（不写值）
- （平台登录与连接器由宿主管理；仓库内不出现 token）
- 可选：与 station 相同的非密钥变量名（`SEARXNG_URL`、`RSSHUB_URL`、`TODO_DB`、`NOTION_HUB_URL`）

## credits_ref_limit
- n/a（平台额度不在本适配器计量；Firecrawl 等见 search 适配器）

## 映射约定
| 抽象 | grok-bot 实现 |
|------|----------------|
| 需对方处理的通知 | `priority:true` 消息 |
| 仅知会 | `priority:false` |
| 定时例会 / 兜底 | 平台 routines（00:00 / 00:40 Asia/Shanghai） |
| agent_id | `config/station.yaml` 的 `roles.*.agent_id` 占位符 |

## 备注
- 不在此文件写入真实 agent UUID；公开树使用 `<AGENT_ID_*>`。

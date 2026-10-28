# schemas/

JSON Schema（Draft 2020-12）定义情报站关键产物字段。Markdown 证据文件仍是日常载体；本目录供校验脚本与适配器对齐字段。

| 文件 | 对应产物 |
|------|----------|
| `manifest.schema.json` | Sketchmind 根目录 `manifest.json`（`url` 必须为可核验的 `http(s)://`） |
| `plan.schema.json` | `rounds/plan-<id>.md` 结构化字段 |
| `search.schema.json` | `rounds/search-<id>.md` |
| `eval.schema.json` | `rounds/eval-<id>.md`（5 分制） |
| `retro.schema.json` | `retros/<YYYY-MM-DD>.md` |
| `daily-report.schema.json` | `meetings/<YYYYMMDD>/<bot>.md` 九项日报 |
| `decision-record.schema.json` | `decisions/<主题>/*.md` |

校验：`python3 scripts/validate-schemas.py [path...]`（无参数时校验 `sketchmind-template/manifest.json`）。

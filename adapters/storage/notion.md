# adapters/storage/notion

> stub。唯一真源仍是仓库 `manifest.json` + Markdown；本适配器只做单向镜像。

## 输入 / 输出
- mirror upsert by manifest_id + content_hash; delete→archived

## 环境变量名（不写值）
- `NOTION_HUB_URL`

## credits_ref_limit
- n/a（存储镜像）

## 备注
- Memory 写四库；Todos 不走本适配器
- 写入速率参考：`storage.notion.write_rate_per_sec_max`（默认 3）。

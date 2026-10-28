# adapters/storage/none

> stub。唯一真源仍是仓库 `manifest.json` + Markdown；本适配器只做单向镜像。

## 输入 / 输出
- no-op mirror

## 环境变量名（不写值）
- （无）

## credits_ref_limit
- n/a（存储镜像）

## 备注
- 仅真源 manifest + 仓库 Markdown
- 写入速率参考：`storage.notion.write_rate_per_sec_max`（默认 3）。

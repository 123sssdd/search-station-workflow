# adapters/storage/local-md

> stub。唯一真源仍是仓库 `manifest.json` + Markdown；本适配器只做单向镜像。

## 输入 / 输出
- one .md per item; front-matter + wikilinks

## 环境变量名（不写值）
- （无）

## credits_ref_limit
- n/a（存储镜像）

## 备注
- 可选镜像
- 写入速率参考：`storage.notion.write_rate_per_sec_max`（默认 3）。

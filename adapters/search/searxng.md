# adapters/search/searxng

> stub：约定与环境变量名；未实现可执行代码。链顺序见 `config/backends.yaml` / `config/station.yaml.example` 的 `search.chain_file`。

## 元信息
- kind: `search`
- credits_ref_limit: credits_ref_limit: n/a（本地）

## 输入
- query, language?=zh-CN, limit?

## 输出
- list[{title,url,source,date,snippet}]

## 前置检查
- GET $SEARXNG_URL/search?q=ping&format=json

## 环境变量名（不写值）
- `SEARXNG_URL`
- `SEARXNG_SECRET`

## 降级
- 失败时按 `backends.yaml` 的 `chain` 顺序写进 `plan-<id>.md` 降级记录后切下一后端。

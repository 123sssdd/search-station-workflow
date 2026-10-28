# adapters/search/firecrawl

> stub：约定与环境变量名；未实现可执行代码。链顺序见 `config/backends.yaml` / `config/station.yaml.example` 的 `search.chain_file`。

## 元信息
- kind: `search+scrape`
- credits_ref_limit: A/B/C 参考上限见 backends.yaml credits_ref_limit（待补数值，不阻断）

## 输入
- query, time_range?, limit?

## 输出
- list[{title,url,source,date,snippet,signals}]

## 前置检查
- firecrawl --status

## 环境变量名（不写值）
- `FIRECRAWL_API_KEY`

## 降级
- 失败时按 `backends.yaml` 的 `chain` 顺序写进 `plan-<id>.md` 降级记录后切下一后端。

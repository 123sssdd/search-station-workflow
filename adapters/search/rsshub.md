# adapters/search/rsshub

> stub：约定与环境变量名；未实现可执行代码。链顺序见 `config/backends.yaml` / `config/station.yaml.example` 的 `search.chain_file`。

## 元信息
- kind: `feed`
- credits_ref_limit: credits_ref_limit: n/a；本实例监听所有网卡（用户 2026-10-28 19:28 维持）

## 输入
- route (公开榜单/热榜)

## 输出
- feed items[{title,url,date,summary}]

## 前置检查
- GET $RSSHUB_URL/

## 环境变量名（不写值）
- `RSSHUB_URL`

## 降级
- 失败时按 `backends.yaml` 的 `chain` 顺序写进 `plan-<id>.md` 降级记录后切下一后端。

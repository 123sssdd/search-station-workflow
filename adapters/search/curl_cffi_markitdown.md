# adapters/search/curl_cffi_markitdown

> stub：约定与环境变量名；未实现可执行代码。链顺序见 `config/backends.yaml` / `config/station.yaml.example` 的 `search.chain_file`。

## 元信息
- kind: `read_page`
- credits_ref_limit: credits_ref_limit: n/a

## 输入
- url

## 输出
- {url, markdown, status}

## 前置检查
- python -c 'import curl_cffi, markitdown'

## 环境变量名（不写值）
- （无）

## 降级
- 失败时按 `backends.yaml` 的 `chain` 顺序写进 `plan-<id>.md` 降级记录后切下一后端。

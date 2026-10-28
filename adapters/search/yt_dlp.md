# adapters/search/yt_dlp

> stub：约定与环境变量名；未实现可执行代码。链顺序见 `config/backends.yaml` / `config/station.yaml.example` 的 `search.chain_file`。

## 元信息
- kind: `video_meta`
- credits_ref_limit: credits_ref_limit: n/a；不用 cookie

## 输入
- video_url

## 输出
- {title,url,meta,subtitles?}

## 前置检查
- enabled:false（B站 412）；B站字幕暂不处理（用户 2026-10-28 19:28）

## 环境变量名（不写值）
- （无）

## 降级
- 失败时按 `backends.yaml` 的 `chain` 顺序写进 `plan-<id>.md` 降级记录后切下一后端。

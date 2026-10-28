# rounds/ — 每轮交接凭证与认领锁
- `search-<YYYY-MM-DD>.md`：Searcher 产出的搜索结果（必需）。
- `eval-<YYYY-MM-DD>.md`：质量评估产出的打分（必需）。两份齐全主 bot 才能拍板、通知 Memory 写仓库；缺任一份只算“草案”。
- `<id>.lock`：开新一轮前写入 `owner=<bot>` 与 `time=<ISO 时间>`；看到未过期的锁另一方不接手。锁 **6 小时** 无更新即视为过期，可接管。

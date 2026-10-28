# rounds/ — 每轮交接凭证与认领锁

轮次 id：`<YYYYMMDD-HHMM>-<01|02>`（UTC+8），由开轮的主 bot 生成，后缀为 owner（01/02），写进每条派活消息。例：`20261028-1430-01`。

- `<轮次id>.lock`：开轮前写入 owner、开始时间、当前进度；每推进一步更新进度。看到未过期的锁另一方不接手。锁 **6 小时** 无更新即过期，接手方须先 priority:true 告知原 owner。
- `<轮次id>.done`：一轮结束后把 .lock 改名为 .done。
- `search-<轮次id>.md`：Searcher 产出（必需，注明是否用了 Firecrawl）。
- `eval-<轮次id>.md`：质量评估产出（必需）。两份齐全且另一主 bot 复核后才能发用户；缺任一份只算「草案」，Memory 不推送。

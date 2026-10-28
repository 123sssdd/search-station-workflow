# adapters/

可插拔适配器骨架（2026-10-28 P1：仅约定文档，无实现代码）。

| 目录 | 用途 | 配置入口 |
|------|------|----------|
| `search/` | 搜索/抓取后端（与 `config/backends.yaml` 链对齐） | `station.yaml` → `search.chain_file` |
| `storage/` | manifest 镜像（notion / local-md / obsidian / none） | `station.yaml` → `storage.mirror` |
| `tasks/` | 任务库（**不**由 manifest 派生） | `station.yaml` → `tasks.adapter` |
| `platform/` | 宿主平台差异（消息/定时/priority） | 角色模板 + 本目录 |

每个 stub 写明：输入输出、环境变量**名**、`credits_ref_limit` 占位。密钥值只出现在本机 `.env`（不入库）。

延后项（用户 2026-10-28 19:28，本轮不改运行时）：
- Tavily：暂不申请
- B站字幕：暂不处理（`yt_dlp` stub 保持 `enabled:false`）
- RSSHub：本实例继续监听所有网卡（不改 localhost-only）

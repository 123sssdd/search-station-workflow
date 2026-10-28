# Notion 资源 ID 清单（本站唯一参考）

> 有意公开：换 Grok 账号后 Notion 不变，各 bot 继续用这些链接。只有获授权的 Notion 集成/成员能读写，仅有链接打不开私有页面。
> 来源：2026-10-28 21:15（UTC+8）读取「学习中枢」页面得到的数据库列表。Notion relation 字段要用裸 UUID（data source id），不要带 `collection://` 前缀。

| 名称 | 用途 | 唯一写入方 | 页面 URL | data source |
|------|------|-----------|----------|-------------|
| 🧠 学习中枢 | 父页面：Schema v1、写入/同步/脱敏规则，下挂五库 | 只读（结构改动先记 Decisions） | https://app.notion.com/p/407d76611323819086f1f6c35f72ab7f | — |
| Decisions | 拍板记录 dec-<YYYYMMDD>-<序号> | Memory | https://app.notion.com/p/2000b02d12164c35ae5976dd11fb59fd | `collection://dac471bb-bd60-4ae3-8ba1-b5a75a1994dd` |
| 轮次 | manifest 轮次镜像（按 manifest_id upsert） | Memory | https://app.notion.com/p/23b5b9d3e45c4fd99891b6c9d38213a0 | `collection://4adb20ee-0c9f-4c1f-8cbe-fb2035e5cb9d` |
| 沉淀条目 | manifest 条目镜像 | Memory | https://app.notion.com/p/4dc92ecc17994db8a70c7a1c829938ca | `collection://6c79243e-1d99-4ca2-a564-1a0c5cdb1324` |
| 工作记录 | 每日×bot 一行（log_key=<YYYYMMDD>-<bot>）、每日清单、周复盘 | Memory | https://app.notion.com/p/c0c8b6c7e95f413d99cba21d7e1f2241 | `collection://9679aab7-9b62-4d11-a22e-3218f7b5ace3` |
| Todos | 待办与每日清单（状态为原生 status 类型） | Todos | https://app.notion.com/p/78895c6f295243adab9a17217c75f450 | `collection://0312e3e7-3dce-4746-ad2d-6a70076d7c38` |

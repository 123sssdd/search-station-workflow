# search-station-workflow · 情报站多 bot 学习闭环工作流

> 一套由 8 个协作 bot 组成的「情报站」工作流：围绕用户发来的主题做**搜索 → 评估 → 沉淀 → 看板/知识库**，每天 00:00 例会复盘并在夜间自主推进，白天由用户拍板关键决策。
> 本仓库是可复用的工作流套件（文档、角色模板、配置示例、决策记录、架构图），目标是让别人 clone 后改一份配置、贴几份角色指令就能搭起自己的情报站。

状态：2026-10-28 整理。当前生效指令版本为 **v2 + v2.1**；v3 为草案（`templates/bot-instructions-v3-draft.md`），**未生效，待用户确认**。

## 架构总览

![总架构](docs/diagrams/architecture.png)

![每日 00:00 例会与夜间推进](docs/diagrams/daily-meeting.png)

图的可编辑源文件：`docs/diagrams/*.excalidraw`（可导入 Excalidraw）、`*.svg`，生成脚本 `docs/diagrams/gen_*.py`（由「手绘风技术配图」bot 维护）。

一句话流程：
- **主循环**：用户发内容 → 当值主 bot（BrainStorm 01/02）发散关键词、发「搜索计划卡」 → Searcher 搜索并验链 → 质量评估打分 → 另一主 bot 复核 → 发排序给用户 → 用户挑选 → Memory 写 manifest 并同步 Notion。
- **复盘与自进化**：每日 00:00 例会 → retros/<日期>.md → 优化规划师出方案 → Brainstorm 02 评审 → BrainStorm 01 拍板 → 不改指令的改动夜间自主落实；改指令的标「B 类 / 待你决定」等用户确认。

## 快速开始

1. 读 [`docs/setup-from-scratch.md`](docs/setup-from-scratch.md)，按步骤在新账号建 8 个 bot。
2. 把 `templates/bots/<role>.md` 的指令粘到对应 bot（再把占位符换成你的实际值）。
3. 复制 `config/config.example.yaml`、`config/.env.example`，只在本地填真实值（`.env` 不进仓库）。
4. 连接 Notion 并建五库（schema 见 setup 文档）；部署 SearXNG 与 RSSHub；登录 Firecrawl CLI。
5. 每个 bot 建好 00:00 例会 / 00:40 兜底定时任务。
6. 用 `templates/evidence/` 的模板跑第一轮搜索。

## 目录

```
README.md                    本文件
CHANGELOG.md                 版本记录（v1 → v2 → v2.1 → v3 草案）
搭建总说明.md                  早期（v1）Sketchmind 学习循环搭建说明，保留
docs/
  workflow.md                角色分工、轮值、证据文件与锁、例会、搜索栈、Notion、看板
  setup-from-scratch.md      从零搭建步骤
  skills-and-tools.md        skills / MCP 连接器 / 本地服务 / CLI 清单（只写环境变量名）
  self-evolution.md          自进化机制（例会 → 复盘 → 提案 → 落实/待批）
  extensibility.md           可扩展性（角色、搜索后端、存储、配置、版本）
  design-tradeoffs.md        关键取舍及原因
  decisions/                 决策记录（脱敏副本，索引见 decisions/README.md）
  diagrams/                  架构图 png/svg/excalidraw 与生成脚本
  search-stack-2026-10-28.md 搜索栈评估（早期提交，保留）
  learning-workflow.*        v1 学习工作流图（保留）
templates/
  bots/<role>.md             8 个角色的通用指令模板 + _new-role-template.md
  bot-instructions-v3-draft.md   v3 指令草案（未生效）
  evidence/                  plan / search / eval 证据文件模板
  retro.md / daily-report.md / decision-record.md
config/
  config.example.yaml        集中配置示例（只写环境变量名）
  .env.example               环境变量名清单
  searxng-settings.example.yml
  backends.yaml              搜索后端与降级链
retros/2026-10-28.md         首日复盘（含各 bot 追加）；retros/inputs/2026-10-28/ 为各 bot 原始输入（脱敏）
bots/                        本实例的 v1 指令与 v2.1 现行指令（含实例专属 id，开源前需替换，见下）
decisions/2026-10-28.md      早期规则决定（保留）
rounds/                      每轮证据文件与锁的约定
skills/                      可直接拷贝的 skills
sketchmind-template/         Sketchmind 看板（GitHub Pages）模板
```

## 实例信息与开源注意

- 看板示例：https://123sssdd.github.io/Sketchmind/ （数据只来自仓库根目录 `manifest.json`）。
- `bots/` 下为本实例实际使用的指令，含 bot 内部 id 与私有路径；对外开源前应只保留 `templates/bots/`，或把 id 换成占位符（待用户决定）。
- 仓库中不含任何密钥、token、cookie；配置只写环境变量名。

## 许可

待补（由用户决定开源许可证）。

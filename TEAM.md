# 团队 AI 编程公约 v0.1

> 仓库：公积金智能客服（`gjj-kefu`）  
> 原则：**共享上下文 + 共享门禁 + 共享完成定义**；Agent 产品 / 模型品牌个人自选。

## 只统一这五件事（其它放开）

| # | 统一 | 怎么落地 | 放开 |
|---|------|----------|------|
| 1 | 规格目录 | 新需求先有 `docs/prd.md` / `docs/spec.md` / `docs/tasks.md`；延后想法进 `docs/backlog.md` | 用 Claude Code / Cursor / Codex / 纯手写 |
| 2 | 完成定义 | 对照当前 Spec 的 System Ready；至少 `python test_retrieve.py` 全绿 + 主路径或失败态可演示 | 本地编辑器、主题、个人 slash 别名 |
| 3 | 密钥与权限 | 密钥只读环境变量 `ZHIPU_API_KEY`；禁止进 Git；合并权在人 | 本地 MCP 清单、个人模型路由 |
| 4 | PR 模板 | 必须填「改动 / 风险 / 怎么测 / Agent 做了什么」——见 `.github/PULL_REQUEST_TEMPLATE.md` | 个人 commit 粒度习惯（仍建议三段式） |
| 5 | CI 门禁 | PR / push 跑检索测试 + 密钥扫描（`.github/workflows/ci.yml`） | 预览环境、额外 linter（有需要再加） |

## 协作节奏

```
Issue / 一句话需求
  → 规格 PR（人审规格，不审代码）
    → 实现 PR（Agent 可写，人审 diff + 跑主路径）
      → CI 绿
        → 合并
          → 短复盘（是否更新 Skill / 宪法 / TEAM.md）
```

**禁止**：在群里贴长聊天记录当需求。需求进仓库（Issue 或 `docs/`）。

## 给 Agent 的共享上下文（壳可换）

| 能力 | 本仓库落点 | 等价物（组员可换壳） |
|------|------------|----------------------|
| 项目宪法 | `CLAUDE.md` | `AGENTS.md` / `.cursorrules` / 系统提示 |
| 可复用动作 | `.claude/skills/*` | Cursor Skills / Prompt 包 / Slash Commands |
| 完成自检 | `/ready` | 对照 Spec Ready 清单手工跑 |
| 只读审查 | `.claude/agents/reviewer.md` | 另一会话扮演 reviewer，或人审 |
| 密钥围栏 | PreToolUse Hook 拦 `.env` | CI 密钥扫描 + `.gitignore` |

公约绑的是 **目录、清单、门禁**，不绑单一厂商。

## 如果组员不用你的 Agent 产品

仍须遵守公约的方式：

1. **规格**：人写也行，文件路径与验收用例表格式不变。  
2. **PR**：照模板填「Agent 做了什么」——若全手写，写 `无，人工实现`。  
3. **测试**：本地跑 `python test_retrieve.py`；CI 不依赖任何人的 IDE 插件。  
4. **密钥**：只设环境变量；不把 key 写进代码或聊天记录。  
5. **审查**：没有 reviewer Subagent 就用人审 + Ready 清单勾选。

换壳不换规矩：能合并的条件永远是 **规格在库、测试绿、人点合并**。

## 本阶段不做

- 强制全员同一 Agent / 同一模型  
- 无门禁的全自动合并（留给更后的课）  
- 为接 MCP 而接 MCP（见 `docs/backlog.md`）

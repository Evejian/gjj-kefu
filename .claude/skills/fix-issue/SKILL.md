---
name: fix-issue
description: 从 Issue（或 docs/issues/编号）走到失败测试→修复→PR。用户说 /fix-issue、修 issue、按工单修时使用。
---

# fix-issue：Issue → PR（自动化等级 1）

## 输入
Issue 编号或路径，例如：`0001`、`docs/issues/0001-tickets-corrupt.md`、GitHub `#12`。

## 步骤（必须按序，禁止跳步）

1. **读 Issue**  
   - 优先 `docs/issues/` 下对应文件；若给了 GitHub 号且网络可用，用 `gh issue view`。  
   - 提炼：现象、复现命令、期望。

2. **复现**  
   - 原样跑复现命令，保存完整报错。不复现不动手。

3. **最小失败测试**  
   - 新增或扩展测试，锁定坏行为（红）。  
   - 提交信息里写清对应 Issue。

4. **修复**  
   - 只改让该测试变绿的最少代码。不顺手重构。  
   - 不碰 `docs/wiki/04-landmines.md` 不敢动区，除非 Issue 明确要求且有表征掩护。

5. **门禁**  
   - 跑 `python scripts/gate_ready.py`（或全量测试列表）。  
   - **测试未全绿禁止声称完成、禁止开「已修好」PR。**

6. **开 PR（等级 1）**  
   - 按 `.github/PULL_REQUEST_TEMPLATE.md` 填写；标题带 Issue 号。  
   - 人点合并；Agent 不得自行合 main（本营不做等级 2/3）。

7. **审查**  
   - 可唤起 reviewer Subagent；把意见贴进 PR，等人决定。

## 输出给用户
- 复现证据（红）→ 修复点 → 门禁绿 → PR 链接（或本地分支名 + push 命令）
- 若中途修错：保留失败日志，再开一轮 debug-loop（算分）

## 禁止
- 没失败测试就改生产代码  
- 测试红仍写「已完成」  
- 自动合并 main / 自动部署生产  

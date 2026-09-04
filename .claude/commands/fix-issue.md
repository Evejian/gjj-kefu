对照 Issue 走完「复现→失败测试→修→门禁→PR」流水线（L8）。

1. 读参数中的 Issue（`docs/issues/` 或用户给出的编号）；无参数则列出 `docs/issues/` 待办。
2. 严格按 `.claude/skills/fix-issue/SKILL.md` 执行。
3. 最后必须跑 `python scripts/gate_ready.py`；未通过不得声称完成。
4. 输出：改了什么 / 为什么 / 怎么验证 / PR 或分支名。

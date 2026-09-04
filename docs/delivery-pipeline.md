# L8 · 端到端交付流水线（Issue → PR）

## 一句话
信号进仓库 → Agent 复现并补红测 → 修复 → 门禁绿 → 自动/半自动开 PR → **人合并**。

## 自动化分级（写进 TEAM.md）

| 级 | 允许 | 本营 |
|----|------|------|
| 0 | 只建议 patch，人复制 | 可用 |
| **1** | 自动开 PR，人合并 | **目标** |
| 2 | 预发自动部署 | 不做 |
| 3 | 生产自动部署 | 不做 |

## 本地可重复路径（无 GitHub 也能练）

1. 读 `docs/issues/0001-tickets-corrupt.md`
2. `python test_ticket_store.py`（修前应红）
3. 修 `ticket_store.py`
4. `python scripts/gate_ready.py`
5. 开分支 PR，人点合并

Cursor / Claude：`/fix-issue 0001` 或引用 fix-issue skill。

## 门禁

- `scripts/gate_ready.py`：测试红 = 禁止 Ready
- CI：PR 上再跑一遍（含 `test_ticket_store.py`）
- 合并权在人

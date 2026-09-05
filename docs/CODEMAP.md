# 仓库地图（CODEMAP）

FAQ → 检索 → 回答；Agent 值守；Issue→PR；按次计费 CLI SaaS；**结营复盘**。

## 关键入口

| 要做什么 | 命令 / 文件 |
|----------|-------------|
| 门禁 | `python scripts/gate_ready.py` |
| 商业闭环演示 | `python demo_saas.py` |
| 结营讲稿 | `python demo_wrap.py` / `docs/camp-retro.md` |
| Day14 PR 草稿 | `docs/pr-day14.md` |
| L4 试行一页 | `python demo_trial.py` / `docs/l4-trial.md` |
| 成本账本 | `python demo_cost.py` / `billing.cost_sum_cny` |
| 计费逻辑 | `billing.py` / `payment_mock.py` / `saas.py` |
| Agent | `demo_agent.py` |
| 修 Issue | `/fix-issue` + `docs/issues/` |

## 怎么跑

```
python scripts/gate_ready.py
python demo_saas.py && python demo_agent.py && python demo_wrap.py && python eval_run.py
```

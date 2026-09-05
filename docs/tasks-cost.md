# Tasks · 估算成本入账

## Task-01 规格先行（本日主证据）
本文件 + prd-cost + spec-cost。
验证：三份路径可指给同事。

## Task-02 红测 test_cost.py
覆盖 CS-01 ~ CS-04。
验证：先失败或同批交测。

## Task-03 billing / saas / demo_cost
`estimate_cost_cny`、`cost_sum_cny`；ask 把 mode 传入 consume；snapshot 带汇总。
验证：`python test_cost.py`；`python demo_cost.py`。

## Task-04 试行日志第 2 天；门禁；commit
验证：`docs/l4-trial.md` 日志日 2 已填；gate 含 test_cost。

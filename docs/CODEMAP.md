# 仓库地图（CODEMAP）

公积金智能客服：FAQ → 检索 top3 → 回答；Agent 值守；Issue→PR 流水线。

接手说明见 [`wiki/`](wiki/)。交付流水线见 [`delivery-pipeline.md`](delivery-pipeline.md)。

## 目录结构

```
gjj-kefu/
├── CLAUDE.md / TEAM.md / README.md / camp-goals.md
├── faq_store.py / faq_stats.py / retrieval.py / answer.py
├── agent.py / intent.py / auth.py / ratelimit.py / order_tool.py / ticket_store.py
├── demo_*.py / eval_run.py / scripts/gate_ready.py
├── test_*.py
├── data/users.json / data/orders.json
├── docs/wiki/ / docs/issues/ / docs/delivery-pipeline.md
├── docs/*-agent.md / docs/eval-set.jsonl / docs/escalation-policy.md
├── .github/ISSUE_TEMPLATE/ / workflows/ci.yml
└── .claude/skills/fix-issue / commands/fix-issue / ready
```

## 改动从哪下手

| 要改什么 | 入口 |
|---|---|
| 检索 / 打分 | test_characterization → retrieval.py |
| 工单容错 | test_ticket_store → ticket_store.py |
| Agent 值守 | agent.py + test_agent.py |
| 修 Issue | docs/issues/ + /fix-issue |
| 门禁 | scripts/gate_ready.py |

## 怎么跑

```
python scripts/gate_ready.py
python demo_main_path.py && python demo_agent.py && python eval_run.py
```

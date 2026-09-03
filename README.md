# 公积金智能客服系统

广州公积金个贷政策咨询问答。核心链路：FAQ → 检索 → 带引用回答；**Agent 值守**（Day8）再加意图路由、Tool、转人工、限额。

## 5 分钟跑通

先读 [`docs/wiki/`](docs/wiki/)。然后：

```bash
pip install openai
python test_retrieve.py && python test_main_path.py && python test_characterization.py
python test_faq_stats.py && python test_agent.py
python demo_main_path.py && python demo_agent.py
python eval_run.py          # 评估集 20 条，诚实公布分数
```

演示 token：`demo-user-1`（查贷款进度）。转人工政策见 [`docs/escalation-policy.md`](docs/escalation-policy.md)。

有密钥：`python faq_demo.py`（交互，auto 模式）。

## 目录（摘要）

| 路径 | 作用 |
|------|------|
| `agent.py` + `intent/auth/ratelimit/order_tool/ticket_store` | 值守编排 |
| `data/users.json` / `data/orders.json` | 演示鉴权与假订单 API |
| `docs/eval-set.jsonl` + `eval_run.py` | 20 条评估 |
| `docs/spec-agent.md` | Agent 规格 |
| `retrieval.py` / `answer.py` | RAG 心脏（表征测试保护） |

## 当前状态

- [x] L4 团队公约 + L5 主路径 + L6 Wiki/表征
- [x] **Day8 / L7**：意图(policy/loan/escalate) + Tool + 工单 + 限额 + 评估集

## 协作

`docs/wiki/` → `TEAM.md` → PR。改 `retrieval.py` 前先看不敢动清单。

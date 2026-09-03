# Spec · Agent 值守编排

## 模块

| 模块 | 职责 |
|------|------|
| `intent.py` | 规则意图：policy / loan_status / escalate |
| `auth.py` | token → user_id（`data/users.json`） |
| `ratelimit.py` | 每 token 每分钟请求上限（内存，可注入） |
| `order_tool.py` | 读 `data/orders.json`，按 user_id 查贷款申请 |
| `ticket_store.py` | 追加 `data/tickets.json` |
| `agent.py` | 编排入口 `handle()` |
| `demo_agent.py` | 非交互演示 |
| `eval_run.py` | 跑 `docs/eval-set.jsonl` 并计分 |

## 意图表

| intent | 触发（关键词示例） | 路由 |
|--------|-------------------|------|
| policy | 公积金、贷款、额度、提取、利率、首付… | `answer.answer(mode=mock\|live)` |
| loan_status | 进度、审批、我的贷款、申请到哪 | `order_tool`（必须鉴权） |
| escalate | 投诉、举报、人工、转人工、骗子 | `ticket_store` |
| other | 以上都不像 | 视同 escalate |

## handle 返回

```python
{
  "intent": str,
  "state": str,  # answered | order_info | escalated | rejected | unauthorized | rate_limited
  "text": str,
  "refs": list,
  "ticket_id": str | None,
  "order": dict | None,
}
```

## 行为规则

1. **鉴权**：`loan_status` 必须带有效 token；否则 `unauthorized`，不调 Tool。
2. **限额**：默认每 token 每分钟 5 次；超出 `rate_limited`，文案提示稍后重试。
3. **政策**：无检索结果 → `rejected`（沿用 `answer` 拒答，禁止编造）。
4. **Tool**：只返回 JSON 里有的字段，不许模型编单号。
5. **转人工**：写入 ticket（含 question、intent、token 摘要），返回 ticket_id。

## 验收用例（test_agent.py）

| 编号 | 输入 | 预期 |
|------|------|------|
| AG-01 | 我能贷多少, token 任意 | intent=policy, state=answered, text 含来源 |
| AG-02 | 今天天气, token 任意 | state=rejected |
| AG-03 | 我的贷款进度, 无 token | state=unauthorized |
| AG-04 | 我的贷款进度, token=demo-user-1 | state=order_info, order 含 status |
| AG-05 | 我要投诉, token 任意 | state=escalated, ticket_id 非空 |
| AG-06 | 连续 6 次政策问, 同 token | 第 6 次 rate_limited |

## 评估集

- `docs/eval-set.jsonl` 20 条，字段：q, expect_intent, expect_state, expect_in_text（可选）
- `eval_run.py` 打印 `得分 X/20`，诚实公布

## System Ready

- [x] test_agent + eval_run 可重复
- [x] demo_agent 无交互
- [x] docs/escalation-policy.md 一页转人工政策
- [x] 不改 retrieval 心脏（表征测试仍绿）

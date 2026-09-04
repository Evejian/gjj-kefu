# 公积金智能客服系统

广州公积金个贷政策咨询问答。核心链路：FAQ → 检索 → 带引用回答；Agent 值守；**Issue→PR 流水线**（Day9/L8）。

## 5 分钟跑通

先读 [`docs/wiki/`](docs/wiki/)。然后：

```bash
pip install openai
python scripts/gate_ready.py    # 全量测试门禁
python demo_main_path.py && python demo_agent.py
python eval_run.py              # 评估 20 条
```

演示 token：`demo-user-1`。转人工：[`docs/escalation-policy.md`](docs/escalation-policy.md)。  
修 bug：[`docs/delivery-pipeline.md`](docs/delivery-pipeline.md) 或 `/fix-issue 0001`。

## 目录（摘要）

| 路径 | 作用 |
|------|------|
| `scripts/gate_ready.py` | 测试红禁止 Ready |
| `docs/issues/` + `.github/ISSUE_TEMPLATE/` | Issue 进仓库 |
| `.claude/skills/fix-issue` | Issue→复现→红测→修→PR |
| `agent.py` 等 | 值守编排 |
| `retrieval.py` / `answer.py` | RAG 心脏（表征保护） |

## 当前状态

- [x] L4–L7：公约 / 主路径 / Wiki / Agent 值守
- [x] **Day9 / L8**：Issue 模板 + fix-issue + 门禁 + 已知 bug 0001（tickets 容错）+ 失败日志；自动化等级 ≤ 1

## 协作

`TEAM.md`（含自动化分级）→ PR 由人合并。改检索前看不敢动清单。

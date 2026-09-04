# 公积金智能客服系统

广州公积金政策快问：**检索 + Agent 值守 + Issue→PR + 最小商业闭环**（Day10）。

## 5 分钟跑通

```bash
pip install openai
python scripts/gate_ready.py
python demo_saas.py             # 注册→耗次→付费墙→假付费
python demo_agent.py            # 政策/Tool/转人工
```

卖什么：见 `python -c "from saas import landing; print(landing())"`  
成本与下线：`docs/spec-saas.md`（`GJJ_KILL_SWITCH=1`）

## 当前状态

- [x] L4–L8：公约 / 主路径 / Wiki / Agent / Issue→PR
- [x] **Day10 / L9 适配**：注册赠次 → 问答扣次 → 墙 → 测试支付加减次 → 后台账本（无 Web、无真支付）

## 协作

`TEAM.md` 自动化 ≤ 1。门禁：`python scripts/gate_ready.py`

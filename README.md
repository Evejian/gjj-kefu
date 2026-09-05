# 公积金智能客服系统

广州公积金政策快问：**检索 + Agent 值守 + Issue→PR + 最小商业闭环**。结营稿：`docs/camp-retro.md`。

## 5 分钟跑通

```bash
pip install openai
python scripts/gate_ready.py
python demo_saas.py             # 注册→耗次→付费墙→假付费
python demo_agent.py            # 政策/Tool/转人工
python demo_wrap.py             # 结营 8 分钟提纲 + 卖什么
python demo_trial.py            # L4 公约一周试行一页纸
```

卖什么：见 `python -c "from saas import landing; print(landing())"`  
成本与下线：`docs/spec-saas.md`（`GJJ_KILL_SWITCH=1`）  
目标对照：`camp-goals.md`（达成 / 部分达成 / 放弃）  
营外：`docs/l4-trial.md`（2026-09-05～09-11）

## 当前状态

- [x] L4–L9：公约 / 主路径 / Wiki / Agent / Issue→PR / 假付费
- [x] **Day11 / L10**：三份资产 + 8 分钟讲稿（测试支付 ≠ 已盈利）
- [x] **Day12 / 营外**：L4 公约一周试行包（不改生产仓、不强制换 Agent）

## 协作

`TEAM.md` 自动化 ≤ 1。门禁：`python scripts/gate_ready.py`

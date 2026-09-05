# PR 草稿 · Day8–13 合入 main（Day14 / 营外日历第 3 天）

按 `.github/PULL_REQUEST_TEMPLATE.md` 填写。自动化等级 **1**：开 PR，**人合并**。CI 红不合。

## 改动

- Day8：Agent 值守（意图 / 假订单 Tool / 工单 / 限额 / eval 20）
- Day9：Issue→PR 流水线、tickets 容错、`gate_ready.py`
- Day10：注册赠次 → 扣次 → 付费墙 → 假付费 → 账本
- Day11：结营三份资产 + `demo_wrap.py`
- Day12：L4 公约一周试行包
- Day13：规格先行；mock 问答 `cost_cny=0`，live 估算 0.02
- Day14：按模板开本 PR；Agent 不合 main

## 风险

- [ ] 无行为变化（文档 / 配置）
- [ ] 检索 / 拒答逻辑有变（必须补或改测试）
- [x] 涉及密钥、依赖、对外 API

说明：未改 `retrieval.score` / `MIN_SCORE`。密钥仍只读 `ZHIPU_API_KEY`。Function Calling 用已有 `order_tool.py`（查贷款进度），不新增天气/新闻工具。

## 怎么测

```bash
python scripts/gate_ready.py
# 预期：10/10 全绿

python demo_agent.py
python demo_saas.py
python demo_cost.py
python eval_run.py
```

## Agent 贡献说明

- 使用的工具 / 壳：Cursor Agent
- Agent 写了哪些文件或步骤：上列模块、规格、测试、本 PR 正文
- 人做了哪些裁剪 / 否决 / 手工验收：合并权在人；CI 红则不合

> 全手写也请填本栏，写「无，人工实现」，方便团队复盘。

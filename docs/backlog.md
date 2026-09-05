# Backlog（以后再说）

新想法一律先登记在这里，不当场实现。

- 语义检索 / embedding：关键词重合度有天花板，但本期先用它跑通全链路
- Web 界面 / 多轮对话 / 语音：非目标，延后
- 真工单系统 / MCP / 向量检索：见 backlog

## 已闭环（2026-09-05）
- ~~结营 L10~~：三份资产 `docs/camp-retro.md`；目标对照 `camp-goals.md`；`demo_wrap.py`

## 已闭环（2026-09-04）
- ~~SaaS 最小商业闭环 L9~~：注册赠次、扣次问答、付费墙、假支付、kill switch、成本核算
- ~~Issue→PR L8~~：fix-issue skill、gate_ready、tickets 容错、Issue 0001 失败日志

## 已闭环（2026-09-03）
- ~~Agent 值守 L7~~：意图路由 + 假订单 Tool + tickets + 限额 + eval-set 20 条

## 已闭环（2026-08-31）
- ~~FAQ 补齐至 10~20 条~~：已扩到 17 条，覆盖额度、首付、绿色建筑、生育支持、提取、商转公
- ~~检索阈值细化~~：MIN_SCORE=4，弱匹配（只撞"怎么"等常见字）拒答，见 docs/spec.md 行为规则 3
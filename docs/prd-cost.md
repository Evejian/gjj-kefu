# PRD · 问答估算成本入账（Day13 / 营外日历第 2 天）

## 用户
运营 / 自己：怕 mock 演示把「每问 0.02 元」记成真成本，也怕后台看不到累计估算。

## 一句话
每次成功扣次的问答，账本记下 **估算成本**；mock 记 0，live 记 flash 单价；后台能汇总。

## 场景
L4 试行第 2 天要求「下一条真实需求先有规格」。本需求来自已有 `docs/spec-saas.md`：mock≈0，但实现里 consume 一律写了 0.02。

## 非目标
- SSE / Web 流式（AGI Day13 网页部分进 backlog）
- 按真实 token 计费、异步并发、换模型路由逻辑
- 改 retrieval、真支付、改生产仓

## 成功标准
- 规格在 `docs/prd-cost.md` / `spec-cost.md` / `tasks-cost.md`
- `python test_cost.py` 全绿
- `python demo_cost.py` 打印 mock 累计 0、live 记账单价

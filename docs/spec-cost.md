# Spec · 估算成本入账

## 常量

沿用 `COST_PER_ASK_CNY = 0.02`（live / flash）。mock = 0。

## 接口

```python
estimate_cost_cny(mode) -> float   # mock→0, live→0.02
consume_credit(token, store, reason="ask", mode="mock")
cost_sum_cny(store) -> float       # 仅 event=consume 的 cost_cny 之和
admin_snapshot(...)["cost_sum_cny"]
```

## 行为规则

1. 只在 **扣次成功** 的 consume 行写 `cost_cny` 与 `mode`。
2. paywall / unauthorized / killed / api_error / no_key：**不** consume，成本不增加。
3. 拒答 `rejected` 若仍扣次（现行为），成本规则与 answered 相同（mock 0 / live 0.02）。本期不改是否扣次。
4. 不调用真实 tokenizer；不做 SSE。

## 验收用例

| 编号 | 场景 | 预期 |
|------|------|------|
| CS-01 | mock 问答扣次 | 该行 cost_cny=0，cost_sum=0 |
| CS-02 | live 扣次（不打 API，直接 consume） | 该行 cost_cny=0.02，sum 增加 0.02 |
| CS-03 | paywall | cost_sum 不变 |
| CS-04 | killed / unauthorized | 不写 consume |
| CS-05 | demo_cost | 退出 0，打印 mock 累计 0 |

## System Ready

- [x] test_cost 全绿
- [x] demo_cost 无交互
- [x] 规格三件套在库（L4 日历第 2 天证据）
- [x] 无密钥进仓

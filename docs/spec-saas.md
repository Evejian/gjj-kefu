# Spec · 计费与假付费

## 常量

| 名 | 值 | 说明 |
|----|-----|------|
| `SIGNUP_CREDITS` | 3 | 注册赠送 |
| `PACK_CREDITS` | 10 | 一包次数 |
| `PACK_PRICE_CNY` | 9.9 | 展示价（测试） |
| `COST_PER_ASK_CNY` | 0.02 | 估算：mock≈0；live flash 约 ¥0.01–0.05/次，取 0.02 记账 |

## 成本核算（10 行）

1. 收入：9.9 元 / 10 次 → 0.99 元/次标价  
2. 变动成本（live）：约 0.02 元/次（flash）或 0.05（plus）  
3. mock 演示成本：0（账本 `cost_cny=0`，见 `docs/spec-cost.md`）  
4. 毛利（flash）：约 0.97 元/次  
5. 免费赠送 3 次：成本 ≤ 0.15 元/用户（live）或 0（mock）  
6. 破产开关：`GJJ_KILL_SWITCH=1` 拒绝一切 ask/pay  
7. 日限：可选 `max_asks_per_day`（本期用 credits 墙即可）  
8. 密钥只读环境变量，不进仓库  
9. 失败不扣次：API/系统错误不消费 credit  
10. 支付取消/失败不发货

## 接口

```python
register(email) -> {token, credits}
ask(token, question, faqs) -> {state, text, credits_left}
  # states: answered|rejected|paywall|unauthorized|killed|api_error
mock_pay(token, outcome="success"|"cancel"|"fail") -> {state, credits}
admin_snapshot(store) -> {users, ledger_tail, kill_switch}
landing() -> str
```

## 验收用例

| 编号 | 场景 | 预期 |
|------|------|------|
| BL-01 | register | credits=3，有 token |
| BL-02 | ask×3 | 均成功，credits→0 |
| BL-03 | ask 第4次 | paywall |
| BL-04 | pay cancel | credits 仍 0 |
| BL-05 | pay success | credits=10，可再 ask |
| BL-06 | kill_switch | ask → killed |
| BL-07 | 无 token ask | unauthorized |

## System Ready

- [x] test_billing 全绿
- [x] demo_saas 无交互跑通故事
- [x] 成本与开关写进本文
- [x] 无密钥进仓

# PRD · 政策问答 SaaS 最小商业闭环（Day10 / L9 适配）

## 用户
小企业 / 中介想给员工提供「广州公积金政策快问」；按次计费，不自建知识库。

## 场景
不开修图站、不开 Web（本营非目标）。用 **CLI 产品闭环** 等价 L9 故事：

| L9 修图 SaaS | 本仓库等价 |
|--------------|------------|
| 落地页价值一句话 | `saas.landing()` 文案 |
| 注册赠送 N 次 | `register` → credits=3 |
| 核心价值（修图） | 政策问答（mock，不耗真 API） |
| 次数用尽 → 付费墙 | `paywall` |
| 测试支付加次数 | `mock_pay(success\|cancel\|fail)` |
| 后台用户/次数/失败 | `admin_snapshot` |

## 非目标
- Next.js / Vercel / 真 Stripe / 真国内支付
- Web 落地页、修图模型
- 自动部署生产（等级 ≤ 1）

## 成功标准
- `python demo_saas.py` 一次跑通：落地 → 注册 → 问答耗次 → 墙 → 支付成功加次 → 支付取消
- `python test_billing.py` 全绿
- Spec 含成本核算与下线开关

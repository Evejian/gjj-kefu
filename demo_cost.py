"""成本账本演示：mock 累计 0；live 记账单价（不调 API）。"""
from billing import COST_PER_ASK_CNY, consume_credit, empty_store
from faq_store import load_faqs
from saas import admin_snapshot, ask, register


def main():
    faqs = load_faqs()
    store = empty_store()
    token = register("cost-demo@gjj.local", store=store)["token"]
    for i in range(2):
        r = ask(token, "我能贷多少", faqs, store=store, mode="mock")
        print(f"mock#{i+1} state={r['state']} credits={r['credits_left']}")
        if r["state"] != "answered":
            raise SystemExit(1)
    snap = admin_snapshot(store=store)
    print(f"mock 累计成本={snap['cost_sum_cny']}（应为 0）")
    if snap["cost_sum_cny"] != 0:
        raise SystemExit(1)
    consume_credit(token, store, reason="ask", mode="live")
    snap = admin_snapshot(store=store)
    print(f"写入 1 次 live 估算后累计={snap['cost_sum_cny']}（应为 {COST_PER_ASK_CNY}）")
    if snap["cost_sum_cny"] != COST_PER_ASK_CNY:
        raise SystemExit(1)
    print("成本账本演示通过。SSE/Web 流式未做。")


if __name__ == "__main__":
    main()

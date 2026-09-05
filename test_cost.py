"""估算成本入账 CS-01 ~ CS-05。"""
import os

from billing import COST_PER_ASK_CNY, consume_credit, cost_sum_cny, empty_store, estimate_cost_cny
from faq_store import load_faqs
from saas import admin_snapshot, ask, register

FAQS = load_faqs()


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    return cond


def main():
    ok = 0
    store = empty_store()
    token = register("cost@gjj.local", store=store)["token"]

    ask(token, "我能贷多少", FAQS, store=store, mode="mock")
    snap = admin_snapshot(store=store)
    consumes = [r for r in store["ledger"] if r.get("event") == "consume"]
    ok += check("CS-01 mock 成本为 0", consumes[-1]["cost_cny"] == 0 and snap["cost_sum_cny"] == 0)
    ok += check("CS-01b estimate mock", estimate_cost_cny("mock") == 0)

    before = cost_sum_cny(store)
    consume_credit(token, store, reason="ask", mode="live")
    after = cost_sum_cny(store)
    ok += check(
        "CS-02 live 记 0.02 且不打 API",
        after == round(before + COST_PER_ASK_CNY, 4) and estimate_cost_cny("live") == COST_PER_ASK_CNY,
    )

    wall_store = empty_store()
    t2 = register("wall@gjj.local", store=wall_store)["token"]
    for _ in range(3):
        ask(t2, "我能贷多少", FAQS, store=wall_store, mode="mock")
    sum_before = cost_sum_cny(wall_store)
    r = ask(t2, "公积金提取", FAQS, store=wall_store, mode="mock")
    ok += check("CS-03 paywall 成本不变", r["state"] == "paywall" and cost_sum_cny(wall_store) == sum_before)

    n_before = len([x for x in wall_store["ledger"] if x.get("event") == "consume"])
    r = ask(None, "我能贷多少", FAQS, store=wall_store, mode="mock")
    old = os.environ.get("GJJ_KILL_SWITCH")
    os.environ["GJJ_KILL_SWITCH"] = "1"
    try:
        k = ask(t2, "我能贷多少", FAQS, store=wall_store, mode="mock")
    finally:
        if old is None:
            os.environ.pop("GJJ_KILL_SWITCH", None)
        else:
            os.environ["GJJ_KILL_SWITCH"] = old
    n_after = len([x for x in wall_store["ledger"] if x.get("event") == "consume"])
    ok += check(
        "CS-04 未登录/下线不 consume",
        r["state"] == "unauthorized" and k["state"] == "killed" and n_after == n_before,
    )

    print()
    print(f"{ok}/5 通过")
    if ok < 5:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

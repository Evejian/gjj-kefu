"""商业闭环演示：落地 → 注册 → 耗次 → 墙 → 取消支付 → 成功支付 → 再问 → 后台。"""
from billing import empty_store
from faq_store import load_faqs
from saas import admin_snapshot, ask, landing, pay, register


def show(title, result):
    print(f"=== {title} ===")
    if isinstance(result, str):
        print(result)
    else:
        print(f"state={result.get('state')} credits={result.get('credits', result.get('credits_left'))}")
        text = result.get("text", "")
        preview = text.replace("\n", " / ")
        if len(preview) > 100:
            preview = preview[:100] + "…"
        print(preview)
    print()


def main():
    faqs = load_faqs()
    store = empty_store()

    show("落地页", landing())
    reg = register("demo@gjj.local", store=store)
    show("注册", reg)
    token = reg["token"]

    for i in range(3):
        r = ask(token, "我能贷多少", faqs, store=store, mode="mock")
        show(f"问答 #{i+1}", r)
        if r["state"] != "answered":
            raise SystemExit(1)

    wall = ask(token, "公积金提取", faqs, store=store, mode="mock")
    show("付费墙", wall)
    if wall["state"] != "paywall":
        raise SystemExit(1)

    show("支付取消", pay(token, outcome="cancel", store=store))
    show("支付失败", pay(token, outcome="fail", store=store))
    paid = pay(token, outcome="success", store=store)
    show("支付成功", paid)
    if paid["state"] != "paid":
        raise SystemExit(1)

    again = ask(token, "商转公条件", faqs, store=store, mode="mock")
    show("充值后再问", again)
    if again["state"] != "answered":
        raise SystemExit(1)

    snap = admin_snapshot(store=store)
    print("=== 后台快照 ===")
    print(f"用户数={snap['user_count']} kill_switch={snap['kill_switch']}")
    for u in snap["users"]:
        print(f"  {u['email']} credits={u['credits']}")
    print(f"账本尾 {len(snap['ledger_tail'])} 条")
    print("\nSaaS 闭环演示通过。")


if __name__ == "__main__":
    main()

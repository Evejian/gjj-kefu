"""计费与假付费测试。"""
import os
from billing import empty_store, SIGNUP_CREDITS, PACK_CREDITS, PACK_PRICE_CNY
from faq_store import load_faqs
from saas import ask, landing, pay, register, admin_snapshot

FAQS = load_faqs()
results = []


def check(name, cond):
    results.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


store = empty_store()

# BL-01
r = register("a@example.com", store=store)
token = r["token"]
check("BL-01 注册赠送次数", r["state"] == "registered" and r["credits"] == SIGNUP_CREDITS and token)

# BL-02
states = []
for i in range(SIGNUP_CREDITS):
    r = ask(token, "我能贷多少", FAQS, store=store, mode="mock")
    states.append(r["state"])
check(
    "BL-02 赠送次数用完",
    all(s == "answered" for s in states) and r["credits_left"] == 0,
)

# BL-03
r = ask(token, "公积金利率", FAQS, store=store, mode="mock")
check("BL-03 付费墙", r["state"] == "paywall")

# BL-04
r = pay(token, outcome="cancel", store=store)
check("BL-04 支付取消不发货", r["state"] == "pay_cancelled" and r["credits"] == 0)

# BL-05
r = pay(token, outcome="success", store=store)
check("BL-05 支付成功加次", r["state"] == "paid" and r["credits"] == PACK_CREDITS)
r = ask(token, "二孩额度", FAQS, store=store, mode="mock")
check("BL-05b 充值后可问", r["state"] == "answered" and r["credits_left"] == PACK_CREDITS - 1)

# BL-06
old = os.environ.get("GJJ_KILL_SWITCH")
os.environ["GJJ_KILL_SWITCH"] = "1"
try:
    r = ask(token, "我能贷多少", FAQS, store=store, mode="mock")
    check("BL-06 kill switch", r["state"] == "killed")
finally:
    if old is None:
        os.environ.pop("GJJ_KILL_SWITCH", None)
    else:
        os.environ["GJJ_KILL_SWITCH"] = old

# BL-07
r = ask(None, "我能贷多少", FAQS, store=store, mode="mock")
check("BL-07 未登录", r["state"] == "unauthorized")

# landing + admin
check("BL-08 落地页含价格", "元" in landing() and str(PACK_PRICE_CNY).split(".")[0] in landing())
snap = admin_snapshot(store=store)
check("BL-09 后台有用户与账本", snap["user_count"] >= 1 and len(snap["ledger_tail"]) >= 1)

failed = [n for n, ok in results if not ok]
print()
print(f"{len(results) - len(failed)}/{len(results)} 通过")
if failed:
    print("失败：", failed)
    raise SystemExit(1)

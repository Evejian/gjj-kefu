"""政策问答 SaaS 编排：落地 → 注册 → 扣次问答 → 付费墙 → 假付费。"""
import os

from answer import answer
from billing import (
    PACK_CREDITS,
    PACK_PRICE_CNY,
    SIGNUP_CREDITS,
    consume_credit,
    cost_sum_cny,
    get_user,
    load_store,
    register as billing_register,
    save_store,
)
from payment_mock import mock_pay


def landing():
    return (
        "【广州公积金政策快问】\n"
        "一句话：缴存职工/中介 30 秒查清「能贷多少」，回答带政策出处。\n"
        f"价格：新用户赠 {SIGNUP_CREDITS} 次；续包 {PACK_CREDITS} 次 / {PACK_PRICE_CNY} 元（测试支付）。\n"
        "下线开关：环境变量 GJJ_KILL_SWITCH=1"
    )


def _killed():
    return os.environ.get("GJJ_KILL_SWITCH", "").strip() in ("1", "true", "TRUE", "yes")


def register(email, store=None, path=None):
    store = store if store is not None else load_store(path)
    user = billing_register(email, store=store, path=None)
    if path is not None:
        save_store(store, path)
    return {
        "state": "registered",
        "token": user["token"],
        "credits": user["credits"],
        "text": f"注册成功。token={user['token']}，赠送 {user['credits']} 次。",
    }


def ask(token, question, faqs, store=None, path=None, mode="mock"):
    store = store if store is not None else load_store(path)
    if _killed() or store.get("kill_switch"):
        return {
            "state": "killed",
            "text": "服务维护中（kill switch），暂停问答。",
            "credits_left": (get_user(token, store) or {}).get("credits", 0),
            "refs": [],
        }

    user = get_user(token, store)
    if not user:
        return {
            "state": "unauthorized",
            "text": "请先注册：saas.register(email)",
            "credits_left": 0,
            "refs": [],
        }

    if user["credits"] <= 0:
        return {
            "state": "paywall",
            "text": (
                f"次数已用尽。购买续包 {PACK_CREDITS} 次 / {PACK_PRICE_CNY} 元："
                f"mock_pay(token, outcome='success')"
            ),
            "credits_left": 0,
            "refs": [],
        }

    # 先调用核心价值；失败不扣次
    result = answer(question, faqs, mode=mode)
    if result["state"] not in ("answered", "rejected"):
        return {
            "state": result["state"],
            "text": result["text"],
            "credits_left": user["credits"],
            "refs": result.get("refs", []),
        }

    consume_credit(token, store, reason="ask", mode=mode)
    user = get_user(token, store)
    if path is not None:
        save_store(store, path)
    return {
        "state": result["state"],
        "text": result["text"],
        "credits_left": user["credits"],
        "refs": result.get("refs", []),
    }


def pay(token, outcome="success", store=None, path=None):
    store = store if store is not None else load_store(path)
    if _killed():
        store = store or {}
        store["kill_switch"] = True
    result = mock_pay(token, store, outcome=outcome)
    if path is not None:
        save_store(store, path)
    return result


def admin_snapshot(store=None, path=None):
    store = store if store is not None else load_store(path)
    users = [
        {"email": u["email"], "token": u["token"], "credits": u["credits"]}
        for u in store["users"].values()
    ]
    return {
        "kill_switch": bool(store.get("kill_switch")) or _killed(),
        "users": users,
        "ledger_tail": store["ledger"][-8:],
        "user_count": len(users),
        "cost_sum_cny": cost_sum_cny(store),
    }

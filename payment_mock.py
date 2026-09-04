"""假支付：测试模式 success / cancel / fail，不接真实商户号。"""
from billing import PACK_CREDITS, PACK_PRICE_CNY, get_user, grant_credits, _append_ledger


def mock_pay(token, store, outcome="success"):
    """outcome: success | cancel | fail"""
    user = get_user(token, store)
    if not user:
        return {"state": "unauthorized", "credits": 0, "text": "请先注册/登录。"}

    if store.get("kill_switch"):
        return {
            "state": "killed",
            "credits": user["credits"],
            "text": "服务维护中（kill switch），暂停充值。",
        }

    if outcome == "cancel":
        _append_ledger(store, "pay_cancel", token=token, price_cny=PACK_PRICE_CNY)
        return {
            "state": "pay_cancelled",
            "credits": user["credits"],
            "text": "支付已取消，次数未增加。",
        }

    if outcome == "fail":
        _append_ledger(store, "pay_fail", token=token, price_cny=PACK_PRICE_CNY)
        return {
            "state": "pay_failed",
            "credits": user["credits"],
            "text": "支付失败（测试），请重试。次数未增加。",
        }

    if outcome != "success":
        return {
            "state": "pay_failed",
            "credits": user["credits"],
            "text": f"未知支付结果：{outcome}",
        }

    grant_credits(token, store, PACK_CREDITS, reason="pack_purchase")
    _append_ledger(
        store,
        "pay_success",
        token=token,
        price_cny=PACK_PRICE_CNY,
        credits_added=PACK_CREDITS,
    )
    user = get_user(token, store)
    return {
        "state": "paid",
        "credits": user["credits"],
        "text": f"支付成功（测试）{PACK_PRICE_CNY} 元，已到账 {PACK_CREDITS} 次。当前余额 {user['credits']}。",
    }

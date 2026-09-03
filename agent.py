"""Agent 值守：鉴权 → 限额 → 意图 → RAG / Tool / 工单。"""
from answer import answer
from auth import resolve_user
from intent import classify_intent
from order_tool import format_order_text, get_loan_application
from ratelimit import RateLimiter
from ticket_store import create_ticket

_DEFAULT_LIMITER = RateLimiter(max_calls=5)


def handle(
    question,
    faqs,
    *,
    token=None,
    mode="mock",
    rate_limiter=None,
    tickets_path=None,
    orders_path=None,
    users_path=None,
):
    limiter = rate_limiter if rate_limiter is not None else _DEFAULT_LIMITER
    rate_key = token or "anonymous"

    if not limiter.check(rate_key):
        return {
            "intent": classify_intent(question),
            "state": "rate_limited",
            "text": "请求过于频繁，请稍后再试。",
            "refs": [],
            "ticket_id": None,
            "order": None,
        }

    intent = classify_intent(question)

    if intent == "escalate":
        ticket = create_ticket(question, intent, token=token, tickets_path=tickets_path)
        return {
            "intent": intent,
            "state": "escalated",
            "text": f"已为您转接人工，工单号：{ticket['ticket_id']}。工作人员将尽快处理。",
            "refs": [],
            "ticket_id": ticket["ticket_id"],
            "order": None,
        }

    if intent == "other":
        result = answer(question, faqs, mode=mode)
        if result["state"] == "answered":
            return {
                "intent": "policy",
                "state": "answered",
                "text": result["text"],
                "refs": result.get("refs", []),
                "ticket_id": None,
                "order": None,
            }
        ticket = create_ticket(question, intent, token=token, tickets_path=tickets_path)
        return {
            "intent": intent,
            "state": "escalated",
            "text": f"暂未查到相关政策，已转人工，工单号：{ticket['ticket_id']}。",
            "refs": [],
            "ticket_id": ticket["ticket_id"],
            "order": None,
        }

    if intent == "loan_status":
        user = resolve_user(token, users_path=users_path)
        if not user:
            return {
                "intent": intent,
                "state": "unauthorized",
                "text": "查询贷款进度需要登录。请提供有效 token（演示账号：demo-user-1）。",
                "refs": [],
                "ticket_id": None,
                "order": None,
            }
        order = get_loan_application(user["user_id"], orders_path=orders_path)
        if not order:
            return {
                "intent": intent,
                "state": "rejected",
                "text": "未找到您的贷款申请记录。",
                "refs": [],
                "ticket_id": None,
                "order": None,
            }
        return {
            "intent": intent,
            "state": "order_info",
            "text": format_order_text(order),
            "refs": [],
            "ticket_id": None,
            "order": order,
        }

    # policy
    result = answer(question, faqs, mode=mode)
    state = result["state"]
    if state == "answered":
        agent_state = "answered"
    elif state == "rejected":
        agent_state = "rejected"
    else:
        agent_state = state
    return {
        "intent": "policy",
        "state": agent_state,
        "text": result["text"],
        "refs": result.get("refs", []),
        "ticket_id": None,
        "order": None,
    }

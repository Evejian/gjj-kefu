"""规则意图分类（可测、不绑模型）。"""

ESCALATE_KEYWORDS = ("投诉", "举报", "人工", "转人工", "骗子", "态度差")
LOAN_STATUS_KEYWORDS = ("进度", "审批", "我的贷款", "申请到哪", "贷款状态", "办到哪", "查订单")
POLICY_KEYWORDS = (
    "公积金",
    "贷款",
    "提取",
    "额度",
    "利率",
    "首付",
    "商转公",
    "绿色建筑",
    "二孩",
    "缴存",
    "能贷",
)


def classify_intent(question: str) -> str:
    q = question.strip()
    if not q:
        return "other"
    for kw in ESCALATE_KEYWORDS:
        if kw in q:
            return "escalate"
    for kw in LOAN_STATUS_KEYWORDS:
        if kw in q:
            return "loan_status"
    for kw in POLICY_KEYWORDS:
        if kw in q:
            return "policy"
    return "other"

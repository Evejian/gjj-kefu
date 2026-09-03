"""假订单 API：只读 JSON，禁止模型编单号。"""
import json
from pathlib import Path

DEFAULT_ORDERS_PATH = Path(__file__).resolve().parent / "data" / "orders.json"


def load_orders(path=None):
    p = Path(path) if path else DEFAULT_ORDERS_PATH
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def get_loan_application(user_id, orders_path=None):
    for row in load_orders(orders_path):
        if row.get("user_id") == user_id:
            return row
    return None


def format_order_text(order):
    return (
        f"申请编号：{order['application_id']}\n"
        f"状态：{order['status']}\n"
        f"金额：{order['amount']}\n"
        f"更新时间：{order['updated_at']}"
    )

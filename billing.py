"""用户额度与账单账本（文件存储，演示用）。"""
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

SIGNUP_CREDITS = 3
PACK_CREDITS = 10
PACK_PRICE_CNY = 9.9
COST_PER_ASK_CNY = 0.02

DEFAULT_STORE = Path(__file__).resolve().parent / "data" / "billing.json"


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def empty_store():
    return {"users": {}, "ledger": [], "kill_switch": False}


def load_store(path=None):
    p = Path(path) if path else DEFAULT_STORE
    if not p.exists():
        return empty_store()
    try:
        with p.open(encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return empty_store()
    if not isinstance(data, dict):
        return empty_store()
    data.setdefault("users", {})
    data.setdefault("ledger", [])
    data.setdefault("kill_switch", False)
    return data


def save_store(store, path=None):
    p = Path(path) if path else DEFAULT_STORE
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=2)


def _append_ledger(store, event, **fields):
    row = {"at": _now(), "event": event, **fields}
    store["ledger"].append(row)
    return row


def register(email, store=None, path=None):
    store = store if store is not None else load_store(path)
    token = "tok-" + uuid.uuid4().hex[:10]
    user = {
        "email": email,
        "token": token,
        "credits": SIGNUP_CREDITS,
        "created_at": _now(),
    }
    store["users"][token] = user
    _append_ledger(store, "signup", token=token, email=email, credits=SIGNUP_CREDITS)
    if path is not None or store is None:
        save_store(store, path)
    return user


def get_user(token, store):
    if not token:
        return None
    return store["users"].get(token)


def consume_credit(token, store, reason="ask"):
    user = get_user(token, store)
    if not user:
        return None
    if user["credits"] <= 0:
        return user
    user["credits"] -= 1
    _append_ledger(
        store,
        "consume",
        token=token,
        reason=reason,
        credits_left=user["credits"],
        cost_cny=COST_PER_ASK_CNY,
    )
    return user


def grant_credits(token, store, amount, reason="pack"):
    user = get_user(token, store)
    if not user:
        return None
    user["credits"] += amount
    _append_ledger(
        store,
        "grant",
        token=token,
        reason=reason,
        amount=amount,
        credits_left=user["credits"],
    )
    return user


def set_kill_switch(store, on: bool):
    store["kill_switch"] = bool(on)
    _append_ledger(store, "kill_switch", on=store["kill_switch"])

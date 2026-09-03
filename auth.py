"""简易 token 鉴权。"""
import json
from pathlib import Path

DEFAULT_USERS_PATH = Path(__file__).resolve().parent / "data" / "users.json"


def load_users(path=None):
    p = Path(path) if path else DEFAULT_USERS_PATH
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def resolve_user(token, users_path=None):
    if not token:
        return None
    users = load_users(users_path)
    for u in users:
        if u.get("token") == token:
            return u
    return None

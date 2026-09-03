"""转人工工单存储。"""
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_TICKETS_PATH = Path(__file__).resolve().parent / "data" / "tickets.json"


def _load(path):
    p = Path(path)
    if not p.exists():
        return []
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def _save(path, items):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def create_ticket(question, intent, token=None, tickets_path=None):
    path = Path(tickets_path) if tickets_path else DEFAULT_TICKETS_PATH
    ticket_id = "T" + uuid.uuid4().hex[:8]
    ticket = {
        "ticket_id": ticket_id,
        "question": question,
        "intent": intent,
        "token_hint": (token[:4] + "***") if token else None,
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    items = _load(path)
    items.append(ticket)
    _save(path, items)
    return ticket

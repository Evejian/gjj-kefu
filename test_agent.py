"""Agent 值守测试。"""
import json
import tempfile
from pathlib import Path

from agent import handle
from faq_store import load_faqs
from ratelimit import RateLimiter

FAQS = load_faqs()
results = []


def check(name, cond):
    results.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


def tmp_tickets():
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8")
    f.write("[]")
    f.close()
    return f.name


def cleanup(path):
    try:
        Path(path).unlink(missing_ok=True)
    except OSError:
        pass


# AG-01
path = tmp_tickets()
try:
    r = handle("我能贷多少", FAQS, token="demo-user-1", mode="mock", tickets_path=path)
    check(
        "AG-01 政策有引用",
        r["intent"] == "policy"
        and r["state"] == "answered"
        and "来源" in r["text"],
    )
finally:
    cleanup(path)

# AG-02
path = tmp_tickets()
try:
    r = handle("今天天气怎么样", FAQS, mode="mock", tickets_path=path)
    check("AG-02 无关问题转人工", r["state"] == "escalated" and r["ticket_id"])
finally:
    cleanup(path)

# AG-03
path = tmp_tickets()
try:
    r = handle("我的贷款进度", FAQS, token=None, tickets_path=path)
    check("AG-03 查进度无 token", r["state"] == "unauthorized")
finally:
    cleanup(path)

# AG-04
path = tmp_tickets()
try:
    r = handle("我的贷款审批进度", FAQS, token="demo-user-1", tickets_path=path)
    check(
        "AG-04 Tool 返回订单",
        r["state"] == "order_info" and r["order"] and "审批中" in r["text"],
    )
finally:
    cleanup(path)

# AG-05
path = tmp_tickets()
try:
    r = handle("我要投诉", FAQS, tickets_path=path)
    check("AG-05 投诉转工单", r["state"] == "escalated" and r["ticket_id"])
finally:
    cleanup(path)

# AG-06
path = tmp_tickets()
limiter = RateLimiter(max_calls=5)
try:
    states = []
    for _ in range(6):
        r = handle("公积金贷款利率", FAQS, token="rl-test", mode="mock", tickets_path=path, rate_limiter=limiter)
        states.append(r["state"])
    check("AG-06 第6次限额", states[-1] == "rate_limited" and states[0] == "answered")
finally:
    cleanup(path)

failed = [n for n, ok in results if not ok]
print()
print(f"{len(results) - len(failed)}/{len(results)} 通过")
if failed:
    raise SystemExit(1)

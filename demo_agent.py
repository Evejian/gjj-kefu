"""Agent 值守演示：政策 / Tool / 转人工 / 限额。"""
import tempfile
from pathlib import Path

from agent import handle
from faq_store import load_faqs
from ratelimit import RateLimiter


def cleanup(path):
    try:
        Path(path).unlink(missing_ok=True)
    except OSError:
        pass


def run_case(title, question, token, limiter, ticket_path, faqs):
    r = handle(
        question,
        faqs,
        token=token,
        mode="mock",
        tickets_path=ticket_path,
        rate_limiter=limiter,
    )
    print(f"=== {title} ===")
    print(f"问：{question}")
    print(f"intent={r['intent']} state={r['state']}")
    if r.get("ticket_id"):
        print(f"工单：{r['ticket_id']}")
    preview = r["text"].replace("\n", " / ")
    if len(preview) > 120:
        preview = preview[:120] + "…"
    print(f"答：{preview}\n")
    return r


def main():
    faqs = load_faqs()
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8")
    f.write("[]")
    f.close()
    ticket_path = f.name
    limiter = RateLimiter(max_calls=10)

    run_case("政策+RAG引用", "我能贷多少", "demo-user-1", limiter, ticket_path, faqs)
    run_case("Tool查进度", "我的贷款审批进度", "demo-user-1", limiter, ticket_path, faqs)
    run_case("未鉴权", "我的贷款进度", None, limiter, ticket_path, faqs)
    run_case("转人工", "我要投诉", None, limiter, ticket_path, faqs)

    # 限额
    rl = RateLimiter(max_calls=2)
    run_case("限额1", "公积金利率", None, rl, ticket_path, faqs)
    run_case("限额2", "公积金提取", None, rl, ticket_path, faqs)
    r = run_case("限额3应被拦", "公积金贷款", None, rl, ticket_path, faqs)
    if r["state"] != "rate_limited":
        cleanup(ticket_path)
        raise SystemExit(1)

    cleanup(ticket_path)
    print("Agent 演示通过。")


if __name__ == "__main__":
    main()

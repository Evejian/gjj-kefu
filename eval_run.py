"""跑评估集并诚实公布分数。"""
import json
import sys
import tempfile
from pathlib import Path

from agent import handle
from faq_store import load_faqs

EVAL_PATH = Path(__file__).resolve().parent / "docs" / "eval-set.jsonl"


def load_eval():
    rows = []
    with EVAL_PATH.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def main():
    faqs = load_faqs()
    cases = load_eval()
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8")
    f.write("[]")
    f.close()
    ticket_path = f.name
    limiter_key = 0

    from ratelimit import RateLimiter

    limiter = RateLimiter(max_calls=100)

    ok = 0
    print(f"评估集：{len(cases)} 条\n")
    for i, case in enumerate(cases, 1):
        token = case.get("token")
        r = handle(
            case["q"],
            faqs,
            token=token,
            mode="mock",
            tickets_path=ticket_path,
            rate_limiter=limiter,
        )
        intent_ok = r["intent"] == case["expect_intent"]
        state_ok = r["state"] == case["expect_state"]
        text_ok = True
        if case.get("expect_in_text"):
            text_ok = case["expect_in_text"] in r["text"]
        passed = intent_ok and state_ok and text_ok
        ok += int(passed)
        mark = "OK" if passed else "FAIL"
        print(f"{mark} {i:02d} q={case['q'][:20]} intent={r['intent']} state={r['state']}")
        if not passed:
            print(f"     期望 intent={case['expect_intent']} state={case['expect_state']} in={case.get('expect_in_text')}")

    try:
        Path(ticket_path).unlink(missing_ok=True)
    except OSError:
        pass
    score = ok / len(cases) * 100
    print(f"\n得分 {ok}/{len(cases)}（{score:.0f}%）")
    if ok < len(cases):
        sys.exit(1)


if __name__ == "__main__":
    main()

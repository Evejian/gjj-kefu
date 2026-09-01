"""非交互演示：成功（mock）/ 拒答 / API 失败 三态一次跑通。"""
import json
from answer import answer


def load_faqs():
    with open("faq.jsonl", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


CASES = [
    ("成功(mock)", "我能贷多少", {"mode": "mock"}, "answered"),
    ("拒答", "今天天气怎么样", {"mode": "mock"}, "rejected"),
    ("API失败", "我能贷多少", {"mode": "live", "force_api_error": True}, "api_error"),
]


def main():
    faqs = load_faqs()
    # API 失败态需要环境里有 key 才会走进 force_api_error 分支（否则先 no_key）
    import os

    os.environ.setdefault("ZHIPU_API_KEY", "demo-placeholder-not-a-real-key")

    print("=== 公积金智能客服 · 主路径演示（无需交互）===\n")
    for title, question, kwargs, expect in CASES:
        result = answer(question, faqs, **kwargs)
        status = "OK" if result["state"] == expect else "MISMATCH"
        print(f"[{status}] {title}")
        print(f"  问：{question}")
        print(f"  状态：{result['state']}（期望 {expect}）")
        preview = result["text"].replace("\n", " / ")
        if len(preview) > 160:
            preview = preview[:160] + "…"
        print(f"  答：{preview}\n")
        if result["state"] != expect:
            raise SystemExit(1)

    print("三态演示通过：answered / rejected / api_error")


if __name__ == "__main__":
    main()

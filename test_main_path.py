import os
from answer import answer
from faq_store import load_faqs


FAQS = load_faqs()
results = []


def check(name, cond):
    results.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


# MP-01 mock 成功
r = answer("我能贷多少", FAQS, mode="mock")
check(
    "MP-01 mock 成功作答且带来源",
    r["state"] == "answered"
    and "[mock]" in r["text"]
    and "来源：" in r["text"]
    and bool(r["refs"]),
)

# MP-02 拒答
r = answer("今天天气怎么样", FAQS, mode="mock")
check("MP-02 无关问题拒答", r["state"] == "rejected" and "没有查到相关政策" in r["text"])

# MP-03 live 但无 key
old = os.environ.pop("ZHIPU_API_KEY", None)
try:
    r = answer("我能贷多少", FAQS, mode="live")
    check("MP-03 live 无 key → no_key", r["state"] == "no_key" and "ZHIPU_API_KEY" in r["text"])
finally:
    if old is not None:
        os.environ["ZHIPU_API_KEY"] = old

# MP-04 API 失败可提示
os.environ["ZHIPU_API_KEY"] = "dummy-key-for-force-error"
try:
    r = answer("我能贷多少", FAQS, mode="live", force_api_error=True)
    check(
        "MP-04 API 失败态",
        r["state"] == "api_error" and "失败" in r["text"] and "mock" in r["text"],
    )
finally:
    del os.environ["ZHIPU_API_KEY"]
    if old is not None:
        os.environ["ZHIPU_API_KEY"] = old

failed = [name for name, ok in results if not ok]
print()
if failed:
    print(f"{len(results) - len(failed)}/{len(results)} 通过，失败：{failed}")
    raise SystemExit(1)
print(f"{len(results)}/{len(results)} 通过")

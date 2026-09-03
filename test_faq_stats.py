"""faq_stats 只读行为测试。"""
from faq_store import load_faqs
from faq_stats import stats

results = []


def check(name, cond):
    results.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


faqs = load_faqs()
s = stats(faqs)
check("FS-01 total 与 load 一致", s["total"] == len(faqs) == 17)
check("FS-02 by_src 非空", len(s["by_src"]) >= 1)
check("FS-03 by_src 条数加总 = total", sum(s["by_src"].values()) == s["total"])

failed = [name for name, ok in results if not ok]
print()
print(f"{len(results) - len(failed)}/{len(results)} 通过")
if failed:
    raise SystemExit(1)

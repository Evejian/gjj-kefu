from faq_store import load_faqs
from retrieval import MIN_SCORE, score, get_top3, format_refs
from answer import answer, REJECT_TEXT


FAQS = load_faqs()
results = []


def check(name, cond):
    results.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


# --- 打分心脏 ---
check("CH-01 MIN_SCORE 仍为 4", MIN_SCORE == 4)

check(
    "CH-02 汉字重合计分",
    score("公积金贷款额度", {"q": "公积金个人住房贷款最高能贷多少？"}) >= 4,
)

check(
    "CH-03 标点与英文不计分",
    score("Hello???", {"q": "Hello 公积金!!!"}) == 0,
)

# --- get_top3 契约（含「第3条可低于 MIN_SCORE」）---
top = get_top3("我能贷多少", FAQS)
check("CH-04 我能贷多少 召回非空且≤3", 1 <= len(top) <= 3)
check(
    "CH-05 top1 分数 ≥ MIN_SCORE",
    score("我能贷多少", top[0]) >= MIN_SCORE,
)
if len(top) >= 2:
    check(
        "CH-06 分数非递增（降序或相等）",
        score("我能贷多少", top[0]) >= score("我能贷多少", top[1]),
    )
else:
    check("CH-06 分数非递增（降序或相等）", True)

check("CH-07 天气拒答为空列表", get_top3("今天天气怎么样", FAQS) == [])
check(
    "CH-08 弱匹配最高分 < MIN_SCORE",
    max(score("这个政策怎么申请", f) for f in FAQS) < MIN_SCORE,
)

# --- format_refs / mock 文本形态 ---
block = format_refs(top[:1])
check(
    "CH-09 format_refs 含问答复来源",
    block.startswith("问：") and "答：" in block and "来源：" in block,
)

mock = answer("我能贷多少", FAQS, mode="mock")
check(
    "CH-10 mock 形态",
    mock["state"] == "answered"
    and mock["text"].startswith("[mock]")
    and "来源：" in mock["text"],
)

rej = answer("今天天气怎么样", FAQS, mode="mock")
check("CH-11 拒答文案锁死", rej["state"] == "rejected" and rej["text"] == REJECT_TEXT)

# --- 额度召回不回归（Day4 修正过的数字）---
top_amt = get_top3("公积金个人住房贷款最高能贷多少", FAQS)
check("CH-12 最高额度仍含 100万元", bool(top_amt) and "100万元" in top_amt[0]["a"])

failed = [name for name, ok in results if not ok]
print()
print(f"{len(results) - len(failed)}/{len(results)} 通过")
if failed:
    print("失败：", failed)
    raise SystemExit(1)

import json
from retrieval import score, get_top3


def load_faqs():
    with open("faq.jsonl", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


FAQS = load_faqs()

results = []

def check(name, cond):
    results.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


# UC-01 贷款额度问题应召回最高额度那条
top = get_top3("公积金个人住房贷款最高能贷多少", FAQS)
check("UC-01 top1 是最高额度那条",
      bool(top) and "100万元" in top[0]["a"])

# UC-02 二孩问题应召回二孩政策那条
top = get_top3("二孩家庭额度能上浮吗", FAQS)
check("UC-02 top1 是二孩政策那条",
      bool(top) and "上浮40%" in top[0]["a"])

# UC-03 无关问题返回空列表（失败态）
check("UC-03 无关问题返回空", get_top3("今天天气怎么样", FAQS) == [])

# UC-03b 弱匹配（仅撞一两个常见字，如"什么"）也拒答
check("UC-03b 弱匹配返回空", get_top3("这个政策怎么申请", FAQS) == [])

# UC-04 标点不计分
check("UC-04 纯标点得 0 分", score("？？？!!!", {"q": "公积金贷款？额度！"}) == 0)
check("UC-04b 纯标点返回空", get_top3("？？？!!!", FAQS) == [])

# UC-05 最多 3 条，按分数降序
items = get_top3("公积金贷款额度", FAQS)
scores = [score("公积金贷款额度", faq) for faq in items]
check("UC-05 最多 3 条", len(items) <= 3)
check("UC-05b 按分数降序", scores == sorted(scores, reverse=True))

failed = [name for name, ok in results if not ok]
print()
print(f"{len(results) - len(failed)}/{len(results)} 通过")
if failed:
    raise SystemExit(1)

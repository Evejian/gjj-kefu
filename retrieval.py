import re

# 只统计汉字和数字，标点、字母、空白不计分
_CHARS = re.compile(r"[一-鿿0-9]")


def score(question, faq):
    q_set = set(_CHARS.findall(question))
    f_set = set(_CHARS.findall(faq["q"]))
    return len(q_set & f_set)


def get_top3(question, faqs):
    ranked = sorted(faqs, key=lambda faq: score(question, faq), reverse=True)
    if not ranked or score(question, ranked[0]) == 0:
        return []
    return ranked[:3]


def format_refs(items):
    blocks = [f"问：{item['q']}\n答：{item['a']}\n来源：{item['src']}" for item in items]
    return "\n\n".join(blocks)

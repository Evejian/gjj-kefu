"""只读：按来源统计 FAQ（L6 安全区小需求，不碰检索/回答）。"""
from collections import Counter
from faq_store import load_faqs


def stats(faqs=None):
    faqs = faqs if faqs is not None else load_faqs()
    by_src = Counter(item.get("src", "(missing)") for item in faqs)
    return {
        "total": len(faqs),
        "by_src": dict(sorted(by_src.items(), key=lambda kv: (-kv[1], kv[0]))),
    }


def main():
    s = stats()
    print(f"FAQ 总计：{s['total']} 条\n")
    print("按来源：")
    for src, n in s["by_src"].items():
        print(f"  {n:3d}  {src}")


if __name__ == "__main__":
    main()

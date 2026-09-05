"""结营产物验收 WR-01 ~ WR-04。"""
from pathlib import Path

from saas import landing

ROOT = Path(__file__).resolve().parent


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    return cond


def main():
    goals = (ROOT / "camp-goals.md").read_text(encoding="utf-8")
    retro = (ROOT / "docs" / "camp-retro.md").read_text(encoding="utf-8")
    from demo_wrap import talk

    text = talk()
    ok = 0
    ok += check("WR-01 camp-goals 达成/部分达成/放弃", all(w in goals for w in ("达成", "部分达成", "放弃")))
    ok += check("WR-02 三份资产标题", all(w in retro for w in ("项目资产", "产品资产", "个人操作系统")))
    ok += check("WR-03 demo_wrap 含价格", "9.9" in text and "结营讲稿打印完毕" in text)
    ok += check(
        "WR-04 八分钟结构",
        all(w in text for w in ("开营目标", "证据", "最大失败", "杠杆")),
    )
    ok += check("WR-03b landing 可给陌生人读", "政策快问" in landing() and "GJJ_KILL_SWITCH" in landing())
    print()
    print(f"{ok}/5 通过")
    if ok < 5:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

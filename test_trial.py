"""公约试行包 TR-01 ~ TR-05。"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    return cond


def main():
    trial = (ROOT / "docs" / "l4-trial.md").read_text(encoding="utf-8")
    team = (ROOT / "TEAM.md").read_text(encoding="utf-8")
    goals = (ROOT / "camp-goals.md").read_text(encoding="utf-8")
    from demo_trial import brief

    text = brief()
    five = ("规格目录", "完成定义", "密钥", "PR 模板", "CI")
    ok = 0
    ok += check("TR-01 七天日历", "09-11" in trial and "09-05" in trial)
    ok += check("TR-02 失败态", "口头" in trial and "密钥进 Git" in trial)
    ok += check("TR-03 五件事", all(w in team for w in five) and "规格目录" in trial)
    ok += check("TR-04 demo 不强制同一", "不强制同一" in text and "试行包打印完毕" in text)
    ok += check("TR-05 禁止群里贴需求", "群里贴" in trial and "群里贴" in team)
    ok += check("TR-00 目标已写试行周", "2026-09-05" in goals or "09-05" in goals)
    print()
    print(f"{ok}/6 通过")
    if ok < 6:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

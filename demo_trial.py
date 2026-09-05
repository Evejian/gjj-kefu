"""把 L4 试行一页打到终端，方便转发给同事。无交互。"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BRIEF = ROOT / "docs" / "l4-trial.md"


def brief():
    body = BRIEF.read_text(encoding="utf-8")
    team = (ROOT / "TEAM.md").read_text(encoding="utf-8")
    head = [
        "=== L4 公约试行 · 一页纸 ===",
        "不强制同一 Agent。只统一：规格目录 / Ready / 密钥与人合并 / PR 模板 / CI。",
        "禁止：群里贴长聊天当需求。",
        "",
    ]
    return "\n".join(head) + body + f"\n\nTEAM.md {len(team)} 字。试行包打印完毕。\n"


def main():
    print(brief())


if __name__ == "__main__":
    main()

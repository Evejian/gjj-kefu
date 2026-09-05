"""结营讲稿：8 分钟提纲 + 3 分钟「卖什么」。无交互。"""
from pathlib import Path

from saas import landing

ROOT = Path(__file__).resolve().parent


def talk():
    goals = (ROOT / "camp-goals.md").read_text(encoding="utf-8")
    retro = (ROOT / "docs" / "camp-retro.md").read_text(encoding="utf-8")
    parts = [
        "=== 8分钟 · 开营目标（原话） ===",
        "公积金智能客服可值守 + Issue→PR + 假付费闭环；另一个人能按 README 跑起来。",
        "升级三层：会交系统、团队快、能卖。",
        "",
        "=== 8分钟 · 证据 ===",
        "python scripts/gate_ready.py",
        "python demo_saas.py",
        "python demo_agent.py",
        "",
        "=== 3分钟 · 卖什么（非技术） ===",
        landing(),
        "测试支付验证闭环，不是已盈利。下线：GJJ_KILL_SWITCH=1",
        "",
        "=== 8分钟 · 最大失败 ===",
        "扫描 PDF 当正文 + FAQ 过时数字。修正：表征测试锁 retrieval；政策对原文。",
        "",
        "=== 8分钟 · 杠杆 ===",
        "规格进仓库 + 测试绿 + 人点合并；不把希望押在更强补全模型上。",
        "",
        f"camp-goals {len(goals)} 字；camp-retro {len(retro)} 字。",
        "结营讲稿打印完毕。",
    ]
    return "\n".join(parts)


def main():
    print(talk())


if __name__ == "__main__":
    main()

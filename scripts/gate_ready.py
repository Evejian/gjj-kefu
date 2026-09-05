"""本地完成门禁：任一测试红则 exit 1。声称 Ready / 开修复 PR 前必跑。"""
import subprocess
import sys

COMMANDS = [
    ["python", "test_retrieve.py"],
    ["python", "test_main_path.py"],
    ["python", "test_characterization.py"],
    ["python", "test_faq_stats.py"],
    ["python", "test_agent.py"],
    ["python", "test_ticket_store.py"],
    ["python", "test_billing.py"],
    ["python", "test_wrap.py"],
    ["python", "test_trial.py"],
]


def main():
    failed = []
    for cmd in COMMANDS:
        print(f"\n>>> {' '.join(cmd)}")
        r = subprocess.run(cmd)
        if r.returncode != 0:
            failed.append(" ".join(cmd))
    print()
    if failed:
        print("门禁未通过（禁止声称完成）：")
        for f in failed:
            print(f"  - {f}")
        return 1
    print(f"门禁通过：{len(COMMANDS)}/{len(COMMANDS)} 套测试全绿")
    return 0


if __name__ == "__main__":
    sys.exit(main())

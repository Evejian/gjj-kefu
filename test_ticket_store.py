"""工单存储表征：非法 / 非列表 tickets 文件不得拖垮转人工。"""
import json
import tempfile
from pathlib import Path

from ticket_store import create_ticket

results = []


def check(name, cond):
    results.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name)


def tmp_file(content):
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8")
    f.write(content)
    f.close()
    return f.name


def cleanup(path):
    try:
        Path(path).unlink(missing_ok=True)
    except OSError:
        pass


# TS-01 空数组正常
path = tmp_file("[]")
try:
    t = create_ticket("投诉测试", "escalate", token="demo-user-1", tickets_path=path)
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    check(
        "TS-01 空数组可写",
        t.get("ticket_id", "").startswith("T") and len(data) == 1,
    )
finally:
    cleanup(path)

# TS-02 文件是 {}（非列表）——修复前会 AttributeError
path = tmp_file("{}")
try:
    t = create_ticket("投诉", "escalate", tickets_path=path)
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    check(
        "TS-02 非列表容错",
        t.get("ticket_id", "").startswith("T") and isinstance(data, list) and len(data) == 1,
    )
except Exception as exc:  # noqa: BLE001
    check("TS-02 非列表容错", False)
    print(f"  复现报错：{type(exc).__name__}: {exc}")
finally:
    cleanup(path)

# TS-03 非法 JSON
path = tmp_file("not-json{{{")
try:
    t = create_ticket("转人工", "escalate", tickets_path=path)
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    check(
        "TS-03 非法JSON容错",
        t.get("ticket_id", "").startswith("T") and isinstance(data, list) and len(data) == 1,
    )
except Exception as exc:  # noqa: BLE001
    check("TS-03 非法JSON容错", False)
    print(f"  复现报错：{type(exc).__name__}: {exc}")
finally:
    cleanup(path)

failed = [n for n, ok in results if not ok]
print()
print(f"{len(results) - len(failed)}/{len(results)} 通过")
if failed:
    raise SystemExit(1)

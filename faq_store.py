"""FAQ 唯一读取入口。"""
import json
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent / "faq.jsonl"


def load_faqs(path=None):
    faq_path = Path(path) if path else DEFAULT_PATH
    items = []
    with faq_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items

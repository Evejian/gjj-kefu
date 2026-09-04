# Issue 0001 · tickets.json 非法内容导致转人工崩溃

> L8 当堂已知 bug（用于 `/fix-issue` 流水线演示）  
> 状态：待修 → 见 `test_ticket_store.py`

## 现象
转人工（`create_ticket`）在 `data/tickets.json` 已存在但内容不是 JSON 数组时崩溃：
- 文件为 `{}` → `AttributeError: 'dict' object has no attribute 'append'`
- 文件为非法 JSON → `json.JSONDecodeError`

## 复现
```bash
python -c "from pathlib import Path; Path('data/_bad_tickets.json').write_text('{}', encoding='utf-8'); from ticket_store import create_ticket; create_ticket('投诉', 'escalate', tickets_path='data/_bad_tickets.json')"
```

## 期望
损坏或非列表内容时，视为空列表并成功写入新工单（或明确报错且不拖垮 Agent 主路径）。本期选择：**容错重置为空列表并继续**。

## 验收
- `python test_ticket_store.py` 覆盖非法 JSON / 非列表
- 全量回归绿
- 人审 PR 后合并（等级 1）

# 03 · 数据存在哪

| 数据 | 位置 | 说明 |
|------|------|------|
| FAQ 知识库 | `faq.jsonl` | 每行 `{"q","a","src"}`，UTF-8；坏行应跳过（当前实现：`json.loads` 遇坏行会抛——见雷区） |
| 政策原文 | `zcwj/*.pdf` | 多为扫描件；FAQ 由人工/OCR 提炼，**运行时不读 PDF** |
| 密钥 | 环境变量 `ZHIPU_API_KEY` | 不进 Git；CI 只跑 mock/测试 |
| 规格与任务 | `docs/*.md` | 需求进仓库，不进群聊长记录 |

## 改 FAQ 的规矩

1. `src` 必须能对应 `zcwj/` 里某文件名（或明确登记过的来源）
2. 改完跑 `test_retrieve.py` + `test_characterization.py`
3. 政策数字变更要对照最新通知，不要凭记忆改额度

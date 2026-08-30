# Tasks · 检索优化（top 3 + 打分修正）

每条任务对应一个测试或一个点击路径。一次一件事。

## Task-01 检索测试先行（TDD）
先写 `test_retrieve.py`，覆盖 Spec 的 UC-01 ~ UC-05。
此时 `retrieval.py` 尚不存在 → 测试必须跑不通（红）。
验证：`python test_retrieve.py` 报 ImportError 或失败。

## Task-02 实现 retrieval.py
按 Spec 接口实现 `score` / `get_top3` / `format_refs`。
验证：`python test_retrieve.py` 全绿（绿）。

## Task-03 faq_demo.py 接入
删除文件内的旧 retrieve()，改用 `retrieval.get_top3`；
prompt 用 `format_refs` 拼多条参考资料；空结果拒答不调 API。
验证：`python -m py_compile faq_demo.py` 通过 + 手工跑一次主路径。

## Task-04 收尾
README 状态更新；延后项（语义检索、FAQ 补齐）登记 docs/backlog.md；
对照 Spec 的 System Ready 清单逐项打勾。
验证：清单全勾，当日 commit。

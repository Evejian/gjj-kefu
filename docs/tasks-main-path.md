# Tasks · 主路径可演示闭环

## Task-01 测试先行
写 `test_main_path.py`，覆盖 Spec MP-01 ~ MP-04。  
验证：先失败（尚无 answer 模块）再变绿。

## Task-02 实现 answer.py
按状态机实现 `answer()`。  
验证：`python test_main_path.py` 全绿。

## Task-03 demo + 接入 faq_demo
写 `demo_main_path.py`（MP-05）；`faq_demo.py` 改为调用 `answer()`。  
验证：`python demo_main_path.py` 退出码 0；`python -m py_compile faq_demo.py`。

## Task-04 收尾
更新 README / CODEMAP / camp-goals；CI 增加 `test_main_path.py`；对照 Spec Ready 打勾。  
验证：当日 commit + PR。

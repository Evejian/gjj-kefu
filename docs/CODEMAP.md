# 仓库地图（CODEMAP）

公积金智能客服：个贷政策问答。核心链路 = FAQ 导入 → 检索 top3 → 带引用回答。

## 目录结构

```
gjj-kefu/
├── CLAUDE.md            # 项目宪法（Agent 必读）
├── TEAM.md              # 团队 AI 编程公约 v0.1（不绑厂商）
├── README.md            # 三步跑起来
├── camp-goals.md        # 行动营目标
├── faq.jsonl            # FAQ 知识库（每行一条 q/a/src）
├── retrieval.py         # 检索：打分(汉字+数字重合) → top3 → 拼参考资料
├── answer.py            # 问答状态机（拒答/mock/live/no_key/api_error）
├── demo_main_path.py    # 非交互三态演示
├── faq_demo.py          # 交互入口（auto：有密钥 live，否则 mock）
├── test_retrieve.py     # 检索测试（8用例）
├── test_main_path.py    # 主路径状态机测试（4用例）
├── test_api.py          # API 连通性测试
├── zcwj/                # 政策原文 PDF（FAQ 的提炼来源，11 份）
├── docs/
│   ├── prd.md / spec.md / tasks.md          # 检索优化（已完成）
│   ├── prd-main-path.md / spec-main-path.md / tasks-main-path.md  # 主路径闭环
│   ├── backlog.md / CODEMAP.md / ten-x.md
├── .github/             # PR 模板 + CI（检索+主路径+演示+密钥扫描）
└── .claude/             # Harness：skills / commands / agents / hooks
```

## 改动从哪下手

| 要改什么 | 入口 |
|---|---|
| 检索逻辑 / 打分规则 | retrieval.py + test_retrieve.py 先加用例 |
| 问答状态 / 失败可恢复 | answer.py + test_main_path.py |
| prompt / live 调用 | answer.py 的 `_live_text` |
| 加 FAQ | faq.jsonl 追加，出处必须对应 zcwj/ 里的文件名 |
| 新需求 | 走 docs/ 的 PRD→Spec→Tasks 流程（用 spec-start skill） |
| 团队协作规矩 | TEAM.md + .github/ PR 模板与 CI |

## 怎么跑

```
pip install openai
python test_retrieve.py && python test_main_path.py && python demo_main_path.py
# 有密钥后再：
export ZHIPU_API_KEY=...   # PowerShell: $env:ZHIPU_API_KEY=...
python faq_demo.py
```

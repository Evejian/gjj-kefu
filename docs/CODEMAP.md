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
├── faq_demo.py          # 主入口：读FAQ → get_top3 → 调GLM → 带出处回答
├── test_retrieve.py     # 检索测试（8用例，python test_retrieve.py 全绿）
├── test_api.py          # API 连通性测试
├── zcwj/                # 政策原文 PDF（FAQ 的提炼来源，11 份）
├── docs/
│   ├── prd.md           # 需求：检索优化（已完成）
│   ├── spec.md          # 规格：接口、验收用例、Ready 清单
│   ├── tasks.md         # 任务拆分（每条带验证）
│   ├── backlog.md       # 延后项登记
│   ├── CODEMAP.md       # 本文件
│   └── ten-x.md         # L3：消灭的重复动作
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md  # 含 Agent 贡献说明
│   └── workflows/ci.yml          # 测试 + 密钥扫描
└── .claude/             # Harness：skills / commands / agents / hooks
```

## 改动从哪下手

| 要改什么 | 入口 |
|---|---|
| 检索逻辑 / 打分规则 | retrieval.py + test_retrieve.py 先加用例 |
| prompt / 回答格式 | faq_demo.py 第 3 段 |
| 加 FAQ | faq.jsonl 追加，出处必须对应 zcwj/ 里的文件名 |
| 新需求 | 走 docs/ 的 PRD→Spec→Tasks 流程（用 spec-start skill） |
| 团队协作规矩 | TEAM.md + .github/ PR 模板与 CI |

## 怎么跑

```
pip install openai
export ZHIPU_API_KEY=...   # PowerShell: $env:ZHIPU_API_KEY=...
python test_retrieve.py    # 测试
python faq_demo.py         # 主程序（交互式输入问题）
```

# 仓库地图（CODEMAP）

公积金智能客服：个贷政策问答。核心链路 = FAQ 导入 → 检索 top3 → 带引用回答。

接手说明（启动/雷区/不敢动）见 [`wiki/`](wiki/)。

## 目录结构

```
gjj-kefu/
├── CLAUDE.md / TEAM.md / README.md / camp-goals.md
├── faq.jsonl / zcwj/
├── faq_store.py         # FAQ 唯一读取
├── faq_stats.py         # 只读统计（安全区）
├── retrieval.py         # 检索打分 top3
├── answer.py            # 问答状态机
├── demo_main_path.py / faq_demo.py
├── test_retrieve.py / test_main_path.py
├── test_characterization.py / test_faq_stats.py
├── docs/wiki/           # L6 Repo Wiki
├── docs/*-main-path.md / docs/prd|spec|tasks|backlog|ten-x.md
├── .github/             # PR 模板 + CI
└── .claude/             # Harness
```

## 改动从哪下手

| 要改什么 | 入口 |
|---|---|
| 检索逻辑 / 打分规则 | 先扩 test_characterization.py，再改 retrieval.py |
| 问答状态 | answer.py + test_main_path.py |
| 读 FAQ | 只改 faq_store.py |
| 只读统计 | faq_stats.py（勿塞进 answer） |
| 加 FAQ | faq.jsonl，对照 zcwj/ |
| 接手知识 | docs/wiki/ 与本文件一起改 |

## 怎么跑

```
pip install openai
python test_retrieve.py && python test_main_path.py && python test_characterization.py && python test_faq_stats.py
python demo_main_path.py && python faq_stats.py
```

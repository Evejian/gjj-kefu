# 02 · 核心入口

## 调用链

```
用户问题
  → faq_demo.py / demo_main_path.py
      → faq_store.load_faqs()          # 读 faq.jsonl
      → answer.answer(...)             # 状态机
          → retrieval.get_top3(...)    # 汉字+数字重合打分，MIN_SCORE=4
          → mock 拼接 | live 调 GLM | rejected | no_key | api_error
```

## 入口文件为什么存在

| 文件 | 为什么存在 |
|------|------------|
| `faq_demo.py` | 给人交互演示；有 key 走 live，否则 auto→mock |
| `demo_main_path.py` | 给 CI / 评审：无交互一次跑成功/拒答/API失败 |
| `answer.py` | 把「检索后怎么办」收成状态机，避免入口脚本分叉逻辑 |
| `retrieval.py` | 纯函数检索，便于表征测试锁行为 |
| `faq_store.py` | 唯一读 FAQ 的地方，避免四处 `open("faq.jsonl")` |
| `faq_stats.py` | 只读统计（L6 安全区小需求），不碰回答逻辑 |

## 状态机（摘要）

见 `docs/spec-main-path.md`。核心约定：无检索结果 **绝不** 调模型。

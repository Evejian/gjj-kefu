# 公积金智能客服系统

广州公积金个贷政策咨询问答。核心链路：文档/FAQ 导入 → 检索 → 带引用回答。

## 5 分钟跑通（新人路径）

先读 [`docs/wiki/`](docs/wiki/)（启动 / 入口 / 数据 / 雷区）。然后：

```bash
pip install openai
python test_retrieve.py
python test_main_path.py
python test_characterization.py
python test_faq_stats.py
python demo_main_path.py
python faq_stats.py
```

不需要密钥即可验收。有密钥后再交互：

```powershell
$env:ZHIPU_API_KEY="你的key"   # bigmodel.cn，勿写入仓库
python faq_demo.py
```

## 目录说明

| 文件 / 目录 | 作用 |
|---|---|
| `docs/wiki/` | 接手说明（L6）：如何启动、入口、数据、不敢动清单 |
| `faq_store.py` | FAQ 唯一读取入口 |
| `faq_stats.py` | 只读：按来源统计 FAQ |
| `faq.jsonl` / `zcwj/` | 知识库与政策原文 |
| `retrieval.py` / `answer.py` | 检索 + 问答状态机 |
| `demo_main_path.py` / `faq_demo.py` | 非交互演示 / 交互入口 |
| `test_*.py` | 检索、主路径、表征、统计 |
| `TEAM.md` / `.github/` | 团队公约 + CI |

## 当前状态

- [x] FAQ 17 条 + 检索 top3 + 弱匹配拒答
- [x] 团队落地（L4）+ 主路径三态演示（L5 适配）
- [x] 祖传迭代流程（Day7/L6）：Wiki + 表征测试 + `faq_store` 去重重构 + 只读 `faq_stats`

## 协作

新人：`docs/wiki/` → `TEAM.md` → 开 PR。改打分/阈值前先看「不敢动清单」。

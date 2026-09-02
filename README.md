# 公积金智能客服系统

广州公积金个贷政策咨询问答。核心链路：文档/FAQ 导入 → 检索 → 带引用回答。

## 5 分钟跑通（新人路径）

```bash
pip install openai
python test_retrieve.py      # 检索 8/8
python test_main_path.py     # 主路径状态机 4/4
python demo_main_path.py     # 无交互：成功 / 拒答 / API失败 三态
```

不需要密钥即可看完主路径。有密钥后再交互体验真实模型：

```powershell
$env:ZHIPU_API_KEY="你的key"   # bigmodel.cn 控制台复制，勿写入仓库
python faq_demo.py             # 问「我能贷多少」→ 带出处；无关问题拒答
```

## 目录说明

| 文件 / 目录 | 作用 |
|---|---|
| `faq.jsonl` | FAQ 知识库，每行一条 `{"q": 问题, "a": 答案, "src": 出处文件名}` |
| `zcwj/` | 政策原文 PDF（FAQ 的提炼来源） |
| `answer.py` | 问答状态机：拒答 / mock作答 / live / 缺密钥 / API失败 |
| `demo_main_path.py` | 非交互演示三态（对应 L5「成功+失败可恢复」） |
| `faq_demo.py` | 交互入口：有密钥走 live，否则自动 mock |
| `retrieval.py` | 检索模块（打分 + top3，规格见 docs/spec.md） |
| `test_retrieve.py` / `test_main_path.py` | 检索与主路径测试 |
| `TEAM.md` | 团队 AI 编程公约 |
| `.github/` | PR 模板 + CI |

## 当前状态

- [x] FAQ 17 条 + 检索 top3 + 弱匹配拒答（MIN_SCORE=4）
- [x] 团队落地（L4）：TEAM.md + PR 模板 + CI
- [x] 主路径可演示（Day6/L5 适配）：状态机 + mock 成功/拒答/API失败，无密钥也能验收

## 协作（团队）

新人先读 `TEAM.md`。开 PR 会自动套用模板；合并前 CI 必须绿。规格见 `docs/prd-main-path.md` / `docs/spec-main-path.md`。

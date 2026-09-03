# 01 · 如何启动

## 环境

- Python 3.10+（CI 用 3.12）
- 依赖：`pip install openai`（仅 live 调智谱时需要；mock / 测试可不装也能跑检索与状态机测试——但 `answer.py` live 分支会 import openai）

## 无密钥验收（推荐新人第一条路径）

在仓库根目录：

```bash
python test_retrieve.py
python test_main_path.py
python test_characterization.py
python demo_main_path.py
python faq_stats.py
```

期望：测试全绿；演示输出三种状态；统计打印 FAQ 条数与按来源汇总。

## 有密钥交互

```powershell
$env:ZHIPU_API_KEY="你的key"   # 来自 bigmodel.cn，禁止写入仓库
python faq_demo.py
```

问「我能贷多少」应带出处；问天气应拒答。

## 不要做的事

- 不要把 key 写进 `.env` 再 `git add`（Hook / CI 会拦）
- 不要跳过测试直接改 `retrieval.py` 的打分规则

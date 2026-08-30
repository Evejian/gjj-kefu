# 公积金智能客服系统

广州公积金个贷政策咨询问答。核心链路：文档/FAQ 导入 → 检索 → 带引用回答。

## 目录说明

| 文件 / 目录 | 作用 |
|---|---|
| `faq.jsonl` | FAQ 知识库，每行一条 `{"q": 问题, "a": 答案, "src": 出处文件名}` |
| `zcwj/` | 政策原文 PDF（FAQ 的提炼来源） |
| `faq_demo.py` | 主程序：读 FAQ → 检索最相关 1 条 → 调模型带出处回答 |
| `test_api.py` | API 连通性测试脚本 |

## 三步跑起来

**第 1 步：装依赖（在项目目录下）**

```
pip install openai
```

**第 2 步：设置密钥**

先到 bigmodel.cn 控制台注册并复制 API Key（不要写进代码，防止提交到仓库泄露）：

```bash
# Git Bash / Linux
export ZHIPU_API_KEY="你的key"
```

```powershell
# Windows PowerShell
$env:ZHIPU_API_KEY="你的key"
```

**第 3 步：运行**

```
python faq_demo.py
```

输入问题（例如"我能贷多少"），程序会检索最相关的 FAQ 并让模型（glm-4.7-flash，免费）基于它回答，末尾注明依据的政策文件。检索不到相关政策时会直接提示。

可先跑 `python test_api.py` 验证网络和密钥是否正常。

## 当前状态

- [x] FAQ 导入（已 4 条，目标 10~20 条，来源见 `zcwj/`）
- [x] 检索 + 带引用回答（关键词字符重合度，取 top 1）
- [ ] FAQ 补齐 + 检索效果优化（top 3）

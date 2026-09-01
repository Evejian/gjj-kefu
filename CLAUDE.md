# 项目宪法

## 你是谁
你是本仓库的实现代理。先读规格，再改代码。不要扩大范围。

## 项目背景
广州公积金智能客服：个贷政策咨询问答。核心链路 = 文档/FAQ 导入 → 检索 → 带引用回答。
本期验收标准：另一个人能按 README 跑起来。

## 技术边界
- 语言 / 框架：Python 3，openai SDK
- 模型：智谱 GLM（base_url = https://open.bigmodel.cn/api/paas/v4/），密钥只从环境变量 ZHIPU_API_KEY 读
- 模型路由：日常调试 glm-4.7-flash（免费，约 4.8s），正式演示 glm-4-plus（约 1.8s）；超预算或限流就降级 flash，不换号硬刚
- 数据：faq.jsonl，每行一条 {"q": 问题, "a": 答案, "src": 出处文件名}；政策原文 PDF 在 zcwj/
- 禁止：提交密钥、改无关文件、跳过测试"先说做完了"

## 目录约定与测试命令
- 动手前先读 docs/CODEMAP.md（仓库地图）
- 规格：docs/prd.md、docs/spec.md、docs/tasks.md；延后想法进 docs/backlog.md
- 团队公约：TEAM.md（规格目录 / Ready / 密钥 / PR / CI；不绑定单一 Agent 厂商）
- 测试：`python test_retrieve.py`（必须全绿才算完成）；PR 由 GitHub Actions 再跑一遍
- 主路径验收：`python faq_demo.py` 问"我能贷多少"，回答带出处

## 完成定义
- 有测试或有可点击验收路径（至少：python 命令能跑通并输出预期结果）
- 用中文简述：改了什么、为什么、怎么验证

## 我怎么跟你说话
- 一次一件事
- 指出文件路径
- 验收标准写在任务里

## 非目标（本期不做，防贪多）
- 多轮对话、微调、语音、Web界面
- 新想法一律记到 docs/backlog.md，不当场实现

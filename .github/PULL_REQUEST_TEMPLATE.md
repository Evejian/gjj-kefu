## 改动

- 

## 风险

- [ ] 无行为变化（文档 / 配置）
- [ ] 检索 / 拒答逻辑有变（必须补或改测试）
- [ ] 涉及密钥、依赖、对外 API

说明：

## 怎么测

```bash
python test_retrieve.py
# 预期：全绿

# 若动到主路径，再跑（需本机已设 ZHIPU_API_KEY）：
# python faq_demo.py
# 问「我能贷多少」→ 回答带出处
```

## Agent 贡献说明

- 使用的工具 / 壳：（例：Claude Code / Cursor Agent / Codex / 无）
- Agent 写了哪些文件或步骤：
- 人做了哪些裁剪 / 否决 / 手工验收：

> 全手写也请填本栏，写「无，人工实现」，方便团队复盘。

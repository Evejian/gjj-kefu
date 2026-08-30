对照当前需求的 System Ready 清单自检，报告达标情况。步骤：

1. 读 docs/spec.md 里的 System Ready 清单
2. 逐项实际验证，不许只看代码就说通过：
   - 测试：真的跑 `python test_retrieve.py`，贴出结果
   - 失败态：用无关问题验证拒答路径
   - 主路径：检查语法编译 + 让用户跑真实 API
3. 输出打勾表 + 未达标项的原因和补救动作
4. 全绿才算 Ready；未达标项不许勾

对照当前需求的 System Ready 清单自检，报告达标情况。步骤：

1. 读相关 Spec（检索 / 主路径 / Agent）里的 System Ready 清单
2. **先跑门禁**：`python scripts/gate_ready.py`  
   - 未全绿：**禁止**勾选 Ready，贴出失败命令与日志
3. 逐项实际验证，不许只看代码就说通过：
   - 失败态 / 主路径 / Agent 演示按清单点
4. 输出打勾表 + 未达标项的原因和补救动作
5. 全绿才算 Ready；未达标项不许勾

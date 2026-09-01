# Spec · 主路径状态机（问答一根针）

## 模块

新建 `answer.py`：承接「检索 → 决定状态 → 产出回答文本」。  
`demo_main_path.py` 非交互演示；`faq_demo.py` 改为调用同一套逻辑（交互壳保留）。

## 状态机

```
输入问题
  → 检索 get_top3
       ├─ 无结果 ──────────────────► rejected（拒答，不调模型）
       └─ 有参考资料
            ├─ mode=mock ──────────► answered（用 FAQ 原文拼接 + 来源）
            └─ mode=live
                 ├─ 无 ZHIPU_API_KEY ► no_key（提示如何设置，不调用）
                 ├─ API 成功 ───────► answered
                 └─ API 抛错 ───────► api_error（提示可重试 / 改 mock）
```

| 状态 | 含义 | 用户可见 |
|------|------|----------|
| `rejected` | 无相关政策 | `抱歉，暂时没有查到相关政策` |
| `answered` | 成功作答 | 正文 + 来源；mock 时标注 `[mock]` |
| `no_key` | 要走 live 但缺密钥 | 明确提示设置 `ZHIPU_API_KEY`，可改用 mock |
| `api_error` | live 调用失败 | 简短错误说明 + 可改用 mock |

## 接口

```python
def answer(question: str, faqs: list[dict], *, mode: str = "auto",
           client=None, model: str = "glm-4.7-flash",
           force_api_error: bool = False) -> dict:
    # 返回 {"state", "text", "refs"}
    # mode: "auto" | "mock" | "live"
    #   auto = 有密钥则 live，否则 mock（便于无 key 演示）
    # force_api_error 仅测试/演示注入失败态
```

## 验收用例

| 编号 | 输入 | 预期 |
|------|------|------|
| MP-01 | q=我能贷多少, mode=mock | state=answered，text 含政策要点或 FAQ 原文，且含来源文件名 |
| MP-02 | q=今天天气怎么样, mode=mock | state=rejected |
| MP-03 | q=我能贷多少, mode=live, 无 key | state=no_key |
| MP-04 | q=我能贷多少, mode=live, force_api_error=True | state=api_error |
| MP-05 | demo 脚本一次跑完 MP-01/02/04 三类，退出码 0 | 标准输出含三种状态标签 |

## System Ready

- [x] `python test_main_path.py` 全绿
- [x] `python demo_main_path.py` 无交互跑通三态
- [x] `python test_retrieve.py` 仍全绿
- [x] README 含 5 分钟路径；无密钥明文

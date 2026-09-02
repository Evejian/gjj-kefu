"""问答主路径：检索 → 状态机 → 回答文本。"""
import os
from retrieval import get_top3, format_refs

REJECT_TEXT = "抱歉，暂时没有查到相关政策"


def _mock_text(refs: list) -> str:
    body = "\n\n".join(f"{item['a']}" for item in refs)
    sources = "、".join(dict.fromkeys(item["src"] for item in refs))
    return f"[mock]\n{body}\n\n来源：{sources}"


def _live_text(question: str, refs: list, client, model: str) -> str:
    resp = client.chat.completions.create(
        model=model,
        temperature=0.1,
        messages=[
            {
                "role": "system",
                "content": (
                    "你是广州公积金客服助手。只能根据下面提供的参考资料回答，"
                    "回答末尾单独一行注明来源文件。\n\n"
                    f"参考资料：\n{format_refs(refs)}"
                ),
            },
            {"role": "user", "content": question},
        ],
    )
    return resp.choices[0].message.content


def answer(
    question: str,
    faqs: list,
    *,
    mode: str = "auto",
    client=None,
    model: str = "glm-4.7-flash",
    force_api_error: bool = False,
) -> dict:
    """返回 {"state", "text", "refs"}。mode: auto | mock | live。"""
    refs = get_top3(question, faqs)
    if not refs:
        return {"state": "rejected", "text": REJECT_TEXT, "refs": []}

    if mode == "auto":
        mode = "live" if os.environ.get("ZHIPU_API_KEY") else "mock"

    if mode == "mock":
        return {"state": "answered", "text": _mock_text(refs), "refs": refs}

    if mode != "live":
        raise ValueError(f"未知 mode: {mode}")

    if not os.environ.get("ZHIPU_API_KEY"):
        return {
            "state": "no_key",
            "text": "未设置环境变量 ZHIPU_API_KEY。可先跑 python demo_main_path.py（默认 mock），或设置密钥后再用 live。",
            "refs": refs,
        }

    if force_api_error:
        return {
            "state": "api_error",
            "text": "调用模型失败（演示注入）。可重试，或改用 mock：python demo_main_path.py",
            "refs": refs,
        }

    try:
        if client is None:
            from openai import OpenAI

            client = OpenAI(
                api_key=os.environ["ZHIPU_API_KEY"],
                base_url="https://open.bigmodel.cn/api/paas/v4/",
            )
        text = _live_text(question, refs, client, model)
        return {"state": "answered", "text": text, "refs": refs}
    except Exception as exc:  # noqa: BLE001 — 主路径需要吞掉 SDK 差异，统一成 api_error
        return {
            "state": "api_error",
            "text": f"调用模型失败：{exc}。可重试，或改用 mock：python demo_main_path.py",
            "refs": refs,
        }

import os
import json
import time
from openai import OpenAI
from retrieval import get_top3, format_refs

  # ---------- 第 1 段：读入 FAQ ----------
faqs = []
with open("faq.jsonl", encoding="utf-8") as f:
      for line in f:
          line = line.strip()
          if line:
              faqs.append(json.loads(line))

  # ---------- 第 2 段：检索（见 retrieval.py，测试见 test_retrieve.py） ----------

  # ---------- 第 3 段：组装 prompt 调 API ----------
client = OpenAI(
      api_key=os.environ["ZHIPU_API_KEY"],
      base_url="https://open.bigmodel.cn/api/paas/v4/"
  )

question = input("你的问题：")
refs = get_top3(question, faqs)
if not refs:
    print("抱歉，暂时没有查到相关政策")
else:
    t0 = time.time()
    resp = client.chat.completions.create(
        model="glm-4-plus",#glm-4-plus glm-4-flash
        temperature=0.1, # 随机性，0~2，越低越稳定
        #max_tokens=1024,# 回答最长多少 token
        #timeout=30,   # 超时秒数
        messages=[
            {"role": "system", "content": (
                "你是广州公积金客服助手。只能根据下面提供的参考资料回答，"
                "回答末尾单独一行注明来源文件。\n\n"

    f"参考资料：\n{format_refs(refs)}"
            )},
            {"role": "user", "content": question}
        ]
    )
    print(resp.choices[0].message.content)
    print(f"\n[{time.time() - t0:.1f} 秒]")

import json
import time
from answer import answer


faqs = []
with open("faq.jsonl", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            faqs.append(json.loads(line))

question = input("你的问题：")
t0 = time.time()
# auto：有 ZHIPU_API_KEY 走 live，否则 mock，保证没密钥也能看到主路径
result = answer(question, faqs, mode="auto", model="glm-4-plus")
print(result["text"])
if result["state"] == "answered":
    print(f"\n[{time.time() - t0:.1f} 秒] state={result['state']}")
else:
    print(f"\n[state={result['state']}]")

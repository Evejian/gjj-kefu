import time
from answer import answer
from faq_store import load_faqs


faqs = load_faqs()
question = input("你的问题：")
t0 = time.time()
# auto：有 ZHIPU_API_KEY 走 live，否则 mock，保证没密钥也能看到主路径
result = answer(question, faqs, mode="auto", model="glm-4-plus")
print(result["text"])
if result["state"] == "answered":
    print(f"\n[{time.time() - t0:.1f} 秒] state={result['state']}")
else:
    print(f"\n[state={result['state']}]")

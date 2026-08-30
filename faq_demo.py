import os
import json
from openai import OpenAI

  # ---------- 第 1 段：读入 FAQ ----------
faqs = []
with open("faq.jsonl", encoding="utf-8") as f:
      for line in f:
          line = line.strip()
          if line:
              faqs.append(json.loads(line))

  # ---------- 第 2 段：检索（今天你来写） ----------
def retrieve(question, faqs):
      """返回和 question 最相关的那条 FAQ"""
      # 思路：给每条 FAQ 打分，取分最高的
      # 最简单的打分法：字符重合度
      #   把 question 转成字符集合 q_set = set(question)
      #   每条 FAQ 算 len(q_set & set(faq["q"]))，重合越多分越高
      # 提示：max(faqs, key=...) 一步就能取出最高分那条
      #...
      q_set = set(question)
      maxkey=2;
      zfaq={};
      for faq in faqs:
         key=len(q_set & set(faq["q"]))
         if maxkey< key :
            zfaq=faq;
            maxkey=key;
      print("maxkey===========",maxkey)
      if maxkey==2:
         return "None";
      return  zfaq;
         


  # ---------- 第 3 段：组装 prompt 调 API ----------
client = OpenAI(
      api_key=os.environ["ZHIPU_API_KEY"],
      base_url="https://open.bigmodel.cn/api/paas/v4/"
  )

question = input("你的问题：")
best = retrieve(question, faqs)
if best=="None":
    print("抱歉，暂时没有查到相关政策")
else :
    #print("hao")
    resp = client.chat.completions.create(
        model="glm-4.7-flash",
        messages=[
            {"role": "system", "content": (
                "你是广州公积金客服助手。只能根据下面提供的参考资料回答，"
                "回答末尾单独一行注明来源文件。\n\n"

    f"参考资料：\n问：{best['q']}\n答：{best['a']}\n来源：{best['src']}"
            )},
            {"role": "user", "content": question}
        ]
    )
    print(resp.choices[0].message.content)
    

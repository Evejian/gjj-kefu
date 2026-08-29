import os 
from openai import OpenAI

client = OpenAI(
      api_key=os.environ["ZHIPU_API_KEY"],   # 不把密钥写进代码，防止提交到仓库泄露
      base_url="https://open.bigmodel.cn/api/paas/v4/"
  )
resp = client.chat.completions.create(
      model="glm-4.7-flash",                 # 免费模型
      messages=[
          {"role": "system", "content": "你是广州公积金客服助手，回答要准确、简洁。"},
          {"role": "user", "content": "公积金个人住房贷款的利率是多少？"}
      ]
  )


print(resp.choices[0].message.content)
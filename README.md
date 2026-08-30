# 公积金智能客服系统

第 1 步：装 SDK（在项目目录下）

  pip install openai

  第 2 步：写 test_api.py（十几行，今晚的 commit）

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

  第 3 步：设置密钥后运行

  export ZHIPU_API_KEY="你从 bigmodel.cn 控制台复制的key"   # Git Bash / Linux 写法
  python test_api.py

  （如果用 Windows 的 PowerShell，则写 $env:ZHIPU_API_KEY="你的key"）



 1. 导入：从 1-2 份 PDF 里手工提炼 10~20 条 FAQ，存成
  faq.jsonl（每条：问题、答案、出处文件名）——手工提炼
  2. 检索+引用： faq_demo.py：读 faq.jsonl →
  关键词匹配挑出最相关的 3 条 → 拼进 prompt →
  让模型回答时标注“依据：xxx通知”。跑起来问一句“我能贷多少”，看它带不带引用
  3. README：写清楚三步——装什么、设什么环境变量、跑哪条命令。
  第 1 步：装 SDK（在项目目录下）pip install openai
  第 2 步： 
  export ZHIPU_API_KEY="你从 bigmodel.cn 控制台复制的key"   # Git Bash / Linux 写法
  $env:ZHIPU_API_KEY="你的key"  #PowerShell/Windows 写法
  第 3 步：
    python faq_demo.py



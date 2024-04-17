# single_turn.py
import google.generativeai as genai
import os

# genai.configure(api_key=os.getenv("YOUR_API_KEY"))
genai.configure(api_key="YOUR_API_KEY")

# 현재 사용 가능한 모델들 출력하기
print('***Available Model List***')
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')     # gemini-1.5-pro-latest
generation_config = genai.GenerationConfig(temperature=1)
response = model.generate_content("인공지능에 대해 한 문장으로 설명하세요.", generation_config=generation_config)
# print(response)
# print(response._result)
print(response.text)
print(response.candidates[0].content.parts[0].text)
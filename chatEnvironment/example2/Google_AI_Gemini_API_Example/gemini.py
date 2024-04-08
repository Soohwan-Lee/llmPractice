# original sourceL https://github.com/luvris2/python-example/tree/main?tab=readme-ov-file
# https://luvris2.tistory.com/880

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from config import Config

# 서식이 지정된 Markdown 텍스트를 표시하는 함수
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



# 제미나이 API 키 설정
genai.configure(api_key=Config.GOOGLE_API_KEY)



# 사용 가능한 제미나이 프로 모델 리스트 확인
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)



### 제미나이 프로 모델 : 텍스트 전용 ###
# # 모델 설정
# model = genai.GenerativeModel('gemini-pro') # 텍스트 전용 모델

# # 텍스트 생성
# response = model.generate_content("파이썬에 대해 알려줄래?")
# print(response.text)

# # 마크다운 사용
# to_markdown(response.text)

# # 실시간 스트리밍 응답 텍스트 생성
# response = model.generate_content("파이썬에 대해 알려줄래?", stream=True)
# for chunk in response:
#   print(chunk.text)
#   print("_"*80)



### 제미나이 프로 비전 모델 : 이미지와 텍스트 혼합 모델 ###
# # 모델 설정
# model = genai.GenerativeModel('gemini-pro-vision') # 이미지/텍스트 혼합 모델

# # 이미지 관련 패키지 및 이미지 파일 호출
# import PIL.Image
# img = PIL.Image.open('image.jpg') # 다운로드한 이미지 파일

# # 이미지로 텍스트 생성
# response = model.generate_content(img)
# print(response.text)

# # 이미지와 텍스트로 텍스트 생성
# response = model.generate_content(["이 그림이 어떤 그림인지 한국말로 답해줘.", img])
# print(response.text)



### 제미나이 프로 모델로 대화 나누기 ###
# 모델 설정
model = genai.GenerativeModel('gemini-pro')

# 채팅 초기화
chat = model.start_chat(history=[])

# 첫 번째 질문 내용 작성
q1 = input("첫 번째 질문 내용을 입력해주세요. : ")

# 첫 번째 질문 내용에 대한 답변 응답
response = chat.send_message(q1)
print("첫 번째 답변 : " + response.text)

# 두 번째 질문 내용 작성
q2 = input("두 번째 질문 내용을 입력해주세요. : ")

# 두 번째 질문 내용에 대한 답변 응답
response = chat.send_message(q2)
print("두 번째 답변 : " + response.text)



# # 채팅 내역 확인
# print(chat.history)


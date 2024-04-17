import google.generativeai as genai
import os

# genai.configure(api_key=os.getenv("YOUR_API_KEY"))
genai.configure(api_key="YOUR_API_KEY")



model = genai.GenerativeModel('gemini-pro')
chat_session = model.start_chat(history=[]) #ChatSession 객체 반환
user_queries = ["인공지능에 대해 한 문장으로 짧게 설명하세요.", "인공지능의 가능성에 대해 한 문장으로 짧게 설명하세요."]
for user_query in user_queries:
    print(f'[사용자]: {user_query}')   
    response = chat_session.send_message(user_query)
    print(f'[모델]: {response.text}')
# print(response.candidates[0].content.parts[0].text)
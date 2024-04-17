import google.generativeai as genai
import os

# genai.configure(api_key=os.getenv("YOUR_API_KEY"))
genai.configure(api_key="YOUR_API_KEY")


def text_generate_Gemini(chat_session, user_query):
    response = chat_session.send_message(user_query)

    return response.text



def main():
    model = genai.GenerativeModel('gemini-pro')
    chat_session = model.start_chat(history=[]) #ChatSession 객체 반환
    while True:
        user_input = input('User: ')
        gemini_response = text_generate_Gemini(chat_session, user_input)
        print(f"Devil's Advocate: {gemini_response}")


if __name__ == "__main__":
    main()
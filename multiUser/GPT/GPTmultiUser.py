from openai import OpenAI
client = OpenAI(api_key='YOUR-API-KEYS')

def text_generate_GPT(messages):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.8
  )

  bot_response = completion.choices[0].message.content
  messages.append({"role" : "assistant", "content" : f"{bot_response}"})
  print(f'ChatBot: {bot_response}')
  print("="*20)

  return messages


def main():
#   personality = "너는 지금부터 '악마의 대변인'역할이야. 내가 하는 말에 논리적으로 근거를 들어서 반론을 제기해야 해."
#   messages = [{"role" : "system", "content" : f"{personality}"}]
  messages = [
    {
        "role": "system",
        "content": "너는 지금부터 네 사람과 이야기 시작하는거야. Alpha, Bravo, Charlie, Delta라는 이름을 가진 네 사람과 이야기를 하는거야. 너도 이야기에 껴서 흐름에 알맞도록 대화에 참여해야 해."
     },
    {
        "role": "user",
        "name": "Alpha",
        "content": "안녕 브라보! 요즘 잘 지내?"
    },
    {
        "role": "user",
        "name": "Bravo",
        "content": "나는 잘 지내지! 너네는 어때?"
    },
    {
        "role": "user",
        "name": "Charlie",
        "content": "나도 잘 지내지! 나 요즘 다빈치 코드 쓴 작가님 책 읽고 있는데... 작가님 이름 생각이 안나네..."
    },
    {
        "role": "assistant",
        "content": "다빈치 코드의 작가는 댄 브라운이야. 다빈치 코드 외에도 천사와 악마, 그리고 인페르노 등등 재밌는 책들을 많이 쓰셨어."
    }
]

  while True:
    user_id = input('User Name: ')
    user_input = input('User Content: ')
    messages.append({"role" : "user", "name": f"{user_id}", "content" : f"{user_input}"})
    user_id = input('User Name: ')
    user_input = input('User Content: ')
    messages.append({"role" : "user", "name": f"{user_id}", "content" : f"{user_input}"})
    messages = text_generate_GPT(messages)



if __name__ == "__main__":
    main()
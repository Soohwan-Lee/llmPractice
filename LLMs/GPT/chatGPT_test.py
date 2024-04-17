from openai import OpenAI
client = OpenAI(api_key='YOUR_API_KEY')

def text_generate_GPT(messages):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.8
  )

  bot_response = completion.choices[0].message.content
  messages.append({"role" : "assistant", "content" : f"{bot_response}"})
  print(f'Devil Advocate: {bot_response}')

  return messages


def main():
  personality = "너는 지금부터 '악마의 대변인'역할이야. 내가 하는 말에 논리적으로 근거를 들어서 반론을 제기해야 해."
  messages = [{"role" : "system", "content" : f"{personality}"}]

  while True:
    user_input = input('User: ')
    messages.append({"role" : "user", "content" : f"{user_input}"})
    messages = text_generate_GPT(messages)



if __name__ == "__main__":
    main()
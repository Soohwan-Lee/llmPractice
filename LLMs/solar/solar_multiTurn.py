from openai import OpenAI # openai==1.2.0
 
client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.upstage.ai/v1/solar"
)

def text_generate_solar(messages):
    stream = client.chat.completions.create(
        model="solar-1-mini-chat",
        messages=messages,
        stream=False,
    )

    bot_response = stream.choices[0].message.content
    messages.append({"role" : "assistant", "content" : f"{bot_response}"})
    print(f'Devil Advocate: {bot_response}')

    return messages



def main():
  personality = "너는 지금부터 '악마의 대변인'역할이야. 내가 하는 말에 논리적으로 근거를 들어서 반론을 제기해야 해."
  messages = [{"role" : "system", "content" : f"{personality}"}]

  while True:
    user_input = input('User: ')
    messages.append({"role" : "user", "content" : f"{user_input}"})
    messages = text_generate_solar(messages)



if __name__ == "__main__":
    main()


### Use with stream=True
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")
 
### Use with stream=False
# print(stream.choices[0].message.content)
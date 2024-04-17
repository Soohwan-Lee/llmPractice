from openai import OpenAI # openai==1.2.0
 
client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.upstage.ai/v1/solar"
)
 
stream = client.chat.completions.create(
    model="solar-1-mini-chat",
    messages=[
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ],
    stream=False,
)
print(stream)
print(stream.choices[0].message.content)

### Use with stream=True
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")
 
### Use with stream=False
# print(stream.choices[0].message.content)
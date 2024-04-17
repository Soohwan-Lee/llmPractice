import anthropic

### Posible Models
# claude-3-haiku-20240307
# claude-3-sonnet-20240229
# claude-3-opus-20240229


def text_generate_claude(client, messages):
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        temperature=0,
        system="너는 지금부터 '악마의 대변인'역할이야. 내가 하는 말에 논리적으로 근거를 들어서 반론을 제기해야 해.",
        messages=messages
    )
    
    bot_response = message.content[0].text
    messages.append({"role" : "assistant", "content" : [{"type": "text", "text": f"{bot_response}"}]})
    print(f"Devil's Advocate: {bot_response}")

    return messages


def main():
  client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="YOUR-API-KEY",)
  messages = []

  while True:
    user_input = input('User: ')
    # messages.append({"role" : "user", "content" : f"{user_input}"})
    messages.append({"role" : "user", "content" : [{"type": "text", "text": f"{user_input}"}]})
    messages = text_generate_claude(client, messages)



if __name__ == "__main__":
    main()
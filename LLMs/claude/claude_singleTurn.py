import anthropic

### Posible Models
# claude-3-haiku-20240307
# claude-3-sonnet-20240229
# claude-3-opus-20240229

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="YOUR-API-KEY",
)
message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0,
    system="Today is March 4, 2024.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What are 3 ways to cook apples?"
                }
            ]
        }
    ]
)
print(message.content)
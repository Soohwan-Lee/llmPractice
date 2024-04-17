from openai import OpenAI # openai == 1.2.0

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.upstage.ai/v1/solar"
)

response = client.chat.completions.create(
	model="solar-1-mini-answer-verification",
	messages=[
		{
      "role": "user",
      "content": "Mauna Kea is an inactive volcano on the island of Hawaiʻi. Its peak is 4,207.3 m above sea level, making it the highest point in Hawaii and second-highest peak of an island on Earth."
    },
		{
      "role": "assistant",
      "content": "Mauna Kea is 5,207.3 meters tall."
    }
	]
)

print(response)
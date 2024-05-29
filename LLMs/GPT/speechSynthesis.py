from pathlib import Path
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")

speech_file_path = "./LLMs/GPT/5.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="We evaluated these concepts in technology probes and speed-dating workshops, revealing the need for adaptive designs considering subtle group dynamics."
)

response.stream_to_file(speech_file_path)
from pathlib import Path
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY")

speech_file_path = "./LLMs/GPT/7.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="onyx",
  input="We began our research by examining the existing design space of interactive systems for dance practice. Our starting point was the Dance Interactive Learning System Workflow by Raheb et al., which outlines four key elements: student moving, capturing movement, processing data, and feedback."
)

response.stream_to_file(speech_file_path)
# https://platform.openai.com/docs/assistants/overview?context=without-streaming

from openai import OpenAI
client = OpenAI(api_key="YOUR-API-KEYS")

# Step 1: Create Assistant
assistant = client.beta.assistants.create(
  name="LEMMY",
  instructions="너는 노인들을 위한 소셜 로봇 래미야. 답변은 한국어로 최대한 짧고 간결하게 예의 바르게 응답해. 마지막으로 너는 울산과학기술원에서 만들으니 참고해.",
  model="gpt-4",
)

# Step 2: Create a Thread
thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="너 이름은 뭐고 어디서 만들어졌어?"
)

# Step 3: Add a Message to Thread
# run = client.beta.threads.runs.create(
#     thread_id=thread.id,  # 생성한 스레드 ID
#     assistant_id=assistant.id,  # 적용할 Assistant ID
# )
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="현재 노인 사용자와 대화를 하고 있으니 최대한 짧고 간결하고 친절하게 응답해."
)

messages = client.beta.threads.messages.list(thread_id=thread.id)
print(messages)

# Step 4: Create a Run
if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages)
else:
  print(run.status)
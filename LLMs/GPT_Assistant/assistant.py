import os
import json
from openai import OpenAI
import time

# OPENAI_API_KEY 를 설정합니다.
api_key = "YOUR-API-KEY"

# OpenAI API를 사용하기 위한 클라이언트 객체를 생성합니다.
client = OpenAI(api_key=api_key)

# 인자로 받은 객체의 모델을 JSON 형태로 변환하여 출력
def show_json(obj):
    print(json.loads(obj.model_dump_json()))    # Display

### 1. Assistant 생성 -> 되도록 Playground에서 생성 권장
### 1-1. Assistant ID를 불러옵니다(Playground에서 생성한 Assistant ID)
# ASSISTANT_ID = "asst_V8s4Ku4Eiid5QC9WABlwDsYs"
# print("Assistant ID: " + ASSISTANT_ID)  # Assistant ID 출력

# # OpenAI API를 사용하기 위한 클라이언트 객체를 생성합니다.
# client = OpenAI(api_key=api_key)

# ### 1-2. Assistant 를 생성합니다.
# from openai import OpenAI

# # OpenAI API를 사용하기 위한 클라이언트 객체를 생성합니다.
# client = OpenAI(api_key=api_key)

# # Assistant 를 생성합니다.
# assistant = client.beta.assistants.create(
#     name="Math Tutor",  # 챗봇의 이름을 지정합니다.
#     # 챗봇의 역할을 설명합니다.
#     instructions="You are a personal math tutor. Answer questions briefly, in a sentence or less.",
#     model="gpt-4-turbo-preview",  # 사용할 모델을 지정합니다.
# )

# # 생성된 챗봇의 정보를 JSON 형태로 출력합니다.
# show_json(assistant)
# ASSISTANT_ID = assistant.id
# print("Assistant ID: " + ASSISTANT_ID)    # Assistant ID 출력



### 2. Thread 생성하기
# ### 2-1. 스레드를 이미 생성한 경우
# THREAD_ID = "thread_6We5fHvb5NBuacPfZYkqUWlO"

### 2-2. 스레드를 새롭게 생성합니다.
def create_new_thread():
    # 새로운 스레드를 생성합니다.
    thread = client.beta.threads.create()
    return thread



### 3. Thread에 메시지 생성
# 반복문에서 대기하는 함수
def wait_on_run(run, thread_id):
    while run.status == "queued" or run.status == "in_progress":
        # 3-3. 실행 상태를 최신 정보로 업데이트합니다.
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


def submit_message(assistant_id, thread_id, user_message):
    # 3-1. 스레드에 종속된 메시지를 '추가' 합니다.
    client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=user_message
    )
    # 3-2. 스레드를 실행합니다.
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )
    return run


def get_response(thread_id):
    # 3-4. 스레드에 종속된 메시지를 '조회' 합니다.
    return client.beta.threads.messages.list(thread_id=thread_id, order="asc")


def print_message(response):
    for res in response:
        print(f"[{res.role.upper()}]\n{res.content[0].text.value}\n")


def ask(assistant_id, thread_id, user_message):
    run = submit_message(
        assistant_id,
        thread_id,
        user_message,
    )
    # 실행이 완료될 때까지 대기합니다.
    run = wait_on_run(run, thread_id)
    print_message(get_response(thread_id).data[-2:])
    return run

# # 새로운 스레드를 생성하고 메시지를 제출하는 함수를 정의합니다.
# def create_thread_and_run(user_input):
#     # 사용자 입력을 받아 새로운 스레드를 생성하고, Assistant 에게 메시지를 제출합니다.
#     thread = client.beta.threads.create()
#     run = submit_message(ASSISTANT_ID, thread, user_input)
#     return thread, run


### main function
def main():
    # Assistnat ID
    ASSISTANT_ID = "asst_V8s4Ku4Eiid5QC9WABlwDsYs"

    # 새로운 스레드 생성
    thread = create_new_thread()
    # 새로운 스레드를 생성합니다.
    show_json(thread)
    # 새롭게 생성한 스레드 ID를 저장합니다.
    THREAD_ID = thread.id

    # # 만약 생성해둔 스레드가 있다면?
    # thread_id = "기존 스레드 ID"

    run = ask(ASSISTANT_ID, thread_id, "I need to solve `1 + 20`. Can you help me?")
    print(run)

def all_dialogue(thread_id):
    # 전체 대화내용 출력
    print_message(get_response(thread_id).data[:])
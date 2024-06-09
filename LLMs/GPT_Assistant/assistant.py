import os
import json
from openai import OpenAI
import time

# Set your OpenAI API key 'YOUR_API_KEY'
api_key = "YOUR_API_KEY"

# Create a client object to use the OpenAI API.
client = OpenAI(api_key=api_key)

# Function to display JSON
def show_json(obj):
    print(json.dumps(obj, indent=2))

# # Function to create a new assistant
# def create_assistant():
#     """
#     Creates a new assistant with specific instructions.
#     """
#     response = client.beta.assistants.create(
#         name="Devil's Advocate",
#         instructions="""You are the "devil's advocate" who uses Socratic questioning to help group discussion participants rethink the correctness of their group decisions. Your role is to provide a logical, well-reasoned counterargument to the majority opinion. Engage in critical thinking and challenge assumptions. You are not a participant but a facilitator who helps members critically reflect on their thinking.""",
#         model="gpt-4-turbo-preview"
#     )
#     assistant_id = response.id
#     print(f"Assistant created with ID: {assistant_id}")
#     return assistant_id

# Function to create a new thread
def create_new_thread():
    """
    Creates a new conversation thread.
    """
    thread = client.beta.threads.create()
    return thread

# Function to wait for the run to complete
def wait_on_run(run, thread_id):
    """
    Waits for the run to complete by polling its status.
    """
    while run.status == "queued" or run.status == "in_progress":
        # 3-3. 실행 상태를 최신 정보로 업데이트합니다.
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

# Function to submit a message in the thread
def submit_message(assistant_id, thread_id, user_message):
    """
    Sends a message in the specified thread and starts a run.
    """
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

# Function to get the response messages from the thread
def get_response(thread_id):
    """
    Retrieves the messages from the specified thread.
    """
    return client.beta.threads.messages.list(thread_id=thread_id, order="asc")

# Function to print messages from the response
def print_message(response):
    """
    Prints the messages from the response.
    """
    for res in response.data:
        print(f"[{res.role.upper()}]\n{res.content[0].text.value}\n")

# Function to handle a user's message and get a response
def ask(assistant_id, thread_id, user_message):
    """
    Submits a user's message and retrieves the assistant's response.
    """
    run = submit_message(
        assistant_id,
        thread_id,
        user_message,
    )
    # 실행이 완료될 때까지 대기합니다.
    run = wait_on_run(run, thread_id)
    print_message(get_response(thread_id))
    return run

# Main function to facilitate a multi-turn conversation with the assistant
def main():
    """
    Main function to facilitate a multi-turn conversation with the assistant.
    """
    # Create a new assistant
    # ASSISTANT_ID = create_assistant()
    ASSISTANT_ID = "asst_4Eg0Fv97rAVVnwmnpuXFpCOC"

    # Create a new thread
    thread = create_new_thread()
    show_json(thread.model_dump())  # Use model_dump to get serializable data
    THREAD_ID = thread.id

    user_input = ""
    while user_input.lower() != "exit":
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        run = ask(ASSISTANT_ID, THREAD_ID, user_input)
        # show_json(run.model_dump())  # Use model_dump to get serializable data

if __name__ == "__main__":
    main()

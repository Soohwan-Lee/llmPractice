# https://yhnb3.github.io/2020/11/25/%EC%B1%84%ED%8C%85%EC%84%9C%EB%B2%84/

from socket import *
import argparse
import threading

client_socket = socket(AF_INET, SOCK_STREAM)  
client_socket.connect(('127.0.0.1', 10000))    ## 로컬에서 진행하기 때문에 로컬 주소와 지정된 포트번호로 소켓 생성

parser = argparse.ArgumentParser()             ## 파서를 통해 클라이언트의 이름을 지정할 수 있도록 정의
parser.add_argument('user')
args = parser.parse_args()
user = args.user

print(f'{user} 접속 완료')

def handle_receive(client_socket, user):       ## 서버로 부터 데이터를 받는 함수
    while 1:
        try:
            data = client_socket.recv(1024)    ## 서버로 부터 데이터가 온다면 데이터를 프린트하고 오지 않는 다면 
                                               ## 서버로부터 연결이 끊겼음을 프린트
        except:
            print("연결 끊김")
            break
        data = data.decode()
        if not user in data:
            print(data)

def handle_send(client_socket, user):          ## 서버로 데이터를 전달
    while 1:
        data = input()
        client_socket.sendall(data.encode())
        if data == "/종료":
            break
    client_socket.close()


receive_thread = threading.Thread(target=handle_receive, args=(client_socket, user,))
receive_thread.start()
send_thread = threading.Thread(target=handle_send, args=(client_socket, user))
send_thread.start()
## 데이터를 보내는 것과 받는 것을 멀티 스레드로 지정하여서 서로 각 각 동작할 수 있도록 합니다.

client_socket.sendall(user.encode()) ## 클라이언트 소켓이 정의 된 후 보내는 첫 데이터 유저의 이름을 보냅니다.
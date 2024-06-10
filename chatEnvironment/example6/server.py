# 소켓 프로그래밍
# 클라이언트 - 서버 모델
# 서버

import socket
import threading
import time

HEADER = 64 # 헤더를 고정 길이 64바이트 (첫 세팅)
PORT= 5050
SERVER = "127.0.0.1"  # ipv4
# gethostname: 로컬 호스트 이름, gethostbyname: 컴퓨터의 이름이나 도메인 이름을 통해 ip 가져옴
# SERVER = socket.gethostbyname(socket.gethostname()) # 컴퓨터를 옮길때마다 직접 변경할 필요없음
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECTED_MESSAGE = "!DISCONNECT" #이 메시지가 오면 연결을 종료할 것

# 소켓 객체 생성 socket.socket(패밀리, 소켓타입)
# 패밀리: 주소 체계
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(ADDR) # 호스트이름과 포트번호를 튜플로 전달

# 클라이언트-서버 간의 개별 연결 처리
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # 소켓으로부터 (bufsize 만큼) 데이터 읽음
        # 바이트형식으로 인코딩, UTF형식으로 디코딩
        msg_length = conn.recv(HEADER).decode(FORMAT) #첫번째 메시지가 얼마나 오래 올지
        # 아무것도 안보냈을때 빈 메세지 예외처리
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECTED_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # (소켓, 주소정보) 반환
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # 1:N 연결 생성 가능
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()








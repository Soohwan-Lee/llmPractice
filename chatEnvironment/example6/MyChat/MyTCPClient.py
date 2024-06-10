# 채팅 프로그램 - 클라이언트

import socket

port = int(input("Port Number: "))
address = ("localhost", port) # 서버주소, 포트번호
BUFSIZE = 1024

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect(address)

# r_msg = sock.recv(BUFSIZE).decode()
# print(r_msg)

while True:
    s_msg = input("Mesage to send: ")
    sock.send(s_msg.encode())
    data = sock.recv(1024).decode()
    print(data)

sock.close()
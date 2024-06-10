
import socket
import threading


# SERVER = "192.168.0.69"
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECTED_MESSAGE = "!DISCONNECT"

c_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
c_sock.connect(ADDR)

# class Client(threading.Thread):
#     def __init__(self, server, port):
#         threading.Thread.__init__(self)
#         self.server = server
#         self.port = port
#         self.sock = None
    
#     def run(self):
#         self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
#         self.sock.connect((self.server, self.port))


#     def recv(self):
#         while True:
#             data = self.sock.recv()

def recv():
    while True:
        data = c_sock.recv(1024).decode(FORMAT)
        if data:
            print(data)

recv_thread = threading.Thread(target=recv)
recv_thread.start()


def send():
    # 닉네임 설정
    nickname = input("Your Nickname: ")
    c_sock.send(nickname.encode(FORMAT))

    while True:
        msg = input("")
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))

        c_sock.send(send_length)
        c_sock.send(message)

        # print(c_sock.recv(1024).decode(FORMAT))

send()

import socket
import threading
from  collections import deque


class Room:
    def __init__(self):
        self.clients = [] # 채팅방 클라이언트

    def addClient(self, c):
        self.clients.append(c)

    def delClient(self, c):
        self.clients.remove(c)
                
    def sendAllClients(self, msg):
        for client in self.clients:
                client.sendMsg(msg)


# 서버 1개 - 채팅방 1개
class TCPServer(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.room = Room()
        self.address = (ip, port)
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.sock.bind(self.address)
        self.sock.listen()

    def run(self):
        print("[STARTING] Server is starting...")
        while True:
            conn, addr = self.sock.accept()
            join_client = HandleClient(conn, addr)
            join_client.start()
        self.sock.close()


# 클라이언트 접속
class HandleClient(threading.Thread):
    def __init__(self, conn=None, addr=None):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.nickname = None
        self.connected = True

    def run(self):
        print(f"[NEW CONNECTION] {self.addr} connected.")
        self.nickname = self.conn.recv(1024).decode(FORMAT)
        server.room.addClient(self)
        # print(server.room.clients.nickname)
        server.room.sendAllClients(self.nickname + "님이 입장하였습니다.\n")
        self.recvMsg()
        server.room.delClient(self)
        # print(server.room.clients.nickname)
        server.room.sendAllClients(self.nickname + "님이 퇴장하였습니다.\n")

    def recvMsg(self):
        while self.connected:
            msg_length = self.conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = self.conn.recv(msg_length).decode(FORMAT)

                if not msg or msg == DISCONNECTED_MESSAGE:
                    self.connected = False
                else:
                    print(self.nickname + "] " + msg)
                    server.room.sendAllClients(self.nickname + "] " + msg)

    def sendMsg(self, msg):
        self.conn.send(msg.encode(FORMAT))



if __name__=="__main__":
    # HOST = socket.gethostname()
    # IP = socket.gethostbyname(HOST) # 192.168.0.69
    SERVER = "192.168.0.13"
    # SERVER = socket.gethostbyname(socket.gethostname())
    PORT = 5050
    ADDR = (SERVER, PORT)
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECTED_MESSAGE = "!DISCONNECT"

    server = TCPServer(SERVER, PORT)
    server.start()

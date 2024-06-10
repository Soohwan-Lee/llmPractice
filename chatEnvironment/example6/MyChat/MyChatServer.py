
import socket
import threading
from collections import deque

# 채팅방
class Room:
    def __init__(self):
        self.clients = dict() # 접속한 클라이언트

    def addClient(self, c):
        self.client[c.nicknamec]

    def delClient(self, c):
        self.clients.pop(c.nickname)

    def sendAllCilents(self, msg):
        for client in self.clients:
            client.sendMsg(msg)



# 채팅 서버 오픈
class TCPServer(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.deque = deque() # [from, to, msg]
        self.address = (ip, port)
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.sock.bind(self.address)
        self.sock.listen()

    def run(self):
        print("[STARTING] Server is starting...")
        while True:
            conn, addr = self.sock.accept()
            connection_client = HandleClient(conn, addr)
            connection_client.start()
        self.sock.close()


# 클라이언트 접속 &
class HandleClient(threading.Thread):
    def __init__(self, conn=None, addr=None):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.nickname = None
        self.room = Room()
        self.connected = True

    def run(self):
        print(f"[NEW CONNECTION] {self.addr} connected.")
        self.nickname = self.conn.recv(1024).decode(FORMAT)
        server.room.addClient(self)

    def recvMsg(self):
        while self.connected:
            msg_length = self.conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = self.conn.recv(msg_length).decode(FORMAT)

                if not msg or msg == DISCONNECTED_MESSAGE:
                    self.connected = False
                else:
                    server.deque.append([])
                    print(f"[{self.addr}] {self.nickname}> {msg}")

        # while self.connected:
        #     conn_list = ""
        #     for c in server.room.clients:
        #         conn_list += (c.nickname + " ")
        #     print("[접속자]: " + conn_list)
        #     self.sendMsg("[접속중] " + conn_list)
        #     self.recvMsg()
        # self.conn.close()



    # def sendMsg(self, msg):
    #     self.conn.send(msg.encode(FORMAT))





if __name__ == "__main__":
    SERVER = "192.168.0.69"
    PORT = 5050
    ADDR = (SERVER, PORT)
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECTED_MESSAGE = "!DISCONNECT"

    server = TCPServer(SERVER, PORT)
    server.start()


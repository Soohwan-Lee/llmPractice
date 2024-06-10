# 채팅 프로그램 - 서버
# 사용자 모듈을 작성 - 소켓 생성과 연결을 모듈로 구현

import socket

class TCPServer:
    def __init__(self, ip, port):
        self.address = (ip, port)
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.sock.bind(self.address)
        self.sock.listen(5)

    # 연결을 허용하고 클라이언트 소켓과 주소 반환
    def Accept(self):
        self.c_sock, self.c_addr = self.sock.accept()
        return self.c_sock, self.c_addr


if __name__=='__main__':
    # HOST = socket.gethostname()
    # IP = socket.gethostbyname(HOST) # 192.168.0.69
    IP = 'localhost'
    PORT = 2500

    server_sock = TCPServer(IP, PORT)
    client_sock, client_addr = server_sock.Accept()

    msg = "Hello Client"
    client_sock.send(msg.encode())

    while True:
        try:
            r_msg = client_sock.recv(1024).decode()
            if not r_msg:
                print("정상 종료")
                break
        except:
            print("연결이 끊겼습니다..")
        else:
            print("수신메시지: ", r_msg)

    client_sock.close()


import MyTCPServer as mt
import sys

ip = 'localhost'
port = 2500

# 1보다 크면 포트번호 입력했다는 의미
if len(sys.argv) > 1:
    # port = int(eval(sys.argv[1]))
    port = int(sys.argv[1])

sock = mt.TCPServer(ip, port)
c_sock, c_addr = sock.Accept()

while True:
    print('Connected by ', c_addr[0], c_addr[1])
    data = c_sock.recv(1024)
    if not data:
        break
    print("Received message: ", data.decode())
    c_sock.send(data)

c_sock.close()

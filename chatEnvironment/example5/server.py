# https://yhnb3.github.io/2020/11/25/%EC%B1%84%ED%8C%85%EC%84%9C%EB%B2%84/

from socket import *
import threading

port = 10000

server_socket = socket(AF_INET, SOCK_STREAM) ## 소켓을 정의합니다.
server_socket.bind(('', port))               ## 서버가 정해진 포트번호로 지정된 소켓을 생성합니다.
server_socket.listen(5)                      ## 최대로 들어올 수 있는 소켓 갯수를 지정합니다.

user_list = {}                               ## 채팅 유저관리를 위한 딕셔너리입니다.
def receive(client_socket, addr, user):
    while 1:                                 
        data = client_socket.recv(1024)      ## 클라이언트 소켓에서 데이터를 받아 옵니다.
        string = data.decode()               ## 받아온 데이터는 비트로 인코딩 되있기 때문에 디코딩을 해줍니다. 

        if string == "/종료" :                           
            msg = f'{user.decode()}가 퇴장하였습니다.'
            for con in user_list.values():                    
              try:
                  con.sendall(msg.encode())
              except:
                  print("연결이 비 정상적으로 종료된 소켓 발견")
            print(msg)
            break
        string = "%s : %s"%(user.decode(), string)
        print(string)
        for con in user_list.values():                    ## 채팅에 참여하고 있는 클라이언트들에게 받아온 메시지 전달
            try:
                con.sendall(string.encode())            
            except:
                print("연결이 비 정상적으로 종료된 소켓 발견")
    del user_list[user]                                   ## 채팅서버를 나간 클라이언트는 딕셔너리에서 제거
    client_socket.close()                                 ## 클라이언트 소켓 제거

while True:
    client_socket, addr = server_socket.accept()          ## 클라이언트 소켓 정의
    user = client_socket.recv(1024)                       ## 처음 클라이언트 소켓이 정의되고 난 후 처음 받는 데이터
                                                          ## 클라이언트는 채팅 유저의 이름을 보냅니다.
    user_list[user] = client_socket                       ## 유저 리스트에 유저 추가
    print(f'{user.decode()}가 입장하였습니다.')          

    receive_thread = threading.Thread(target=receive, args=(client_socket, addr,user))
    ## 각각의 클라이언트 서버가 채팅을 따로 치기 위해 각 클라이언트로 부터 데이터를 받고 보내는 부분은 스레드로 정의해줍니다.
    receive_thread.start()
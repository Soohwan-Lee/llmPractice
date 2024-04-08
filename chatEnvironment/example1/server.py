# Refer this blog(original source): https://hyobn.tistory.com/15#%EC%82%AC%EC%9A%A9%20%EB%B0%A9%EB%B2%95-1

# Server

from socket import *
from threading import *
from queue import *
import sys
import datetime

#------------- 서버 세팅 -------------
HOST = '127.0.0.1' # 서버 ip 주소 .
PORT = 9190 # 사용할 포트 번호.
#------------------------------------

s=''
s+='\n  -------------< 사용 방법 >-------------'
s+='\n   연결 종료 : !quit 입력 or ctrl + c    '
s+='\n   참여 중인 멤버 보기 : !member 입력      '
s+='\n   귓속말 보내기 : /w [상대방이름] [메시지]   '
s+='\n'
s+='\n     이 프로그램은 Jupyter Notebook에  '
s+='\n            최적화되어 있습니다.             '
s+='\n  --------------------------------------\n\n'

def now_time():
    now = datetime.datetime.now()
    time_str=now.strftime('[%H:%M] ')
    return time_str

def send_func(lock):
    while True:
        try:
            recv = received_msg_info.get()

            if recv[0]=='!quit' or len(recv[0])==0:  
                msg=str('[SYSTEM] '+now_time()+left_member_name)+'님이 연결을 종료하였습니다.'

            elif recv[0]=='!enter' or recv[0]=='!member':
                now_member_msg='현재 멤버 : '
                for mem in member_name_list:
                    if mem!='-1':
                        now_member_msg+='['+mem+'] '
                recv[1].send(now_member_msg.encode())
                if(recv[0]=='!enter'):
                     msg=str('[SYSTEM] '+now_time()+member_name_list[recv[2]])+'님이 입장하였습니다.'
                else:
                    recv[1].send(now_member_msg.encode())
                    continue
                
            elif recv[0].find('/w')==0: # 귓속말 기능
                split_msg=recv[0].split()
                if split_msg[1] in member_name_list:
                    msg=now_time()+'(귓속말) '+member_name_list[recv[2]] +' : '
                    msg+=recv[0][len(split_msg[1])+4:len(recv[0])]
                    idx=member_name_list.index(split_msg[1])
                    whisper_list[idx]=recv[2] # 귓속말을 받은 상대에게 보낸 사람 count값 저장
                    socket_descriptor_list[idx].send(msg.encode())
                else:
                    msg='해당 사용자가 존재하지 않습니다.'
                    recv[1].send(msg.encode())
                continue 
                
            elif recv[0].find('/r')==0: # 귓속말 답장 기능
                whisper_receiver=whisper_list[recv[2]]
                if whisper_receiver!=-1:
                    msg=now_time()+'(귓속말) '+member_name_list[recv[2]] +' : '
                    msg+=recv[0][3:len(recv[0])]
                    socket_descriptor_list[whisper_receiver].send(msg.encode())
                    whisper_list[whisper_receiver]=recv[2]
                else:
                    msg='귓속말 대상이 존재하지 않습니다.'
                    recv[1].send(bytes(msg.encode()))
                continue
                
            else:
                msg = str(now_time() + member_name_list[recv[2]]) + ' : ' + str(recv[0])

            for conn in socket_descriptor_list:
                if conn =='-1': # 연결 종료한 클라이언트 경우.
                    continue
                elif recv[1] != conn: #자신에게는 보내지 않음.
                    conn.send(msg.encode())
                else:
                    pass
            if recv[0] =='!quit':
                recv[1].close()
        except:
            pass

def recv_func(conn, count, lock):

    if socket_descriptor_list[count]=='-1':
        return -1
    while True:
        global left_member_name
        data = conn.recv(1024).decode()
        received_msg_info.put([data, conn, count]) 

        if data == '!quit' or len(data)==0:
            # len(data)==0 은 해당 클라이언트의 소켓 연결이 끊어진 경우에 대한 예외 처리임.
            lock.acquire()
            print(str(now_time()+ member_name_list[count]) + '님이 연결을 종료하였습니다.')
            left_member_name=member_name_list[count] # 종료한 클라이언트 닉네임 저장.
            socket_descriptor_list[count]= '-1'
            for i in range(len(whisper_list)):
                if whisper_list[i]==count:
                    whisper_list[i]=-1
            member_name_list[count]='-1'
            lock.release()
            break
    conn.close()
    
print(now_time()+'서버를 시작합니다')
server_sock=socket(AF_INET, SOCK_STREAM)
server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # Time-wait 에러 방지.
server_sock.bind((HOST, PORT))
server_sock.listen()

count = 0
socket_descriptor_list=['-1',] # 클라이언트들의 소켓 디스크립터 저장.
member_name_list=['-1',] # 클라이언트들의 닉네임 저장, 인덱스 접근 편의를 위해 0번째 요소 '-1'로 초기화.
whisper_list=[-1,]

received_msg_info = Queue()
left_member_name=''
lock=Lock()

while True:
    count = count +1
    conn, addr = server_sock.accept()
    # conn과 addr에는 연결된 클라이언트의 정보가 저장된다.
    # conn : 연결된 소켓
    # addr[0] : 연결된 클라이언트의 ip 주소
    # addr[1] : 연결된 클라이언트의 port 번호

    while True:
        client_name=conn.recv(1024).decode()

        if not client_name in member_name_list:
            conn.send('yes'.encode())
            break
        else:
            conn.send('overlapped'.encode())

    member_name_list.append(client_name)
    socket_descriptor_list.append(conn)
    whisper_list.append(-1)
    print(str(now_time())+client_name+'님이 연결되었습니다. 연결 ip : '+ str(addr[0]))

    if count>1:
        sender = Thread(target=send_func, args=(lock,))
        sender.start()
        pass
    else:
        sender=Thread(target=send_func, args=(lock,))
        sender.start()
    receiver=Thread(target=recv_func, args=(conn, count, lock))
    receiver.start()

server_sock.close()
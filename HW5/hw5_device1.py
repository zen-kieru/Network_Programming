# <2개의 IoT 디바이스로부터 데이터 수집>
# 1. 각각의 디바이스 서버가 기다리고 있다가 사용자(클라이언트)가 연결을 맺은 후에 'Request'를 보냄
# 2. 서버는 온습도조도 3가지 데이터를 보냄

### 서버 ###
from socket import *
import random
import time

BUF_SIZE = 8000
LENGTH = 4

s = socket(AF_INET, SOCK_STREAM)  # 디바이스 1의 서버 소켓
s.bind(('', 5555))
s.listen(10)
print('Device 1 server is running...')

while True:
    conn, addr = s.accept()
    print('User is connected')

    msg = conn.recv(BUF_SIZE)  # 'Request' 메세지 수신
    print('user: ', addr, msg.decode())

    if msg.decode() == 'Request':
        temp = str(random.randint(0, 40))
        humi = str(random.randint(0, 100))
        illum = str(random.randint(70, 150))

        # print(type(temp), temp)
        # print(type(humi), humi)
        # print(type(illum), illum)

        conn.send(temp.encode())
        conn.send(humi.encode())
        time.sleep(0.2)
        conn.send(illum.encode())

        conn.close()

    elif msg.decode() == 'quit':
        break

conn.close()

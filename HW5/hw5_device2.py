### 서버 ###
from socket import *
import random
import time

BUF_SIZE = 8000
LENGTH = 4

s = socket(AF_INET, SOCK_STREAM)  # 디바이스 1의 서버 소켓
s.bind(('', 7777))
s.listen(10)
print('Device 2 server is running...')

while True:
    conn, addr = s.accept()
    print('User is connected')

    msg = conn.recv(BUF_SIZE)  # 'Request' 메세지 수신
    print('user: ', addr, msg.decode())

    if msg.decode() == 'Request':
        heartbeat = str(random.randint(40, 140))
        steps = str(random.randint(2000, 6000))
        cal = str(random.randint(1000, 4000))

        # print(type(heartbeat), heartbeat)
        # print(type(steps), steps)
        # print(type(cal), cal)

        conn.send(heartbeat.encode())
        conn.send(steps.encode())
        time.sleep(0.2)
        conn.send(cal.encode())

        conn.close()

    elif msg.decode() == 'quit':
        break

conn.close()

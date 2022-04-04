### 클라이언트 ###
from socket import *
import sys
import time

BUF_SIZE = 8000

while True:
    # 문자열 '1', '2'를 입력받음
    DeviceNumber = input('Enter the Device number (1 or 2 or quit): ')

    if DeviceNumber == '1':  # *그냥 1이 아니라 문자열'1' 로 써야함.
        s1 = socket(AF_INET, SOCK_STREAM)
        s1.connect(('localhost', 5555))
        s1.send(b'Request')

        temp = s1.recv(BUF_SIZE)
        humi = s1.recv(BUF_SIZE)
        illum = s1.recv(BUF_SIZE)

        # print(type(temp), temp.decode())
        # print(type(humi), humi.decode())
        # print(type(illum), illum.decode())
        # print('device1: ', temp.decode(), humi.decode(), illum.decode())

        t = time.ctime(time.time())  # 문자열로 시간 반환
        d1_data = t + ':Device1: Temp=' + temp.decode() + \
            ', Humid=' + humi.decode() + ', Illum=' + illum.decode() + '\n'

        f = open('data.txt', 'a')
        f.write(d1_data)
        f.close()

    elif DeviceNumber == '2':
        s2 = socket(AF_INET, SOCK_STREAM)
        s2.connect(('localhost', 7777))
        s2.send(b'Request')

        heartbeat = s2.recv(BUF_SIZE)
        steps = s2.recv(BUF_SIZE)
        cal = s2.recv(BUF_SIZE)

        # print(type(heartbeat), heartbeat.decode())
        # print(type(steps), steps.decode())
        # print(type(cal), cal.decode())
        # print('device1: ', heartbeat.decode(), steps.decode(), cal.decode())

        t = time.ctime(time.time())  # 문자열로 시간 반환
        d2_data = t + ':Device2: heartbeat=' + heartbeat.decode() + \
            ', stepsd=' + steps.decode() + ', cal=' + cal.decode() + '\n'

        f = open('data.txt', 'a')
        f.write(d2_data)
        f.close()

    elif DeviceNumber == 'quit':
        s1 = socket(AF_INET, SOCK_STREAM)
        s1.connect(('localhost', 5555))
        s1.send(b'quit')

        s2 = socket(AF_INET, SOCK_STREAM)
        s2.connect(('localhost', 7777))
        s2.send(b'quit')

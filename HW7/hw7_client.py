from socket import *
import random
import time

port = 3333
BUFSIZE = 1024

s = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0  # 재전송 카운트
    addr = ('localhost', port)

    while reTx <= 3:
        re = str(reTx) + ' ' + msg
        s.sendto(re.encode(), addr)  # 메세지 전송
        s.settimeout(2)  # 2초동안 ack을 기다림.

        try:
            data, addr = s.recvfrom(BUFSIZE)  # ack을 기다림.
        except timeout:  # 2초가 지나 timeout이 되면
            reTx += 1  # 재전송 카운트 증가
            continue  # 위로 다시 가서 while문 수행
        else:
            break

    s.settimeout(None)

    while True:
        data, addr = s.recvfrom(BUFSIZE)  # 클라이언트의 메세지를 기다림.

        if random.randint(1, 10) <= 5:  # 50%의 확률로 ack을 보냄
            continue
        else:
            s.sendto(b'ack', addr)
            print('<-', data.decode())
            break

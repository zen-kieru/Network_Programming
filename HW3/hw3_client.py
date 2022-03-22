""" from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('계산식을 입력하시오 예) 20+17:')
    if msg == 'q':
        break
    s.send(msg.encode())

    result = s.recv(1024)  #
    print('계산 결과:', int.from_bytes(result, 'big'))
    # print('계산 결과:', s.recv(1024).decode())/

s.close() """


from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('계산식을 입력하시오 예) 20+17:')  # ***두자리수만 가능
    if msg == 'q':
        break
    s.send(msg.encode())

    print('계산 결과:', s.recv(1024).decode())

s.close()

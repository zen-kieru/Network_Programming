import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)
while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    name = client.recv(1024)  # 클라이언트로부터 이름을 수신
    print(name.decode())  # 클라이언트로부터 수신한 문자열 형태의 이름을 출력

    s_number = 20194164
    client.send(s_number.to_bytes(8, 'big'))  # 클라이언트로 학번을 정수형 변수로 빅엔디언 변환하여 전송

    client.close()

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

sock.send(b'Chaeyeon Kim')  # 서버로 이름을 보냄

r_number = sock.recv(1024)  # 서버로부터 학번을 수신
print(int.from_bytes(r_number, 'big'))  # 학번을 빅엔디언 변환하여 출력

sock.close()

from socket import *

port = 3333
BUFSIZE = 1024

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('localhost', port))

while True:
    msg = input(
        'Enter the message("send mboxId message" or "receive mboxId" or "quit"): ')

    if msg == 'quit':
        s.sendto(msg.encode(), ('localhost', port))
        break

    s.sendto(msg.encode(), ('localhost', port))
    data, addr = s.recvfrom(BUFSIZE)
    print(data.decode())


s.close()

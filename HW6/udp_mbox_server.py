from socket import *

port = 3333
BUFSIZE = 1024

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', port))
mbox = {'1': [], '2': [], '3': [], '4': [], '5': []}

while True:
    data, addr = s.recvfrom(BUFSIZE)  # 'send 3 how are you'
    data1 = data.decode()

    # data에서 앞에서부터 공백 2개만 자름 -> str.split(seq=none, maxsplit=-1)
    data2 = data1.split(' ', maxsplit=2)
    print(data2)  # ['send', '3', 'how are you']

    if data2[0] == 'send':
        mbox[data2[1]].append(data2[2])
        print(mbox)
        s.sendto('OK'.encode(), addr)

    elif data2[0] == 'receive':
        print(mbox[data2[1]])
        mbox[data2[1]].reverse()
        print(mbox[data2[1]])

        try:
            popped = mbox[data2[1]].pop()
            print(popped)
        except:
            s.sendto(b'No messages', addr)
        else:
            s.sendto(popped.encode(), addr)

    elif data2[0] == 'quit':
        break

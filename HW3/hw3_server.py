""" from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('wating...')

while True:
    client, addr = s.accept()
    print('connection from', addr)
    while True:
        data = client.recv(1024)
        dd = data.decode()  # a = '20+17'
        a = dd[0:2]
        k = dd[2]
        b = dd[3:5]
        if k == '+':
            result = int(a) + int(b)
            client.send(result.to_bytes(5, 'big'))
        if k == '-':
            result = int(a) - int(b)
            # print(type(result), result)
            client.send(result.to_bytes(5, 'big'))
        if k == '*':
            result = int(a) * int(b)
            client.send(result.to_bytes(5, 'big'))
        if k == '/':
            result1 = int(a) / int(b)  # result1 은 float형
            result = round(result1, 1)
            client.send(result.to_bytes(5, 'big'))
    client.close() """


from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('wating...')

while True:
    client, addr = s.accept()
    print('connection from', addr)
    while True:
        data = client.recv(1024)
        dd = data.decode()  # a = '20+17'
        a = dd[0:2]
        k = dd[2]
        b = dd[3:5]
        if k == '+':
            result = int(a) + int(b)
            client.send(str(result).encode())
        if k == '-':
            result = int(a) - int(b)
            # print(type(result), result)
            client.send(str(result).encode())
        if k == '*':
            result = int(a) * int(b)
            client.send(str(result).encode())
        if k == '/':
            result1 = int(a) / int(b)  # result1 은 float형
            result = round(result1, 1)
            client.send(str(result).encode())
    client.close()

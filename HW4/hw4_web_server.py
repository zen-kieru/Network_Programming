# 간단한 웹 서버 프로그램
# 필요 파일 : index.html, iot.png, favicon.ico
# 실행하는법 :
# 1. 터미널-cd hw4 엔터-python hw4_web_server.py
# 2. 엣지(크롬은 아이콘 적용이 안됨) 브라우저에서 http://127.0.0.1/index.html 접속

from mimetypes import MimeTypes
from socket import *
from os import path  # 파일 존재여부 확인을 위한 모듈 임포트

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    # msg = 'GET /index.html HTTP/1.1'

    req = str(msg.split('\r\n'))  # GET /index.html HTTP/1.1 라인이 리스트로 req에 저장
    # print(f'req : {req}') # ['GET /index.html HTTP/1.1']
    req2 = req.split()
    # print(f'req2 : {req2}') # ["['GET", '/index.html', "HTTP/1.1']"]
    req3 = req2[1]
    # req3 = str(req2[1])
    # print(f'req3 : {req3}') # /index.html
    filename = req3.lstrip('/')
    # print(f'filename : {filename}') # index.html

    if path.isfile(filename):  # filename의 파일이 존재하는지 검사 -> 파일존재하면 True반환 아니면 False
        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html'
        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'

        # 헤더 전송
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n\r\n')

        # 바디 전송
        data = f.read()
        if mimeType == 'text/html':  # index.html 파일(한글 텍스트 파일)의 경우
            c.send(data.encode('euc-kr'))  # 그 외 파일(바이너리 파일)의 경우
        else:
            c.send(data)

    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')

    c.close()

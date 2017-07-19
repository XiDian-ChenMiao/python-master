# coding:utf-8
import socket

HOST = '127.0.0.1'
PORT = 5003

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 建立UDP协议的套接字
s.bind((HOST, PORT))

data = True
while data:
    data, addr = s.recvfrom(2014)
    if data == b'bye':
        break
    print('Receive Data:', data.decode('utf-8'))
    s.sendto(data, addr)

s.close()

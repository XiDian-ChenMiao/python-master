# coding:utf-8
from socket import *
HOST = '127.0.0.1'
PORT = 5004
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

socket = socket(AF_INET, SOCK_STREAM)
socket.connect(ADDR)
data = 'Hello Server.'
while data:
    socket.send(data.encode('utf-8'))
    if data == 'bye':
        break
    data = socket.recv(BUFFERSIZE)
    print('Received From Server:', data.decode('utf-8'))
    data = input('> ')
socket.close()

# coding:utf-8
import socket

HOST = '127.0.0.1'
PORT = 5003

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    data = 'Hello Server'
    while data:
        s.sendto(data.encode('utf-8'), (HOST, PORT))  # 向指定服务器地址发送数据
        if data == 'bye':  # 如果接收到数据为指定数据，则关闭与服务器的通信
            break
        data, addr = s.recvfrom(1024)  # 从服务器接收数据
        print('Receive From Server:', data.decode('utf-8'))
        data = input('Please Enter Message:')
except socket.error as err:
    print(err)
finally:
    s.close()

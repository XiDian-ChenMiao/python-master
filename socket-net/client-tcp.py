# coding:utf-8
import socket

HOST = '127.0.0.1'
PORT = 5002  # 与服务器端口相同

s = socket.socket()  # 创建socket连接

try:
    s.connect((HOST, PORT))  # 连接服务器
    data = 'Hello Server'
    while data:
        s.sendall(data.encode('utf-8'))  # 向服务器发送数据
        data = s.recv(1024)  # 从服务器端接收数据
        print('Receive Data From Server:', data.decode('utf-8'))
        data = input('Please Enter Message:')  # 等待用户输入
except socket.error as err:  # 处理可能的异常
    print(err)  # 打印异常信息
finally:
    s.close()




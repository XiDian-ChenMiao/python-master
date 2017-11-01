# coding:utf-8
import socket
HOST = '127.0.0.1'
PORT = 5002

s = socket.socket()  # 创建socket
s.bind((HOST, PORT))  # 绑定地址以及端口
s.listen(5)  # 开启监听指定端口

conn, addr = s.accept()  # 开始接收来自客户端的socket连接
print('Client Address:', addr)
while True:
    data = conn.recv(1024)  # 接收客户端发送的数据
    if not data:
        break  # 如果没有再收到任何消息，则断开连接
    print('Receive Data From Client:', data.decode('utf-8'))  # 打印接收到的数据
    conn.send(data)  # 向客户端发送接收的数据

conn.close()  # 关闭连接对象
s.close()  # 关闭服务器端socket

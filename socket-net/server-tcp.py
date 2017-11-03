# coding:utf-8
import socket
from tcp_authen import client_authen, server_authen
HOST = '127.0.0.1'
PORT = 5002
SECRET_KEY = b'daqinzhidi'

def echo_handler(client_sock):
    if not server_authen(client_sock, SECRET_KEY):
        client_sock.close()
        return
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)


def echo_server(address):
    s = socket.socket()  # 创建socket
    s.bind((HOST, PORT))  # 绑定地址以及端口
    s.listen(5)  # 开启监听指定端口
    while True:
        c, a = s.accept()
        echo_handler(c)


if __name__ == '__main__':
    echo_server((HOST, PORT))


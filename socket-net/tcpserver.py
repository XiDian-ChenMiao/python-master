#!/usr/bin/env python
# coding=utf-8
# 创建一个TCP服务器

from socketserver import BaseRequestHandler, TCPServer, ThreadingTCPServer
import socket

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('get connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


if __name__ == '__main__':
    server = TCPServer(('', 20000), EchoHandler, bind_and_activate=False) # 单线程服务器，限制TCPServer在实例化时就会绑定并激活底层的socket
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server.server_bind()
    server.server_activate()

    # mserver = ThreadingTCPServer(('', 20001), EchoHandler) # 多线程服务器
    from threading import Thread
    NWORKERS = 16
    for n in range(NWORKERS):
        t = Thread(target=server.serve_forever)
        t.daemon = True
        t.start()
    server.serve_forever()
    # mserver.serve_forever()

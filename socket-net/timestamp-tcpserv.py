# coding:utf-8
from socketserver import TCPServer, StreamRequestHandler
from time import ctime
import threading

HOST = '127.0.0.1'
PORT = 5004
ADDR = (HOST, PORT)


def shutdown_server():
    if server:
        server.shutdown()  # 必须与实例的serve_forever方法处于不同的线程中
    print('Server shutdown')


class CustomRequestHandler(StreamRequestHandler):
    """
    自定义请求处理器
    """

    def handle(self):
        while True:
            print('Connected From:', self.client_address)
            data = self.request.recv(1024)
            print('Received From Client:', data.decode('utf-8'))
            if data == b'bye':
                break
            message = '[' + ctime() + '] ' + data.decode('utf-8')
            self.request.sendall(message.encode('utf-8'))
        threading.Thread(target=shutdown_server).start()


if __name__ == '__main__':
    server = TCPServer(ADDR, CustomRequestHandler)
    print('Waiting For Connection......')
    server.serve_forever()

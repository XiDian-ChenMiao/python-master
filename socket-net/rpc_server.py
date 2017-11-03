#!/usr/bin/env python
# coding=utf-8
# 实现远程过程调用

import pickle

class RPCHandler(object):
    def __init__(self):
        self._functions = {}

    def register(self, func):
        self._functions[func.__name__] = func

    def handle(self, connection):
        try:
            while True:
                func_name, args, kwargs = pickle.loads(connection.recv())
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


from multiprocessing.connection import Listener
from threading import Thread

def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle, args=(client, ))
        t.daemon = True
        t.start()

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

if __name__ == '__main__':
    rpc = RPCHandler()
    rpc.register(add)
    rpc.register(sub)
    rpc_server(rpc, ('localhost', 17000), authkey=b'daqinzhidi')

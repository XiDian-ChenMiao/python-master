#!/usr/bin/env python
# coding=utf-8
# RPC客户端

import pickle

class RPCProxy(object):
    def __init__(self, connection):
        self.connection = connection

    def __getattr__(self, name):
        def rpc(*args, **kwargs):
            self.connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self.connection.recv())
            if isinstance(result, Exception):
                raise result
            return result
        return rpc

if __name__ == '__main__':
    from multiprocessing.connection import Client
    proxy = RPCProxy(Client(('localhost', 17000), authkey=b'daqinzhidi'))
    print(proxy.add(2, 3))
    print(proxy.sub(2, 3))

#!/usr/bin/env python
# coding=utf-8
# TCP服务器的验证模块

import hmac
import os

def client_authen(connection, secret_key):
    message = connection.recv(32)
    hashm = hmac.new(secret_key, message)
    digest = hashm.digest()
    connection.send(digest)


def server_authen(connection, secret_key):
    message = os.urandom(32)
    connection.send(message)
    hashm = hmac.new(secret_key, message)
    digest = hashm.digest()
    resp = connection.recv(len(digest))
    return hmac.compare_digest(digest, resp)

# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试Python的加密和解密模块
import base64


def base64_encode(string):
    return str(base64.b64encode(string.encode(encoding='utf-8')))


def base64_decode(string):
    return str(base64.b64decode(string))


def base64_safe_encode(string):
    return str(base64.urlsafe_b64encode(string.encode(encoding='utf-8')))


def base64_safe_decode(string):
    return str(base64.urlsafe_b64decode(string))


if __name__ == '__main__':
    print(base64_encode('DAQINZHIDI'))
    print(base64_decode('REFRSU5aSElESQ=='))

    print(base64_safe_encode('DAQINZHIDI/+'))
    print(base64_safe_decode('REFRSU5aSElESS8r'))

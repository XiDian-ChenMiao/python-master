# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: python的摘要算法
import hashlib


def md5_string(string):
    obj = hashlib.md5()
    obj.update(string.encode('utf-8'))
    print(obj.hexdigest())  # 固定的32位16进制字符


def sha1_string(string):
    obj = hashlib.sha1()
    obj.update(string.encode('utf-8'))
    print(obj.hexdigest())  # 固定的40位16进制字符

if __name__ == '__main__':
    md5_string('大秦之帝')
    sha1_string('大秦之帝')

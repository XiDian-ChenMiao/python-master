# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 简单的机器信息获取
import uuid
import socket


def get_mac_address():
    """
    获取本机MAC地址
    :return:
    """
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ':'.join([mac[e:e + 2] for e in range(0, 11, 2)])


def get_host_name():
    """
    获取本机电脑名
    :return:
    """
    return socket.getfqdn(socket.gethostname())


def get_host_ip():
    """
    获取本机IP地址
    :return:
    """
    return socket.gethostbyname(get_host_name())


if __name__ == '__main__':
    print('MAC ADDRESS:', get_mac_address())
    print('HOST NAME:', get_host_name())
    print('HOST IP:', get_host_ip())

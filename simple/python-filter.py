# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: Python的filter函数


def filter_odd(l):
    def is_odd(n):
        return n % 2 == 1
    return list(filter(is_odd, l))


if __name__ == '__main__':
    print(filter_odd([x for x in range(30)]))



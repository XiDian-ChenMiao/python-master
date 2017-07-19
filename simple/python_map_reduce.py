# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: Python的Map和Reduce测试
from functools import reduce


def python_map():
    def sqrt(x):
        return x * x

    r = map(sqrt, [x for x in range(5)])
    print('结果类型为：', type(r), '结果为：', list(r))


def fn(x, y):
    return x * 10 + y


def char2value(c):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]


def char2num(s):
    return reduce(fn, map(char2value, s))


def str2num(s):
    return reduce(lambda x, y: x * 10 + y, map(char2value, s))


if __name__ == '__main__':
    python_map()
    print(char2num('1234'))
    print(str2num('12345'))

# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python的__getattr__


class UrlChain:
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return UrlChain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

    def __call__(self, *args, **kwargs):
        if args:
            print(args)
        if kwargs:
            print(kwargs)
        print('调用了对象的__call__方法')

    __repr__ = __str__


if __name__ == '__main__':
    print(UrlChain().name.status.list)  # 链式打印地址
    UrlChain()()  # 对象充当函数调用

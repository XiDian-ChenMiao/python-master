#!/usr/bin/env python
# coding=utf-8
# 利用元类来控制实例的创建
import weakref


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print('constructor Spam')


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            o = super().__call__(*args)
            self.__cache[args] = o
            return o


class B(metaclass=Cached):
    def __init__(self, name):
        print('creating B({!r})'.format(name))
        self.name = name


if __name__ == '__main__':
    a = Spam()
    b = Spam()
    print(a is b)

    c = B('XiDian-ChenMiao')
    d = B('XiDian-ChenMiao')
    e = B('ChenMiao')
    print(c is d)
    print(d is e)

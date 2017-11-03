#!/usr/bin/env python
# coding=utf-8
# 定义一个接口或者抽象基类

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        print('IStream read.')
        pass

    @abstractmethod
    def write(self, data):
        print('IStream write.')
        pass


class SimpleStream(IStream):
    def read(self, maxbytes=-1):
        print('SimpleStream read.')
        super().read()

    def write(self, data):
        print('SimpleStream write.')
        super().write(data)


if __name__ == '__main__':
    ss = SimpleStream()
    ss.read()
    ss.write('data')

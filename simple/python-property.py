# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: python的属性装饰器
class Person(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('名字长度超过限制')
        self._name = value

    def __str__(self):
        return 'Person object(name: %s)' % self._name

    __repr__ = __str__  # __repr__是提供调试使用的宏定义

if __name__ == '__main__':
    p = Person()
    p.name = 'DAQINZHIDI'
    print(p.name)
    print(p)

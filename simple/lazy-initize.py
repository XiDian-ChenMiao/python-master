# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: python延迟初始化
import math


class LazyProperty(object):
    """
    属性延迟初始化
    """
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print('计算面积')
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        print('计算周长')
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(5)
    print(c.area)
    print(c.area)
    print(c.perimeter)
    print(c.perimeter)


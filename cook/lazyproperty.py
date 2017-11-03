#!/usr/bin/env python
# coding=utf-8
# 让属性具有懒惰求值的能力
import math

class lazyproperty(object):
    def __init__(self, func):
        self._func = func

    def __get__(self, instance, cls):
        print(cls, instance)
        if instance is None:
            return self
        else:
            value = self._func(instance)
            setattr(instance, self._func.__name__, value)
            return value


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('计算面积：')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('计算周长：')
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(4.0)
    print(c.area)
    print(c.perimeter)
    print(c.area)
    print(c.perimeter)

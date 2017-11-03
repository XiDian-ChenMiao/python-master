#!/usr/bin/env python
# coding=utf-8
# 在类中定义装饰器

from functools import wraps

def log_getattribute(cls):
    original_attrite = cls.__getattribute__

    def new_getattribute(self, name):
        print('get:', name)
        return original_attrite(self, name)
    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class A(object):
    def decorator_self(self, func):
        @wraps(func)
        def decorate(*args, **kwargs):
            print('decorator_self')
            return func(*args, **kwargs)
        return decorate

    @classmethod
    def decorate_cls(cls, func):
        @wraps(func)
        def decorate(*args, **kwargs):
            print('decorate_cls')
            return func(*args, **kwargs)
        return decorate

a = A()

@a.decorator_self
def a():
    pass

@A.decorate_cls
def b():
    pass
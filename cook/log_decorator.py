#!/usr/bin/env python
# coding=utf-8
# 定义一个可接受参数的装饰器

from functools import wraps
import logging

def logged(level, name=None, message=None):
    """
    """
    def decorate(func):
        logname = name if name else func.__name__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(*args):
    return sum(*args)

@logged(logging.CRITICAL, 'example')
def spam():
    print('Frando')


if __name__ == '__main__':
    print(add([1, 2, 3, 4, 5]))
    spam()

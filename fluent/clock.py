#!/usr/bin/env python
# coding=utf-8
import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        args_str = ', '.join(arg_list)
        print('[%0.8f] %s(%s) -> %r' % (elapsed, name, args_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'calling factorial(6)')
    print('6! = ', factorial(6))

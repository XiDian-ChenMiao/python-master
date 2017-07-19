# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: python的装饰器
import datetime
import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('装饰器参数为：%s，调用的是方法：%s' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('管理员')
def show_time():
    print('当前时间为：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    show_time()

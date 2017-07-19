# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 上下文管理器测试
import contextlib
import time


class OpenFileContextManager(object):

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('__enter__')
        self.f = open(self.filename, 'a+')
        return self.f  # 作为as关键字之后变量的句柄

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        self.f.close()
        if exc_type != SyntaxError:
            return True  # 如果返回True，则此时该异常就不会被抛出
        return False  # 如果是语法异常，则抛出


@contextlib.contextmanager
def timeout():
    start_time = time.time()
    yield start_time  # yield之后的返回值可以作为with语句中as后变量所持有的句柄
    end_time = time.time()
    use_time = (end_time - start_time) * 1000
    print('use_time: %d ms' % use_time)

if __name__ == '__main__':
    with OpenFileContextManager('config.ini') as f:
        f.read()

    with timeout() as start:  # 如果在此语句块中抛出异常的话，yield后面的代码将不会被执行，所以必要时对yield语句使用try-finally
        print('start_time:', start)
        time.sleep(1)

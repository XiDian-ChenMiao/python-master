# coding:utf-8

import threading
from time import ctime, sleep

loops = [6, 2, 5]


def loop(nloop, nesc):
    print('开启循环', nloop, '，时间为：', ctime())
    sleep(nesc)
    print('关闭循环', nloop, '，时间为：', ctime())


def main():
    print('开始执行main函数，时间为：', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    # join方法是调用线程将等待被调用线程结束，或者在提供了超时时间的情况下，达到超时时间。
    # 使用join方法比等待锁释放的无限循环更加清晰，常被称为自旋锁。
    # join方法只有在你需要等待线程完成的视乎才是有用的。
    print('main函数执行完成，时间为：', ctime())


def main_threadfunc():
    print('开始执行main函数，时间为：', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i])), args=(i, loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print('main函数执行完成，时间为：', ctime())


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self, *args, **kwargs):
        self.func(*self.args)


if __name__ == '__main__':
    # main()
    print('当前线程：', threading.current_thread().name)
    main_threadfunc()

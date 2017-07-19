# coding:utf-8
from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock
from time import ctime, sleep


class CleanOutputSet(set):
    def __str__(self):  # 重载输出方法
        return ', '.join(x for x in self)


lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()


def loop(nsec):
    tname = currentThread().name
    lock.acquire()
    remaining.add(tname)
    print('线程[%s]启动，时间为：%s' % (tname, ctime()))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(tname)
    print('线程[%s]在%s时间完成线程任务，用时：%s，存在任务为：%s' % (tname, ctime(), nsec, remaining or 'NONE'))
    lock.release()


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print('所有任务都已经完成', ctime())


if __name__ == '__main__':
    _main()

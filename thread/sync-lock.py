# coding:utf-8
import threading
import time
import random

SHARE = 4

lock = threading.Lock()


class CustomThread(threading.Thread):
    def __init__(self, i):
        super(CustomThread, self).__init__()
        self.i = i

    def run(self):
        global SHARE
        for d in range(3):
            lock.acquire()  # 获取共享资源的锁
            print('Share:', SHARE)
            SHARE += self.i
            time.sleep(random.random())
            print('+', self.i, '=', SHARE)
            lock.release()


if __name__ == '__main__':
    one = CustomThread(2)
    two = CustomThread(6)
    one.start()
    two.start()

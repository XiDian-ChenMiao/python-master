# coding:utf-8
import threading
import time

sema = threading.Semaphore(2)  # 定义有两个资源的信号量


class CustomThread(threading.Thread):
    def __init__(self, name):
        super(CustomThread, self).__init__()
        self.name = name

    def run(self):
        if sema.acquire():
            print(self.name, 'Got Resource.')
            time.sleep(1)
        sema.release()
        print(self.name, 'Released Resource.')


if __name__ == '__main__':
    ths = [CustomThread(str(i) + '-Sema') for i in range(5)]
    for th in ths:
        th.start()

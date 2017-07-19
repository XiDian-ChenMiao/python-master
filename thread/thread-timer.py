# coding:utf-8
import threading
import time


def echo():
    time.sleep(1)
    print('Hello DAQINZHIDI')


if __name__ == '__main__':
    t = threading.Timer(3, echo)
    t.start()

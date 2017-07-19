# coding:utf-8

import threading
import time

event = threading.Event()


class WaitThread(threading.Thread):
    def run(self):
        self.name = 'Wait Thread'
        print(self.name, 'Wait......')
        event.wait()
        print(self.name, 'Start......')
        event.clear()


class MainThread(threading.Thread):
    def run(self):
        time.sleep(3)
        print('Main Thread set event flag.')
        event.set()


if __name__ == '__main__':
    wait = WaitThread()
    mth = MainThread()

    wait.start()
    mth.start()

# coding:utf-8
import threading
import time


def thfunc():
    s = 0
    for i in range(30):
        s += i
        print('Thread:', i)
        time.sleep(0.1)
    print('Sum=', s)


class CustomThread(threading.Thread):
    def run(self):
        s = 0
        for i in range(30):
            s += i
            print('Current Sum:', s)
            time.sleep(0.1)
        print('Sum=', s)

if __name__ == '__main__':
    # ths = [threading.Thread(target=thfunc) for i in range(1)]
    # for th in ths:
    #     th.start()

    th = CustomThread()
    th.start()
    th.join(1)  # 等待线程执行完毕，主线程才能继续运行，参数为主线程等待子线程的时间

    for num in range(30):
        print('Main:', num)

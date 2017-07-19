# coding:utf-8
import threading
import time


def dmn():
    print('开启守护线程......')
    time.sleep(2)
    print('结束守护线程......')


def ndmn():
    print('开启非守护线程......')
    time.sleep(1)
    print('结束非守护线程......')


if __name__ == '__main__':
    d = threading.Thread(target=dmn)
    d.daemon = True
    n = threading.Thread(target=ndmn)
    print('主线程开启......')
    d.start()
    n.start()
    print('主线程关闭......')  # 主线程要等待非后台线程执行完成之后才能退出

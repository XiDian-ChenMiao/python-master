# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python的threadlocal
import threading
# 在多线程环境下，每个线程都有自己的数据。
# 一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦。

thread_pool = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = thread_pool.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student
    thread_pool.student = name
    process_student()


# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('大秦之帝',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('陈苗',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

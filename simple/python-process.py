# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python的进程
import os
import time
import random
import subprocess
from multiprocessing import Process, Queue


def run_proc(name):
    print('运行子进程%s，进程ID为：%s' % (name, os.getpid()))


def long_time_task(name):
    print('运行任务%s(%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('任务%s运行了%0.2f秒' % (name, (end - start)))


# 通过子进程模块调用linux平台下的nslookup命令
def call_nslookup():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('错误码:', r)


# 进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

# windows环境下没有fork调用
# pid = os.fork()
# if pid == 0:
#     print('我是子进程%s，我的父进程为%s' % (os.getpid(), os.getppid()))
# else:
#     print('我是父进程%s，子进程为%s' % (os.getpid(), pid))
def proc_communicate_read_queue(queue):
    print('读进程的进程ID为：', os.getpid())
    while True:
        value = queue.get(True)
        print('从队列中读取%s' % value)


def proc_communicate_write_queue(queue):
    print('写进程的进程ID为：', os.getpid())
    for c in ['D', 'A', 'Q', 'I', 'N', 'Z', 'H', 'I', 'D', 'I']:
        print('将%s写入到队列中' % c)
        queue.put(c)
        time.sleep(random.random())


if __name__ == '__main__':
    print('当前进程编号为：', os.getpid())
    print('父进程ID为：', os.getpid())
    p = Process(target=run_proc, args=('P-1',))
    print('子进程开启')
    p.start()
    p.join()  # join方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('子进程结束')

    # pool = Pool(4)  # Pool的默认大小是CPU的核数
    # for i in range(5):
    #     pool.apply_async(long_time_task, args=('P-' + i,))
    # print('等待所有的子进程完成')
    # pool.close()  # 在join方法之前执行close方法，表示进程池将不再添加进程
    # pool.join()
    # print('所有的子进程都已完成')

    q = Queue()
    p_write = Process(target=proc_communicate_write_queue, args=(q,))
    p_read = Process(target=proc_communicate_read_queue, args=(q,))
    p_write.start()  # 开启写进程
    p_read.start()  # 开启读进程
    p_write.join()  # 等待写进程执行完成
    p_read.terminate()  # 读进程为死循环，只能强制退出

# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python的分布式工作进程

import random
import queue
import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 通过网络将两个队列注册，callable参数关联了队列对象
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 绑定本地的10000端口，设置验证码为‘abc’
SERVER_ADDR = '127.0.0.1'
print('连接到服务器%s' % SERVER_ADDR)
manager = QueueManager(address=(SERVER_ADDR, 10000), authkey=b'abc')
# 从网络连接
manager.connect()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 将任务放入到网络上获取的队列中
for i in range(10):
    n = random.randint(0, 10000)
    print('任务队列中放入任务%d' % n)
    task.put(n)
# 从网络上获取的任务队列中获取任务
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('运行任务%d乘以%d' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Queue.Empty:
        print('任务队列已经为空')
print('工作进程退出')

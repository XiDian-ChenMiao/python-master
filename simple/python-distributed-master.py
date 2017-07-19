# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python的分布式主进程

import random
import queue
from multiprocessing.managers import BaseManager
# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。
# 比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


# 通过网络将两个队列注册，callable参数关联了队列对象
QueueManager.register('get_task_queue', callable=lambda:task_queue)
QueueManager.register('get_result_queue', callable=lambda:result_queue)
# 绑定本地的10000端口，设置验证码为‘abc’
manager = QueueManager(address=('', 10000), authkey=b'abc')
# 启动管理器
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 将任务放入到网络上获取的队列中
for i in range(10):
    n = random.randint(0, 10000)
    print('任务队列中放入任务%d' % n)
    task.put(n)
# 从网络上获取的结果队列中获取结果
for i in range(10):
    r = result.get(timeout=10)
    print('结果为：%s' % r)
# 关闭
manager.shutdown()
print('主调度器关闭')

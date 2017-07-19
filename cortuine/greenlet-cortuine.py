# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2017 Miao.Chen
# Summary: 使用greenlet协程库实现生产者消费者模式
from greenlet import greenlet


def consumer():
    last = ''
    while True:
        receival = pro.switch(last)
        if receival:
            print('[Consumer] %s' % receival)
            last = receival


def producer(n):
    con.switch()
    x = 0
    while x < n:
        x += 1
        print('[Producer] %s' % x)
        last = con.switch(x)


pro = greenlet(producer)
con = greenlet(consumer)
pro.switch(5)

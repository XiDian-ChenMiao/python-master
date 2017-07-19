# coding:utf-8
import time
import datetime


# 将指定时间转为时间戳
def transfer():
    t = "2016-09-02 11:09:20"
    timearray = time.strptime(t, '%Y-%m-%d %H:%M:%S')
    timestamp = int(time.mktime(timearray))
    print(timestamp)


# 变换给定时间的时间格式
def formattime():
    t = "2016-09-02 11:09:20"
    timearray = time.strptime(t, '%Y-%m-%d %H:%M:%S')
    othertime = time.strftime('%Y/%m/%d %H:%M:%S', timearray)
    print(othertime)


# 通过时间戳转换为时间
def stamptotime():
    t = "2016-09-03 11:09:20"
    timearray = time.strptime(t, '%Y-%m-%d %H:%M:%S')
    timestamp = int(time.mktime(timearray))
    timearray = time.localtime(timestamp)
    othertime = time.strftime('%Y/%m/%d %H:%M:%S', timearray)
    print(othertime)


# 当前时间转为格式字符串
def nowtotime():
    nowstamp = int(time.time())
    nowtimearray = time.localtime(nowstamp)
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', nowtimearray)
    print(nowtime)


def datetimenow():
    nowarray = datetime.datetime.now()
    print('当前时间为：', nowarray.strftime('%Y-%m-%d %H:%M:%S'))


# 当前时间以前的三天
def datetime_3days_ago():
    threedaysago = datetime.datetime.now() - datetime.timedelta(days=3)
    print('三天之前时间为：%s，对应的时间戳为：%s' % (threedaysago.strftime('%Y-%m-%d %H:%M:%S'), int(time.mktime(threedaysago.timetuple()))))


# 把当前时间戳转为时间
def timestamptodatetime():
    nowstamp = int(time.time())
    timearray = datetime.datetime.utcfromtimestamp(nowstamp)
    print('当前时间戳转为时间为：', timearray.strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    transfer()
    formattime()
    stamptotime()
    nowtotime()
    datetimenow()
    datetime_3days_ago()
    timestamptodatetime()

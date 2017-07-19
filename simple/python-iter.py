# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试Python的迭代


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):  # 使得其可以像列表一样使用
        if isinstance(item, int):  # 如果为索引查找
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # 如果为切片查找
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l

if __name__ == '__main__':
    for i in Fib():
        print(i)
    print('第五个元素为：', Fib()[4])
    print('第五到十之间的元素为：', Fib()[5:10:0])

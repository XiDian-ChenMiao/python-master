# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python的集合模块

from collections import namedtuple, deque, defaultdict, Counter


def python_deque():
    q = deque(['DAQINZHIDI', 'CHENMIAO'])
    print(q.pop())
    print(q.pop())
    q.appendleft('陈苗')
    q.append('大秦之帝')


# 当字典中不存在指定的键时，如果用内置的dict将会报KeyError异常，而使用defaultdict则可以设置默认
def python_defaultdict():
    dd = defaultdict(lambda: None)
    dd['name'] = '大秦之帝'
    print('名字为：', dd['name'], '年龄为：', dd['age'])


# 测试集合包下的计数器
def python_counter():
    c = Counter()
    for s in 'DAQINZHIDI':
        c[s] += 1
    print(c)
    print(c.most_common(2))  # 获取次数最多的前两个元素


if __name__ == '__main__':
    # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 3)
    print('横坐标为:', p.x, '纵坐标为:', p.y)
    print('是否为Point：', isinstance(p, Point), '是否为元组：', isinstance(p, tuple))
    python_deque()
    python_defaultdict()
    python_counter()

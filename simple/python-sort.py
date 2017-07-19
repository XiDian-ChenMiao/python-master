# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python的sorted函数


def python_sorted(l, func=None):
    print(python_sorted.__name__)  # 每一个函数都有一个__name__属性
    if func:
        return list(sorted(l, key=func))
    return list(sorted(l))


if __name__ == '__main__':
    print(python_sorted([5, 1, -20, 4, 2, -100]))
    print(python_sorted([5, 1, -20, 4, 2, -100], func=abs))
    print(python_sorted(['abc', 'ANC', 'cde', 'bdf'], func=str.lower))

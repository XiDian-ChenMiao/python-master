# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试Python的生成器


def list_generator():
    l = [x * x for x in range(6)]
    print(l)


def generator():  # 保存的是算法
    g = (x * x for x in range(6))
    print(g)
    for number in g:
        print(number)


def enumateor():
    for i, value in enumerate([x * x for x in range(6)]):
        print('下标为%d，值为：%d' % (i, value))


def fib(number):
    n, a, b = 0, 0, 1
    while n < number:
        yield b  # yield关键字可将函数变为一个generator
        a, b = b, a + b
        n = n + 1
    return 'DONE'


if __name__ == '__main__':
    list_generator()
    generator()
    enumateor()
    print(type(fib(5)))
    for i in fib(5):
        print(i)

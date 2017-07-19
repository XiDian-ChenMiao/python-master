# coding:utf-8


class Calc:

    def add(self, a, b):
        a += b
        return a

    def sub(self, a, b):
        a -= b
        return a

    def muti(self, a, b):
        a *= b
        return a

    def div(self, a, b):
        if b == 0:
            raise Exception('除数为0')
        return a / b


if __name__ == '__main__':
    calc = Calc()
    print('测试加法：', calc.add(5, 10) == 15)
    print('测试减法：', calc.sub(5, 10) == -5)
    print('测试乘法：', calc.muti(5, 10) == 50)
    print('测试除法：', calc.div(10, 5) == 2)

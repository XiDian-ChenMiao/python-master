# coding:utf-8


def pythonargs(*args, **kwargs):
    for a in args:
        print(a)
    for kw in kwargs:
        print('关键字为：%s，值为：%s' % (kw, kwargs[kw]))


if __name__ == '__main__':
    pythonargs(2, 3, name='daqinzhidi')

# coding:utf-8
class NoneNeg:
    """
    非负类
    """

    # 描述符：数据描述符__set__，__get__，__delete__只能在新式类中使用；所有的类成员函数都为非数据描述符
    def __init__(self, default=0):
        self._default = default

    def __set__(self, instance, value):
        print('Instance:', instance)
        if value > 0:
            self._default = value
        else:
            print('Number must be negative.')

    def __get__(self, instance, owner):
        print('Owner:', owner)
        print('Instance:', instance)
        return self._default

    def __delete__(self, instance):
        pass

    # 将对象可以当做方法来调用
    def __call__(self, *args, **kwargs):
        print('Args Length:', len(args))
        index = 0
        for argument in args:
            print('[' + str(index) + ']', argument)
            index += 1


class Movie:
    """
    电影类
    """
    score = NoneNeg()
    rating = NoneNeg()

    def __init__(self):
        pass


if __name__ == '__main__':
    m = Movie()
    print('Rating:', m.rating)
    print('Score:', m.score)
    m.rating = 80
    m.score = -10
    print('Rating:', m.rating)
    print('Score:', m.score)
    n = NoneNeg()
    n(-8)

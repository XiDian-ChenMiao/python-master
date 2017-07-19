# coding:utf8
class A:
    def __init__(self):
        pass
    name = 'A'


class B:
    def __init__(self):
        pass
    name = 'B'


class Factory:

    def __init__(self):
        pass

    def get_instance(self, cls):
        return cls()


if __name__ == '__main__':
    factory = Factory()
    print(type(factory.get_instance(A)))
    print(type(factory.get_instance(B)))

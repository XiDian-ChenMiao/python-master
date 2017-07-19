# coding:utf-8
class Singleton:
    """
    单例模式
    """
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_sgl'):
            cls._sgl = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._sgl


if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    print(id(a))
    print(id(b))

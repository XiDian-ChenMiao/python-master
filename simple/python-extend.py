# coding:utf-8
class BaseClass:
    """
    基类
    """
    def show_info(self, info):
        print('Info:', info)

    def __init__(self):
        print('Constructor:', BaseClass.__name__)

    # 先执行__new__创建实例，然后执行__init__执行初始化
    def __new__(cls, *args, **kwargs):
        print('Creator:', 'BaseClass')
        return object.__new__(cls, *args, **kwargs)


class AnotherBaseClass:
    """
    基类
    """
    def __init__(self):
        print('Constructor:', AnotherBaseClass.__name__)
    pass


class DerivedClass(BaseClass):
    """
    单继承的派生类
    """
    def __init__(self):
        super(DerivedClass, self).__init__()  # python不会隐式的调用父类的构造函数
        print('Constructor:', DerivedClass.__name__)

    def show_info(self, info):  # 对基类的方法进行覆盖达到重写效果
        print('Derived Info:', info)


class MultiDerivedClass(BaseClass, AnotherBaseClass):
    """
    多继承的派生类
    """
    def __init__(self):
        print('Constructor:', MultiDerivedClass.__name__)
    pass


class MetaClass(type):
    def __init__(cls, name, bases, dicts):
        print('Init Instance')

    def __new__(cls, name, bases, dicts):
        print('New Instance')
        res = type.__new__(name, bases, dicts)
        res.school = 'XiDian'
        return res


class Custom:
    __metaclass__ = MetaClass  # 配置其元类型为MetaClass

    def __init__(self):
        pass
    pass


if __name__ == '__main__':
    print(BaseClass.__base__)
    print(AnotherBaseClass.__base__)
    print(DerivedClass.__base__)
    print(MultiDerivedClass.__base__)  # 只显示第一个基类的名称
    print(MultiDerivedClass.__bases__)  # 显示全部基类的名称

    base = BaseClass()
    another = AnotherBaseClass()
    derived = DerivedClass()
    derived.show_info('show_info')  # 继承使用
    multi = MultiDerivedClass()
    print('Type:', type(BaseClass))  # 类的创建者和管理者为元类type，所有的类都是元类的实例

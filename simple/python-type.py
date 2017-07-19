# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python的type函数

# metaclass：元类
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”
# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码


def show(self, name='DAQINZHIDI'):
    print('名字为：', name)


if __name__ == '__main__':
    # type函数有三个参数：第一个为构造的类的名称，第二个为其继承的父类，第三个为其绑定的方法
    Hello = type('Hello', (object,), dict(hello=show))
    h = Hello()
    h.hello()

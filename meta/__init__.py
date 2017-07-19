# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: Create Meta Package


def upper_attr(future_class_name, future_parent_name, future_class_attr):
    """
    将每个类中的属性名称统统改为大写
    :param future_class_name: 类名称字符串
    :param future_parent_name: 父类元组
    :param future_class_attr: 类属性字典
    :return: 动态创建的类
    """
    # 选择所有不以‘__’开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将这些属性改为大写形式
    uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
    # 通过type来进行类对象的创建
    return type(future_class_name, future_parent_name, uppercase_attrs)


class UpperAttributesMetaClass(type):
    """
    自定义元类，复写__new__方法
    """
    def __new__(mcs, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items if not name.startswith('__'))
        uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(mcs, future_class_name, future_class_parents, uppercase_attrs)


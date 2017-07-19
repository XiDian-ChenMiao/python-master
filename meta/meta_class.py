# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 指定元类测试
from src.meta import UpperAttributesMetaClass


class Foo(metaclass=UpperAttributesMetaClass):
    name = 'Foo'


print(hasattr(Foo, 'name'))
print(Foo.name)
print(type(Foo))
print(dir(Foo))

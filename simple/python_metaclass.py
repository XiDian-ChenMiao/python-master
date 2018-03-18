#!/usr/bin/env python
# coding=utf-8
import re
class SayMetaClass(type):

    def __new__(cls, name, bases, attrs):
        attrs['say_' + name] = lambda self, value, saying=name: print(','.join([saying, value]))
        return type.__new__(cls, name, bases, attrs)


class Hello(object, metaclass=SayMetaClass):
    pass


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mapping = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s -> %s' % (k, v))
                mapping[k] = v
        for k in mapping.keys():
            attrs.pop(k)
        attrs['__mapping__'] = mapping # 保存属性和列的映射关系
        attrs['__table__'] = str(name) # 假设表名称与类名称一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        args = []
        for k, v in self.__mapping__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
            sql = 'INSERT INTO %s (%s) VALUES (%s)' % (self.__table__, ','.join(fields), str(args)[1:-1])
        print('SQL: %s' % sql)


class User(Model):
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')


if __name__ == '__main__':
    hello = Hello()
    hello.say_Hello('DAQINZHIDI')
    u = User(id=1503121727, name='XiDian-ChenMiao', email='daqinzhidi@163.com', password='password')
    u.save()

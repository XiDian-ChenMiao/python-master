# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: python的json测试
import json

person = dict(name='大秦之帝', age=23, school='西电')


def person2dict(person):
    return {
        'name': person._name,
        'age': person._age
    }


def dict2person(d):
    return Person(d['name'], d['age'])


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return 'Person-name:%s，-age:%s' % (self._name, self._age)


if __name__ == '__main__':
    print(json.dumps(person))
    print(json.loads(json.dumps(person)))
    p = Person('大秦之帝', 23)
    print('对象转为JSON为：', json.dumps(p, default=person2dict))
    print('JSON转为对象为：', json.loads(json.dumps(p, default=person2dict), object_hook=dict2person))

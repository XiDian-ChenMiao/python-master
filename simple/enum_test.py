#!/usr/bin/env python
# coding=utf-8
import enum
import unittest
import abc


class BaseEnum(enum.Enum):

    @classmethod
    def values(cls):
        values = []
        for attr in cls:
            values.append(attr.value)
        return values


class ABCBaseEnum(abc.ABC):
    @abc.abstractclassmethod
    def values(cls):
        cls_dict = cls.__dict__
        return [cls_dict[key] for key in cls_dict.keys() if not key.startswith('_') and key.isupper()]


class Gender(ABCBaseEnum):
    MALE = 1
    FEMALE = 2


class Direction(BaseEnum):

    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class TestBaseEnum(unittest.TestCase):

    def test_values(self):
        excepted = frozenset((Direction.UP.value, Direction.DOWN.value, \
                             Direction.LEFT.value, Direction.RIGHT.value))
        actual = frozenset(Direction.values())
        self.assertSetEqual(excepted, actual)

    def test_gender_values(self):
        excepted = frozenset([Gender.MALE, Gender.FEMALE])
        actual = frozenset(Gender.values())
        self.assertSetEqual(excepted, actual)

    def test_value_in(self):
        value = 1
        self.assertTrue(value in Direction.values())
        self.assertTrue(value in Gender.values())

    def test_value_equal(self):
        value = 1
        self.assertTrue(value == Direction.UP.value)
        self.assertTrue(value == Gender.MALE)


if __name__ == '__main__':
    unittest.main()

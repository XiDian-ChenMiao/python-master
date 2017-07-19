# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 用协程模拟教师处理作业
from collections import deque


def student(name, homeworks):
    """
    学生生成作业给老师
    :param name:
    :param homeworks:
    :return:
    """
    for homework in homeworks.items():
        yield (name, homework[0], homework[1])


class Teacher(object):
    def __init__(self, students):
        self.students = deque(students)

    def handle(self):
        while len(self.students):
            stu = self.students.pop()
            try:
                homework = next(stu)
                print('handle', homework[0], homework[1], homework[2])
            except StopIteration:
                pass
            else:
                self.students.appendleft(stu)


if __name__ == '__main__':
    Teacher([
        student('ST-1', {'MATH': '1 + 1 = 2', 'CS': 'OPERTATING SYSTEM'}),
        student('ST-2', {'MATH': '1 + 1 = 3', 'CS': 'COMPUTER GRAPHICS'}),
        student('ST-3', {'MATH': '1 + 1 = 4', 'CS': 'COMPLIER CONSTRUCTION'})
    ]).handle()



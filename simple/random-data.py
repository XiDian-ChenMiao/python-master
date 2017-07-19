# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 随机生成数据

import random
from collections import namedtuple
from functools import reduce

Student = namedtuple('Student', ['id', 'ans'])
N_Questions = 25
N_Students = 20


def gen_random_list(opts, n):
    return [random.choice(opts) for i in range(n)]


ANS = gen_random_list('ABCD', N_Questions)
SCORE = gen_random_list(range(1, 6), N_Questions)

QUIZE = list(zip(ANS, SCORE))
STUDENTS = [Student(_id, gen_random_list('ABCD*', N_Questions)) for _id in range(1, N_Students + 1)]


def normal(students, quize):
    for student in students:
        sid = student.id
        score = 0
        for i in range(len(quize)):
            if quize[i][0] == student.ans[i]:
                score += quize[i][1]
        print(sid, '\t', score)


def cal(quize):
    def inner(stu):
        filtered = filter(lambda x: x[0] == x[1][0], list(zip(stu.ans, quize)))
        reduced = reduce(lambda x, y: x + y[1][1], filtered, 0)
        print(stu.id, '\t', reduced)
    return inner


if __name__ == '__main__':
    print('ID\tScore')
    normal(STUDENTS, QUIZE)
    list(map(cal(QUIZE), STUDENTS))



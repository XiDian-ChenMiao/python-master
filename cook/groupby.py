#!/usr/bin/env python
# coding=utf-8
# 根据字段进行分组

rows = [
    {'address': '1 N A', 'date': '07/01/2017'},
    {'address': '2 N A', 'date': '07/02/2017'},
    {'address': '3 N A', 'date': '07/03/2017'},
    {'address': '4 N A', 'date': '07/03/2017'},
    {'address': '5 N A', 'date': '07/03/2017'},
    {'address': '6 N A', 'date': '07/02/2017'}
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print(date, ':')
    for item in items:
        print(' ', item)

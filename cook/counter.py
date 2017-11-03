#!/usr/bin/env python
# coding=utf-8
# 使用集合包中的计数器

from collections import Counter

INFO = """
    HELLO WORLD DAQINZHIDI
    HELLO WORLD DAQINZHIDI
    HELLO WORLD DAQINZHIDI
    HELLO WORLD DAQINZHIDI

    HELLO CHENMIAO
    DAQINZHIDI XIDIAN CHENMIAO
"""

a = Counter(INFO.split())
print('INFO COUNTER:', a)
NEXT_INFO = """
    PYTHON COOK
    FLUENT PYTHON
    HELLO PYTHON
"""

b = Counter(NEXT_INFO.split())
a.update(b)
print('UPDATE INFO:', a)
print('INFO - NEXT_INFO:', a - b)
print('INFO + NEXT_INFO:', a + b)


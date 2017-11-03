#!/usr/bin/env python
# coding=utf-8
# 利用堆找到最大或者最小的N个元素

import heapq

nums = [4, 2, 3, 4, 1, 6, 7, 8]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

userinfo = [{'name': 'XiDian-ChenMiao', 'age': 25},
            {'name': 'daqinzhidi', 'age': 24}]

print(heapq.nlargest(2, userinfo, key=lambda s: s['age']))

#!/usr/bin/env python
# coding=utf-8
# 从序列中移除重复元素并保持元素间顺序不变

def remove_dupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 1},
            {'x': 2, 'y': 1},
            {'x': 1, 'y': 2}
        ]
    print(list(remove_dupe(a, key=lambda s: (s['x'], s['y']))))

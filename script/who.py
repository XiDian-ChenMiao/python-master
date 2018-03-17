#!/usr/bin/env python
# coding=utf-8
# 利用linux系统内置who命令获取用户信息

import os
import re

if __name__ == '__main__':
    with os.popen('who', 'r') as f:
        for line in f:
            print(re.split(r'\s\s+|\t', line.rstrip()))

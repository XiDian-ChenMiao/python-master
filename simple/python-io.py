# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python的简单IO函数
from io import StringIO, BytesIO


def python_stringio():
    s = StringIO('Hello\nDAQINZHIDI')
    # s.write('\nHello\nChen Miao')
    print(s.getvalue())
    while True:
        p = s.readline()
        if p == '':
            break
        print(p.strip())


def python_bytesio():
    f = BytesIO()
    f.write('大秦之帝'.encode(encoding='utf-8'))
    print(f.getvalue())


if __name__ == '__main__':
    python_stringio()
    python_bytesio()

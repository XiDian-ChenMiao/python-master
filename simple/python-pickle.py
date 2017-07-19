# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 序列化与反序列化

import pickle

person = dict(name='大秦之帝', age=23, school='西电')
print(pickle.dumps(person))
f = open('dump.txt', 'wb')
pickle.dump(person, f)  # 将对象序列化转出到文件中
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
print(d)
f.close()

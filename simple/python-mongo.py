# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2017 Miao.Chen
# Summary: 利用PYTHON测试MONGO

from pymongo import MongoClient


client = MongoClient("localhost", 27017)

db = client['mongodb_user']  # 获取名称为mongodb_user的数据库
tb_user = db.tb_user  # 获取集合tb_user（相当于关系型数据库中的表）

user = {
    'username': 'daqinzhidi',
    'school': 'XiDian University',
    'gender': 'M',
    'age': 24,
    'address': {
        'province': 'Shaanxi',
        'city': "Baoji",
    }
}

result = tb_user.insert_one(user)
print('insert user, id : {0}'.format(result.inserted_id))

query_result = tb_user.find({
    'username': 'daqinzhidi'
})

print('document user count:', tb_user.count())

for user in query_result:
    print('user:', user)

tb_user.delete_many({'username': 'daqinzhidi'})








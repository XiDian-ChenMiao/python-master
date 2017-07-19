# coding:utf-8
import pymysql

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='786078509',
                             db='test',
                             charset='UTF8')
cur = connection.cursor()
cur.execute('select * from t_user')
res = cur.fetchall()
for row in res:
    print('uid=%s, username=%s, password=%s' % row)

connection.autocommit(False)  # 设置不自动提交
try:
    cur.execute("insert into t_user(username,password) values('陈苗','786078509')")
    print(cur.rowcount)  # 打印受影响的行数
    connection.commit()  # 提交事务
except Exception as e:
    print(e)
    connection.rollback()  # 事务回滚
cur.close()
connection.close()

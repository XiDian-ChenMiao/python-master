# coding:utf-8
import sys
import pymysql


class TransferMoney:
    def __init__(self, conn):
        self.conn = conn

    def transfer(self, src_aid, dst_aid, money):
        self.conn.autocommit(False)
        try:
            self.check_acc_available(src_aid)
            self.check_acc_available(dst_aid)
            self.has_enough_money(src_aid, money)
            self.operate_money(src_aid, money)
            self.operate_money(dst_aid, money, True)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_acc_available(self, accid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from t_account where aid = %s" % accid
            print('check_acc_available：' + sql)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s不存在' % accid)
        finally:
            cursor.close()

    def has_enough_money(self, accid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from t_account where aid = %s and money > %s" % (accid, money)
            print('has_enough_money：' + sql)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s余额不足' % accid)
        finally:
            cursor.close()

    def operate_money(self, accid, money, add_flag=False):
        cursor = self.conn.cursor()
        try:
            if not add_flag:
                sql = "update t_account set money = money - %s where aid = %s" % (money, accid)
            else:
                sql = "update t_account set money = money + %s where aid = %s" % (money, accid)
            print('operate_money：' + sql)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception('更新账户%s余额异常' % accid)
        finally:
            cursor.close()


if __name__ == '__main__':
    src_aid = sys.argv[1]
    dst_aid = sys.argv[2]
    tfr_money = sys.argv[3]

    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='786078509',
                                 db='test',
                                 charset='UTF8')

    transfer = TransferMoney(connection)
    try:
        transfer.transfer(src_aid, dst_aid, tfr_money)
    except Exception as e:
        print(e)
        connection.rollback()
    finally:
        connection.close()

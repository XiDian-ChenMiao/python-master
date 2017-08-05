# coding: utf8

from pymongo import MongoClient
from bson import Code


def get_db(db_name, host='localhost', port=27017):
    """
    获取数据库函数
    :param db_name: 数据库名称
    :param host: 数据库地址
    :param port: 访问端口
    :return: 数据库
    """
    client = MongoClient(host=host, port=port)
    db = client[db_name]
    return db


def get_collection(db, collection_name):
    """
    获取集合
    :param db: 数据库实例
    :param collection_name: 集合名称
    :return: 集合实例
    """
    return db[collection_name]


def main():
    """
    通过使用pymongo编写简单的mapreduce任务
    :return:
    """
    db = get_db('test')
    uniques = get_collection(db, 'uniques')
    map_func = Code('function() {emit(this.dim0, 1);}')
    red_func = Code('function(key, values) {return Array.sum(values);}')
    result = uniques.map_reduce(map=map_func, reduce=red_func, out='result')
    for doc in result.find():
        print(doc)


if __name__ == '__main__':
    main()
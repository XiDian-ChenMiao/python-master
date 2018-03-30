#!/usr/bin/env python
# coding=utf-8
import random
import sqlite3
import time

random.seed()
name = [c for c in 'ABCDEFGHIJKLMNOPQRST']
conn = sqlite3.connect('/home/daqinzhidi/programs/mbtiles4j/src/main/resources/master.db')

def generate_longitude_and_latitude():
    """
    generate longitude and latitude data ramdomly.
    """
    min_x = random.randint(-180, 180) # 西经
    max_x = random.randint(min_x, 180) # 东经
    min_y = random.randint(-90, 90) # 南纬
    max_y = random.randint(min_y, 90) # 北纬
    return min_x, max_x, min_y, max_y

def generate_metadata_name_and_timestamp():
    """
    generate name and timestamp of metadata
    """
    random.shuffle(name)
    meta_name = ''.join(name)
    timestamp = int(time.time() * 10**6)
    return meta_name, timestamp

def insert_metadata():
    """
    insert a metadata to sqlite3 database
    """
    name, timestamp = generate_metadata_name_and_timestamp()
    min_x, max_x, min_y, max_y = generate_longitude_and_latitude()
    cur = conn.cursor()
    cur.execute("insert into metadata(pyramid_name, timestamp, west, east, south, north) \
                       values (?, ?, ?, ?, ?, ?)", (name, timestamp, min_x, max_x, min_y, max_y, ))
    cur.close()

def insert(cnt=10000):
    """
    insert metadata by the given number
    """
    for i in range(cnt):
        insert_metadata()
    conn.commit()
    cur = conn.cursor()
    cur.execute('select count(*) from metadata')
    print('current metadata capacity: %d' % cur.fetchone())
    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert()

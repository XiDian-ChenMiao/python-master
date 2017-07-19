# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试Python的解析模块ConfigParser

import configparser
cp = configparser.ConfigParser()
cp.read('config.ini', encoding='utf-8')
sections = cp.sections()
print('Sections：', sections)
opts = cp.options('sec_a')
print('Options in sec_a：', opts)
kvs = cp.items('sec_a')
print('Items in sec_a：', kvs)

str_val = cp.get('sec_a', 'a_key1')
int_val = cp.getint('sec_a', 'a_key2')
print('Value for sec_a[a_key1]', str_val)
print('Value for sec_a[a_key2]', int_val)
cp.set("sec_b", "b_key3", "new-$r")
cp.set("sec_b", "b_newkey", "new-value")
cp.add_section('a_new_section')
cp.set('a_new_section', 'new_key', 'new_value')
cp.write(open("config.conf", "w"))

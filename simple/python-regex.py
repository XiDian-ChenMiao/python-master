# coding:utf-8
import re

'''
正则表达式的应用
'''


def add_one(matcher):
    return str(int(matcher.group()) + 1)


if __name__ == '__main__':
    pattern = re.compile(r'[a-zA-Z][\w]{6,15}@(163|126).com')
    match = pattern.match('daqinzhidi@163.com')
    print(match.group())
    print(re.split(r':| |,', 'Name:daqinzhidi,Age:23,Favorite:Basketball PingPang'))

    message = 'China has 5000 years history and has 56 nations.'
    print(re.findall(r'\d+', message))

    count = 'Foods:25,Vegetables:30'
    print(re.sub(r'\d+', add_one, count))

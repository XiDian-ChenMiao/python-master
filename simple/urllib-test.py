# coding:utf-8

import urllib.request
import http.cookiejar
"""
测试网页下载器库的使用
"""
url = 'http://www.baidu.com'
print('第一种方法：')

res = urllib.request.urlopen(url)
print('状态码：', res.getcode())
print('内容长度为：', len(res.read()))

print('第二种方法')
req = urllib.request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
res = urllib.request.urlopen(url)
print('状态码：', res.getcode())
print('内容长度为：', len(res.read()))

print('第三种方法')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
res = urllib.request.urlopen(url)
print('状态码：', res.getcode())
print('内容为：', res.read())
print('Cookie内容为：', cj)

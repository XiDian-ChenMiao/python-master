# coding:utf-8

from bs4 import BeautifulSoup
import re

HTML_CONTENT = "<a href='http://www.baidu.com'>百度</a>"

soup = BeautifulSoup(HTML_CONTENT, 'html.parser', from_encoding='utf-8')
node = soup.find('a', href=re.compile(r'^http'), string='百度')
print('节点名称：', node.name)
print('节点链接：', node['href'])
print('节点内容：', node.get_text())

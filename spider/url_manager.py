# coding:utf-8
"""
Created on 2016年8月29日
@author: Administrator
"""


class UrlManager:
    """
    URL的管理器
    """
    def __init__(self):
        self.old_urls = set()
        self.new_urls = set()

    '''获取新的URL地址'''

    def get_new_url(self):
        return self.new_urls.pop()

    '''添加新的URL地址'''

    def add_new_url(self, new_url):
        if not new_url:
            return
        if new_url in self.old_urls or new_url in self.new_urls:
            return
        self.new_urls.add(new_url)

    '''是否有新的URL地址'''

    def has_new_url(self):
        return len(self.new_urls) != 0

    '''将URL集合添加进URL管理器中'''

    def add_new_urls(self, urls):
        if not urls or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

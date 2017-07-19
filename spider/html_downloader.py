# coding:utf-8
"""
Created on 2016年8月29日
@author: Administrator
"""
import urllib.request


class HtmlDownloader:
    """
    HTML的下载器
    """
    def download(self, url):
        if url is None:
            return
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()

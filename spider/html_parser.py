# coding:utf-8
"""
Created on 2016年8月29日
@author: Administrator
"""

from bs4 import BeautifulSoup
import urllib.parse
import re


class HtmlParser:
    """
    HTML的解析器
    """
    '''获取新的URL集合'''

    def _get_new_urls(self, page_url, soup):
        all_links = set()
        linknodes = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for node in linknodes:
            all_links.add(urllib.parse.urljoin(page_url, node['href']))
        return all_links

    '''从给定URL地址中获取关注信息'''

    def _get_new_data(self, page_url, soup):
        data = dict()
        data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1 >c++</h1>
        data['title'] = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        data['summary'] = soup.find('div', class_='lemma-summary').get_text()
        return data

    '''根据当前URL地址和输出的内容来解析新的URL和当前页面对应的关注信息'''

    def parse(self, page_url, html_content):
        if not page_url:
            return None
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

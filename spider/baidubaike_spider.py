#!/usr/bin/env python
# coding=utf-8
import requests
from urllib.parse import urljoin
import re
from bs4 import BeautifulSoup
import codecs

class UrlManager(object):
    """
    URL管理器
    """
    def __init__(self):
        self.new_urls = set() # 未爬取的URL集合
        self.old_urls = set() # 已爬取的URL集合

    def has_new_url(self):
        """
        判断是否仍有待爬取的URL
        """
        return self.new_url_size() != 0

    def new_url_size(self):
        """
        获取未爬取集合的URL数目
        """
        return len(self.new_urls)

    def get_new_url(self):
        """
        获取一个未爬取的URL
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        """
        向未爬取的URL集合中添加元素
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        向未爬取的URL集合中添加新集合
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def old_url_size(self):
        """
        获取已经爬取过的URL集合大小
        """
        return len(self.old_urls)


class HtmlDownloader(object):
    """
    HTML下载器
    """
    def download(self, url):
        """
        download a given url
        :param url: a url which need to download
        :return: the content of this url
        """
        if url is None:
            return
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None


class HtmlParser(object):
    """
    HTML解析器
    """
    def parser(self, page_url, html_cont):
        """
        parse a given html page
        :param page_url: the url path
        :param html_cont: the content of this url
        :return: a turple about new urls and the dictionary of this url
        """
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        """
        get some new urls which need to download through this page url
        :param page_url: the given url
        :param soup: the object of BeautifulSoup
        :return: the new urls set need to download
        """
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        get content dictionary by given page_url
        :param page_url: the given url
        :param soup: the object of BeautifulSoup
        :return: the dictionary about this url content
        """
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data


class DataOutput(object):
    """
    数据存储器
    """
    def __init__(self):
        self.datas = []

    def store_data(self, data):
        """
        store data info
        :param data: data object
        """
        if data is None:
            return
        self.datas.append(data)

    def output_html(self, path):
        """
        output data info by some format
        :param path: the absolute path to output
        """
        if path is None:
            return
        import os
        fout = codecs.open(os.path.abspath(path), 'w', encoding='utf-8')
        fout.write('<html><body><table>')
        for data in self.datas:
            fout.write('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (data['url'], data['title'], data['summary']))
            self.datas.remove(data)
        fout.write('</table></body></html>')
        fout.close()


class SpiderManager(object):
    """
    爬虫调度器
    """
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url, path='result.html'):
        """
        crawl function
        :param root_url: the seed url to crawl
        """
        self.manager.add_new_url(root_url)
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print('have crawled %d links.' % self.manager.old_url_size())
            except Exception as e:
                print('crawled error, reason: %s.' % e)
        self.output.output_html(path)


if __name__ == '__main__':
    spider_man = SpiderManager()
    spider_man.crawl('http://baike.baidu.com/view/284853.htm')


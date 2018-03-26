#!/usr/bin/env python
# coding=utf-8
import re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from multiprocessing.managers import BaseManager


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers, verify=False)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/\w+'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data


class SpiderWorkNode(object):
    """
    爬虫工作节点
    """
    def __init__(self):
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')
        server_addr = '127.0.0.1'
        print('connect to server %s...' % server_addr)
        self.m = BaseManager(address=(server_addr, 8001), authkey='daqinzhidi'.encode('utf-8'))
        self.m.connect()
        self.task = self.m.get_task_queue()
        self.result = self.m.get_result_queue()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        print('initize finish.')

    def crawl(self):
        while True:
            try:
                if not self.task.empty():
                    url = self.task.get()
                    if url == 'end':
                        print('worker node reveived a signal to end crawling.')
                        self.result.put({'new_urls': 'end', 'data': 'end'})
                        return
                    print('crawl node is parsing now: %s' % url)
                    content = self.downloader.download(url)
                    new_urls, data = self.parser.parser(url, content)
                    self.result.put({'new_urls': new_urls, 'data': data})
            except EOFError as e:
                print('connect failed.')
                return
            except Exception as e:
                print('crawled error, reason: %s' % e)


if __name__ == '__main__':
    spider = SpiderWorkNode()
    spider.crawl()

# coding:utf-8
"""
Created on 2016年8月29日
@author: Administrator
"""
import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain:
    """爬虫调度类"""

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)  # URL管理器添加新的URL
        count = 1
        while self.urls.has_new_url():  # 判断URL管理器中是否可以获取新的URL
            try:
                new_url = self.urls.get_new_url()  # 获取新的URL
                print('当前正在爬第%d个页面，地址为：%s' % (count, new_url))
                html_content = self.downloader.download(new_url)  # 从新的URL取出对应的内容
                new_urls, new_data = self.parser.parse(new_url, html_content)  # 从内容中解析出合适的新的URL集合和当前URL对应的内容信息
                self.urls.add_new_urls(new_urls)  # 将获取到的新的URL添加到URL管理器中
                self.outputer.collect_data(new_data)  # 输出器接收要显示的数据
                if count == 10:
                    break
                count += 1
            except Exception as e:
                print('当前页面爬虫异常工作')
                print(e)
        self.outputer.output()  # 输出器打印出爬虫找到的信息


JAVA_URL_ROOT = 'http://baike.baidu.com/view/21087.htm'
if __name__ == '__main__':
    target_spider = SpiderMain()
    target_spider.craw(JAVA_URL_ROOT)

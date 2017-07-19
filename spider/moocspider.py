# coding:utf-8
import re
import requests


class MoocSpider:
    """慕课网爬虫"""

    def get_all_links(self, base, count):
        links = []
        for i in range(count):
            links.append(base + str(i + 1))
        return links

    def get_text(self, url):
        return requests.get(url).text

    def geteveryclass(self, html_content):
        allclasses = re.findall(r'<div class="moco-course-box">.*?</span></div>', html_content, re.S)
        return allclasses

    def getinfo(self, every_class):
        course_info = []
        course_info.append(re.search(r'<img  alt="(.*?)"', every_class, re.S).group(1))
        course_info.append(re.search(r'<p>(.*?)</p>', every_class, re.S).group(1))
        course_info.append(re.search(r'<span class="l"> (\d+)人在学</span>', every_class, re.S).group(1))
        return course_info

    def saveinfo(self, infos):
        fout = open('mooc_courses.txt', 'a')
        for message in infos:
            # message = json.load(message)
            fout.writelines('课程名：' + message[0] + '\n')
            fout.writelines('课程介绍：' + message[1] + '\n')
            fout.writelines('选课人数：' + message[2] + '\n\n')
        fout.close()


if __name__ == '__main__':
    classinfo = []
    _url = 'http://www.imooc.com/course/list?page='
    mooc_spider = MoocSpider()
    all_links = mooc_spider.get_all_links(_url, 5)
    for link in all_links:
        print('正在爬取页面：', link)
        html = mooc_spider.get_text(link)
        everyclass = mooc_spider.geteveryclass(html)
        for each in everyclass:
            info = mooc_spider.getinfo(each)
            print(info)
            # mooc_spider.saveinfo(info)

            # print('读取课程文件：')
            # f = open('mooc_courses.txt', 'r')
            # print(f.read())

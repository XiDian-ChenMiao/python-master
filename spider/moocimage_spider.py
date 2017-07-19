# coding:utf-8
import requests
import threading
import urllib.parse
import urllib
import os
import html.parser as h

image_urls = []  # 存放生产者线程生成的图片的URL列表集合
condition = threading.Condition()  # 线程条件用于同步生产者与消费者
url = 'http://www.maiziedu.com/course/list/?catagory='


class ImageProducer(threading.Thread):
    def __init__(self, url_root):
        super().__init__()
        self.url_root = url_root

    def run(self):
        global image_urls
        global condition
        print('图片生产者线程开启......')
        content = self._get_url_content()
        condition.acquire()
        self._get_image_urls(content)
        condition.notify_all()
        condition.release()

    def _get_url_content(self):
        res = requests.get(url)
        return res.text

    def _get_image_urls(self, content):
        parser = ImageParser()
        parser.feed(content)


class ImageConsumer(threading.Thread):
    def run(self):
        print('图片消费者线程开启......')
        while True:
            global image_urls
            global condition
            condition.acquire()
            print('正在尝试下载图片，现在库中还有%d条地址' % len(image_urls))
            while len(image_urls) == 0:
                condition.wait()
            image_url = image_urls.pop()
            self._download_image(image_url)
            condition.release()

    def _download_image(self, image_url, folder='image'):
        if not os.path.isdir(folder):
            os.mkdir(folder)
        print('正在下载图片：%s' % image_url)

        def _fname(s):
            return os.path.join(folder, os.path.split(s)[1])
        r = requests.get(image_url)
        with open(_fname(image_url), 'wb') as f:
            f.write(r.content)


class ImageParser(h.HTMLParser):
    def __init__(self):
        super(ImageParser, self).__init__()
        self.in_p = False

    def handle_data(self, data):
        super().handle_data(data)

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            if len(attrs) == 0:
                self.in_p = True
        if self.in_p and tag == 'img':
            if len(attrs) != 0 and self._get_value_in_attrs(attrs, 'src'):
                image_urls.append(urllib.parse.urljoin(url, self._get_value_in_attrs(attrs, 'src')))
                print('图片列表中添加了图片：%s，现在已有图片：%d' % (
                    urllib.parse.urljoin(url, self._get_value_in_attrs(attrs, 'src')), len(image_urls)))

    def _get_value_in_attrs(self, attrs, attribute):
        for element in attrs:
            if attribute in element:
                return element[1]
        return None

    def handle_endtag(self, tag):
        if tag == 'p':
            self.in_p = False


if __name__ == '__main__':
    ImageProducer(url).start()
    for i in range(6):
        ImageConsumer().start()

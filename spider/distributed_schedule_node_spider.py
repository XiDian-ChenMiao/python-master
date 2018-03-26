#!/usr/bin/env python
# coding=utf-8
try:
    import cPickle as pickle
except ImportError:
    import pickle

import hashlib
import time
import codecs
from multiprocessing.managers import BaseManager
from multiprocessing import Queue, Process


class UrlManager(object):

    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt')
        self.old_urls = self.load_progress('old_urls.txt')

    def has_new_url(self):
        return self.new_url_size() != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url.encode('utf-8'))
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url

    def add_new_url(self, url):
        if url is None:
            return
        m = hashlib.md5()
        m.update(url.encode('utf-8'))
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)

    def save_progress(self, path, data):
        with open(path, 'wb') as f:
            pickle.dump(data, f)

    def load_progress(self, path):
        print('[+] load progress: %s' % path)
        try:
            with open(path, 'rb') as f:
                tmp = pickle.load(f)
                return tmp
        except:
            print('[!] without progress file, create: %s' % path)
        return set()


class DataOutput(object):
    def __init__(self):
        self.filepath = 'baike_%s.html' % (time.strftime('%Y_%m_%d_%H_%M_%S',\
                                                         time.localtime()))
        self.output_head(self.filepath)
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_html(self.filepath)

    def output_head(self, path):
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.write('<html><body><table>')
        fout.close()

    def output_html(self, path):
        fout = codecs.open(path, 'a', encoding='utf-8')
        for data in self.datas:
            fout.write('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (data['url'], data['title'], data['summary']))
            self.datas.remove(data)
        fout.close()

    def output_end(self, path):
        fout = codecs.open(path, 'a', encoding='utf-8')
        fout.write('</table></body></html>')
        fout.close()


class ControlManager(object):
    """
    控制调度器主要产生并启动URL管理进程、数据提取进程和数据存储进程，同时维护下面四个队列保持进程间通信
    url_q:队列是URL管理进程将URL传递给爬虫节点的通道
    result_q:队列是爬虫节点将数据返回给数据提取进程的通道
    conn_q:队列是数据提取进程将新的URL数据提交给URL管理进程的通道
    store_q:队列是数据提取进程将获取到的数据交给数据存储进程的通道
    """
    def start_manager(self, url_q, result_q):
        BaseManager.register('get_task_queue', callable=lambda:url_q)
        BaseManager.register('get_result_queue', callable=lambda:result_q)
        manager = BaseManager(address=('', 8001), authkey='daqinzhidi'.encode('utf-8'))
        return manager

    def url_manager_proc(self, url_q, conn_q, root_url):
        url_manager = UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            while (url_manager.has_new_url()):
                new_url = url_manager.get_new_url()
                url_q.put(new_url)
                print('old_url = ', url_manager.old_url_size())
                if (url_manager.old_url_size() > 10):
                    url_q.put('end')
                    print('control node send a signal to worker node to end crawling.')
                    url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt', url_manager.old_urls)
                    return
            try:
                if not conn_q.empty():
                    urls = conn_q.get()
                    url_manager.add_new_urls(urls)
            except BaseException as e:
                time.sleep(0.1)

    def result_solve_proc(self, result_q, conn_q, store_q):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        print('analysis process receive a message to end.')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])
                    store_q.put(content['data'])
                else:
                    time.sleep(0.1)
            except BaseException as e:
                time.sleep(0.1)

    def store_proc(self, store_q):
        output = DataOutput()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    print('storage process receive a message to end.')
                    output.output_end(output.filepath)
                    return
            else:
                time.sleep(0.1)


if __name__ == '__main__':
    url_q = Queue()
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()

    node = ControlManager()
    manager = node.start_manager(url_q, result_q)
    url_manager_proc = Process(target=node.url_manager_proc, args=(url_q, conn_q, 'http://baike.baidu.com/view/284853.htm', ))
    result_solve_proc = Process(target=node.result_solve_proc, args=(result_q, conn_q, store_q, ))
    store_proc = Process(target=node.store_proc, args=(store_q, ))
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    manager.get_server().serve_forever()

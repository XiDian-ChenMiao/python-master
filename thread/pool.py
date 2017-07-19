# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2017 Miao.Chen
# Summary: 线程池与进程池的使用
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import time
import urllib.request


def return_future_result(message):
    time.sleep(2)
    return message


def thread_call():
    pool = ThreadPoolExecutor(max_workers=2)
    one = pool.submit(return_future_result, ('daqinzhidi'))
    two = pool.submit(return_future_result, ('python'))
    print(one.done())  # 判读第一个任务是否结束
    time.sleep(3)
    print(two.done())
    print(one.result(), two.result())


def process_call():
    pool = ProcessPoolExecutor(max_workers=2)
    one = pool.submit(return_future_result, ('daqinzhidi'))
    two = pool.submit(return_future_result, ('python'))
    print(one.done())  # 判读第一个任务是否结束
    time.sleep(3)
    print(two.done())
    print(one.result(), two.result())


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def thread_submit_call():
    urls = ['http://httpbin.org', 'http://example.com/', 'https://api.github.com/']
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_to_url = {executor.submit(load_url, url, 60) : url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))


if __name__ == '__main__':
    thread_submit_call()
    thread_call()
    process_call()




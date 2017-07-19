# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python的wsgi
from wsgiref.simple_server import make_server


def application(environ, start_response):
    print('请求信息为：', environ)
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH'][1:] or 'DAQINZHIDI')
    return [body.encode('utf-8')]


if __name__ == '__main__':
    # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
    httpd = make_server('', 9000, application)
    print('在8000端口上开启模拟WSGI服务器...')
    # 开始监听HTTP请求:
    httpd.serve_forever()

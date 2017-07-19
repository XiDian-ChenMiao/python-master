# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试利用POP协议接收邮件
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


# 下载邮件
def download_email():
    email = input('输入邮件地址：')
    pwd = input('输入登录密码：')
    pop_server = input('输入POP3服务器：')
    server = poplib.POP3(pop_server)  # 连接到pop3服务器
    server.set_debuglevel(1)  # 可以打开或者关闭调试信息
    print(server.getwelcome().decode('utf-8'))  # 打印POP3服务器的欢迎文字
    # 验证密码信息
    server.user(email)
    server.pass_(pwd)
    print('邮件数量为：%s，占用空间为：%s' % server.stat())
    resp, mails, octets = server.list()  # 返回所有邮件的编号
    print(mails)

    # 获取最新一封邮件，索引号从1开始
    index = len(mails)
    resp, lines, octets = server.retr(index)
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)
    return msg


# 解析邮件
def parse_email(email, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = email.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_header(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s:%s' % (' ' * indent, header, value))
    if email.is_multipart():
        parts = email.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            parse_email(part, indent + 1)
    else:
        content_type = email.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = email.get_payload(decode=True)
            charset = guess_charset(email)
            if charset:
                content = content.decode(encoding=charset)
            print('%sText: %s' % (' ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % (' ' * indent, content_type))


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

if __name__ == '__main__':
    parse_email(download_email())

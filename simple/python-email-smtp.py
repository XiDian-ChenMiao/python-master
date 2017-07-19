# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 使用python的内置库通过STMP协议发送邮件
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr


# 生成邮件
def generate_email(message, subtype='plain'):
    # 第一个参数表示邮件正文，第二个参数表示类型，传入‘plain’表示纯文本，最后通过第三个编码参数保证多语言的兼容性
    msg = MIMEText(message, subtype, 'utf-8')
    return msg


# 格式化邮件地址
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 发送邮件
def transfer_email(email, from_addr, password, to_addr, stmp_server):
    email['From'] = _format_addr('大秦之帝 <%s>' % from_addr)
    email['To'] = _format_addr('管理员 <%s>' % to_addr)
    email['Subject'] = Header('测试SMTP', 'utf-8').encode()
    server = smtplib.SMTP(stmp_server, 25)  # SMTP协议默认的端口为25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], email.as_string())
    server.quit()
    print('邮件发送成功')


# 测试带附件的邮件发送
def transfer_with_attachment(message, from_addr, password, to_addr, stmp_server, subtype='plain'):
    msg = MIMEMultipart()  # 生成邮件对象
    msg['From'] = _format_addr('大秦之帝 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('测试SMTP', 'utf-8').encode()
    msg.attach(generate_email(message, subtype=subtype))
    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('ZYJ.jpg', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'jpeg', filename='ZYJ.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='ZYJ.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    server = smtplib.SMTP(stmp_server, 25)  # SMTP协议默认的端口为25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print('邮件发送成功')


if __name__ == '__main__':
    start = input('请输入邮件的发出地：')
    passwd = input('请输入邮件的发出地口令：')
    end = input('请输入邮件的接收地：')
    stmp_serv = input('请输入SMTP服务器的地址：')
    message = '''
        <html><body><h1>您好，我是大秦之帝。</h1><p>由<a href="http://www.python.org">Python</a>客户端发送此邮件，请查收。</p>
        </body></html>
    '''
    message_with_attachment = '''
        <html><body><h1>您好，我是大秦之帝。</h1><p>由<a href="http://www.python.org">Python</a>客户端发送此邮件，请查收。</p>
        <p>附件为：<img src="cid:0"></p>
        </body></html>
    '''
    # transfer_email(generate_email(message, subtype='html'), start, passwd, end, stmp_serv)
    transfer_with_attachment(message_with_attachment, start, passwd, end, stmp_serv, subtype='html')

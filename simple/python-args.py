# coding:utf-8
import sys
import argparse


def pythonargs(*args, **kwargs):
    for a in args:
        print(a)
    for kw in kwargs:
        print('关键字为：%s，值为：%s' % (kw, kwargs[kw]))

def main(args):
    print('address:{}'.format(args.code_address))
    print('flag:{}'.format(args.flag))
    print('port:{}'.format(args.port))

if __name__ == '__main__':
    pythonargs(2, 3, name='daqinzhidi')
    print('命令行参数个数：', len(sys.argv))
    print('脚本名称：', sys.argv[0])
    if len(sys.argv) > 1:
        print('参数列表：', '#'.join(sys.argv[1:]))

    parser = argparse.ArgumentParser(usage="it's usage tip.", description='help info.')
    parser.add_argument('--address', default='localhost', help='the address.', dest='code_address')
    parser.add_argument('--flag', choices=['.txt', '.jpg', '.xml'], default='.txt', help='the file type.')
    parser.add_argument('--port', type=int, required=True, help='the port number.')
    args = parser.parse_args()
    main(args)

# coding:utf-8
import os
import socket
import socketserver
import threading


class DataHdl(socketserver.StreamRequestHandler):
    def handle(self):
        pass


def get_file(host, port, filepath):
    # print('start connect...',host,port)
    s = socket.socket()
    s.connect((host, port))
    filepath = os.path.join('.', 'bakt', filepath)
    f = open(filepath, 'wb')
    data = True
    while data:
        data = s.recv(1024)
        if data:
            f.write(data)
    s.close()
    f.close()


def put_file(host, port, filepath):
    # print('start connect...',host,port)
    s = socket.socket()
    s.connect((host, port))
    f = open(filepath, 'rb')
    while True:
        data = f.read(1024)
        if data:
            s.sendall(data)
        else:
            break
    s.close()
    f.close()


class FtpCient:
    def __init__(self, host='localhost', port=21):
        self.host = host
        self.port = port
        self.cmds = ('QUIT', 'USER', 'NOOP', 'TYPE',
                     'PASV', 'PORT', 'RETR', 'STOR')
        self.linesep = '\n'
        self.data_port = None
        self.loged = False
        self.sock = None
        self.pasv_mode = None
        self.pasv_host = None
        self.pasv_port = None

    def cmd_connect(self):
        print('connect')
        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))
        self.data_port = self.sock.getsockname()[0]

    def start(self):
        print('命令列表：', self.cmds)
        self.cmd_connect()
        self.login()
        while True:
            cmd = input('请输入命令：')
            if not cmd:
                print('请输入命令：')
                continue
            cmd, args = self.split_args(cmd)
            if not self.send_cmd(cmd, args):
                continue
            res = self.readline(self.sock)
            print(res)
            if cmd.startswith('PASV') and res.startswith('227'):
                self.pasv_mode = True
                servinfos = res[res.index('(') + 1:res.index(')')]
                self.pasv_host = '.'.join(servinfos.split(',')[:4])
                servinfos = servinfos.split(',')[-2:]
                self.pasv_port = 256 * int(servinfos[0]) + int(servinfos[1])
                # print(self.pasv_host,self.pasv_port)
            if cmd.startswith('RETR'):
                if self.pasv_mode:
                    threading.Thread(target=get_file,
                                     args=(self.pasv_host, self.pasv_port, args)).start()
            if cmd.startswith('STOR'):
                if self.pasv_mode:
                    threading.Thread(target=put_file,
                                     args=(self.pasv_host, self.pasv_port, args)).start()
            if cmd.startswith('QUIT'):
                break
            args = ''
        self.sock.close()
        self.sock = None

    def login(self):
        if self.sock:
            self.send_cmd('USER')
            res = self.readline(self.sock)
            if res.startswith('230'):
                print('Login successful as anonymous!')
                self.loged = True

    def readline(self, sock):
        data = ''
        while not data.endswith(self.linesep):
            d = sock.recv(1)
            data += d.decode('utf-8')
        return data

    def split_args(self, cmds):
        if ' ' in cmds:
            cmdlsts = cmds.split(' ')
            cmd = cmdlsts[0]
            args = ' '.join(cmdlsts[1:])
        else:
            cmd = cmds
            args = ''
        return cmd.upper(), args

    def send_cmd(self, cmd, args=''):
        if self.sock:
            if args:
                cmd = ' '.join((cmd, args))
            if cmd.startswith('RETR') or cmd.startswith('STOR'):
                if self.pasv_mode is None:
                    print('Please appoint port or stor mode.')
                    return False
                if not args:
                    return False
            if cmd.startswith('STOR'):
                if args:
                    if not os.path.exists(args):
                        print('File is not exist.')
                        return False
                else:
                    print('Please offer filename.')
                    return False
            cmd += self.linesep
            self.sock.sendall(cmd.encode('utf-8'))
            return True


if __name__ == '__main__':
    fc = FtpCient()
    fc.start()

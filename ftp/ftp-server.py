# coding:utf-8
import socketserver
import threading
import time
import os


class DataHdl(socketserver.StreamRequestHandler):
    client_opr = {}

    def handle(self):
        peerip = self.request.getpeername()[0]
        print(peerip, 'connected!')
        opr = self.get_opr_args(peerip)
        if opr:
            if opr[0] == 'RETR':
                self.retr_file(opr[1])
            elif opr[0] == 'STOR':
                self.stor_file(opr[1])
        self.request.close()

    def get_opr_args(self, peerip):
        if peerip in self.client_opr:
            opr = self.client_opr[peerip].pop(0)
            if not self.client_opr[peerip]:
                self.client_opr.pop(peerip)
            return opr

    def retr_file(self, filepath):
        f = open(filepath, 'rb')
        while True:
            data = f.read(1024)
            if data:
                self.request.sendall(data)
            else:
                break
        f.close()

    def stor_file(self, filepath):
        f = open(os.path.join('.', 'bakt', filepath), 'wb')
        while True:
            data = self.request.recv(1024)
            if data:
                f.write(data)
            else:
                break
        f.close()


class FTPHdl(socketserver.StreamRequestHandler):
    def __init__(self, request=None, client_address=None, server=None):
        self.coms_keys = ('QUIT', 'USER', 'NOOP', 'TYPE',
                          'PASV', 'PORT', 'RETR', 'STOR')
        self.coms = {}
        self.init_coms()
        self.server = server
        self.cmd_port = 21
        self.data_port = 20
        self.pasv_data_ip = None
        self.pasv_data_port = None
        self.cmd_args = None
        self.loged = False
        self.pasv_mode = None
        super().__init__(request, client_address, server)

    def handle(self):
        while True:
            cmds = self.rfile.readline()
            if not cmds:
                break
            cmds = cmds.decode('utf-8')
            # print(cmds)
            cmd = self.deal_args(cmds)
            if cmd in self.coms_keys:
                self.coms.get(cmd)()
            else:
                self.send(500, 'Invalid command.')
            if cmd == 'QUIT':
                break

    def deal_args(self, cmds):
        if ' ' in cmds:
            cmd, args = cmds.split(' ')
            args = args.strip('\n')
        else:
            cmd = cmds.strip('\n')
            args = ''
        if args:
            self.args = args
        return cmd.upper()

    def init_coms(self):
        for k in self.coms_keys:
            self.coms[k] = getattr(self, 'exe_' + k.lower())

    def exe_quit(self):
        self.send(221, 'bye')

    def exe_user(self):
        user = ''
        if user in ['', 'anonymous']:
            user = 'anonymous'
            self.loged = True
            self.send(230, 'identified!')
        else:
            self.send(530, 'Only use anonymous')

    def exe_pasv(self):
        if not self.loged:
            self.send(332, 'Please login.')
            return
        if self.pasv_mode:
            info = 'entering passive mode (%s)' % self.make_pasv_info()
            self.send(227, info)
            return
        try:
            self.enter_pasv()
            info = 'entering passive mode (%s)' % self.make_pasv_info()
            self.pasv_mode = True
            self.send(227, info)
        except Exception as e:
            print(e)
            self.send(500, 'failure change to passive mode')

    def make_pasv_info(self):
        ip_info = self.pasv_data_ip.split('.')
        ip_info = ','.join(ip_info)
        port_a = str(self.pasv_data_port // 256)
        port_b = str(self.pasv_data_port % 256)
        return ','.join((ip_info, port_a, port_b))

    def enter_pasv(self):
        if self.server.data_server is None:
            self.pasv_data_ip, self.pasv_data_port = self.server.create_data_server()

    def exe_port(self):
        self.send(500, 'Do not offer port mode.')

    def exe_noop(self):
        self.send(200, 'ok')

    def exe_type(self):
        self.send(200, 'ok')

    def exe_retr(self):
        if not os.path.exists(self.args):
            self.send(550, 'file failure')
            return
        client_addr = self.request.getpeername()[0]
        self.add_opr_file(client_addr, ('RETR', self.args))
        self.send(150, 'ok')

    def exe_stor(self):
        client_addr = self.request.getpeername()[0]
        self.add_opr_file(client_addr, ('STOR', self.args))
        self.send(150, 'ok')

    def add_opr_file(self, client_addr, item):
        if client_addr in DataHdl.client_opr:
            DataHdl.client_opr[client_addr].append(item)
        else:
            DataHdl.client_opr[client_addr] = [item, ]

    def send(self, code, info):
        infos = '%d %s\n' % (code, info)
        self.request.sendall(infos.encode('utf-8'))


class MyThrTCPServ(socketserver.ThreadingTCPServer):
    def __init__(self, addr, Hdl):
        self.data_server = None
        super().__init__(addr, Hdl)

    def shutdown(self):
        if self.data_server:
            threading.Thread(target=self.data_server.shutdown).start()
        super().shutdown()

    def create_data_server(self):
        self.data_server = socketserver.ThreadingTCPServer(('127.0.0.1', 0), DataHdl)
        pasv_data_ip, pasv_data_port = self.data_server.server_address
        threading.Thread(target=self.data_server.serve_forever).start()
        return pasv_data_ip, pasv_data_port


if __name__ == '__main__':
    server = MyThrTCPServ(('127.0.0.1', 21), FTPHdl)
    threading.Thread(target=server.serve_forever).start()
    print('start')
    time.sleep(300)
    server.shutdown()

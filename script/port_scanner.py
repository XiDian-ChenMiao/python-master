#!/usr/bin/env python
# coding=utf-8
import socket
from socket import setdefaulttimeout
import argparse
import threading

lock = threading.Lock()
port_opening_cnt = 0
threads = []

def port_scanner(host, port):
    global port_opening_cnt
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        lock.acquire()
        port_opening_cnt += 1
        print('[+] {port} open'.format(port=port))
        lock.release()
        s.close()
    except:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((host, port))
        lock.acquire()
        port_opening_cnt += 1
        print('[+] {port} open'.format(port=port))
        lock.release()
        s.close()


def main():
    p = argparse.ArgumentParser(description='port_scanner...')
    p.add_argument('-host', dest='hosts', type=str, help='host address', default='localhost')
    p.add_argument('-from', dest='port_from', type=int, help='the start of scanning', default=0)
    p.add_argument('-to', dest='port_end', type=int, help='the end of scanning', default=1024)
    args = p.parse_args()
    host_list = args.hosts.split(',')
    setdefaulttimeout(1)
    for host in host_list:
        print('scanning the host: %s.' % host)
        for p in range(args.port_from, args.port_end):
            t = threading.Thread(target=port_scanner, args=(host, p))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        print('[*] The host: %s scan is complete.' % host)
        print('[*] A total of %d openning port.' % port_opening_cnt)

if __name__ == '__main__':
    main()

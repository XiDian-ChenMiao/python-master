#!/usr/bin/env python
# coding: utf-8
import os
import subprocess
import argparse
import time
import telnetlib

host = '127.0.0.1'
port = 8080

def external_cmd(cmd, msg_in=''):
    """
    execute system command
        :param cmd: command
        :param msg_in='': some messages you want to communicate with process
    """
    try:
        proc = subprocess.Popen(cmd, shell=True, 
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        stdout_val, stderr_val = proc.communicate(msg_in)
        return stdout_val, stderr_val
    except ValueError as err:
        return None, None
    except IOError as err:
        return None, None


def shutdown(tomcat_path):
    """
        close tomcat service
        :param tomcat_path: tomcat home
    """
    os.system(os.path.join(tomcat_path, "bin/shutdown.sh"))
    os.system("kill -9 $(ps -ef | grep java| awk '{print $2}')")
    time.sleep(5)
    try:
        tel = telnetlib.Telnet(host, port)
        print("[-] close tomcat service failed, please close manually.")
        sys.exit()
    except:
        print("[-] close tomcat service successful.")


def startup(tomcat_path):
    """
        start up tomcat service
        :param tomcat_path: tomcat home
    """
    print("[-] tomcat service is starting now.")
    os.system(os.path.join(tomcat_path, "bin/startup.sh"))
    time.sleep(3)
    rizhi = open(os.path.join(tomcat_path, "logs/catalina.out"), 'r')
    try:
        telnet = telnetlib.Telnet(host, port)
        xinxi = rizhi.read()
        xinxi.index("Server startup in")
        time.sleep(6)
        print("[-] start tomcat service successful.")
        rizhi.close()
    except:
        print("[-] start tomcat service failed, please start manually.")
        rizhi.close()


def operate(code_path, jenkins_home, tomcat_home):
    """
    operate function
        :param code_path: the code path of jenkins plugin 
        :param jenkins_home: the path of jenkins home
        :param tomcat_home: the path of tomcat home
    """
    if not os.path.exists(code_path) or not os.path.isdir(code_path):
        raise OSError(code_path + ' not exists or valid path.')
    print('[+] cd ' + code_path + ' && mvn -U clean package')
    external_cmd('cd ' + code_path + ' && mvn -U clean package')
    plugin_path = os.path.join(code_path, 'target', os.path.basename(code_path) + '.hpi')
    if not os.path.exists(plugin_path):
        raise OSError('generate plugin error. path: ' + plugin_path)
    if not os.path.exists(tomcat_home) or not os.path.isdir(tomcat_home):
        raise OSError('invalid tomcat home path. path: ' + tomcat_home)
    print('[+] cd ' + os.path.join(tomcat_home, 'bin') + ' && ./shutdown.sh')
    shutdown(tomcat_home)
    if os.path.exists(jenkins_home):
        jenkins_plugin_home = os.path.join(jenkins_home, 'plugins')
        if os.path.exists(jenkins_plugin_home):
            plugin_name = os.path.basename(plugin_path).split('.')[0]
            this_plugin_dir_path = os.path.join(jenkins_plugin_home, plugin_name)
            if os.path.exists(this_plugin_dir_path):
                print('[+] rm -rf ' + this_plugin_dir_path)
                external_cmd('rm -rf ' + this_plugin_dir_path)
            this_plugin_file_path = os.path.join(jenkins_plugin_home, plugin_name + '.hpi')
            if os.path.exists(this_plugin_file_path):
                print('[+] rm ' + this_plugin_file_path)
                external_cmd('rm ' + this_plugin_file_path)
            print('[+] cp ' + plugin_path + '  ' + jenkins_plugin_home)
            external_cmd('cp ' + plugin_path + ' ' + jenkins_plugin_home)
            print('[+] cd ' + os.path.join(tomcat_home, 'bin') + ' && ./startup.sh')
            startup(tomcat_home)


if __name__ == '__main__':
    code_path = '/Users/chenmiao/Documents/github/helloplugin'
    jenkins_home = '/Users/chenmiao/.jenkins/'
    tomcat_home = '/Users/chenmiao/Library/apache-tomcat'

    p = argparse.ArgumentParser(description='generate jenkins plugin and move it at jenkins home.', 
        usage='need some path configuration, including plugin code home, jenkins home and tomcat home.')
    p.add_argument('-c', default=code_path, dest='code_home_path', help='the code path of plugin home.', type=str)
    p.add_argument('-j', default=jenkins_home, dest='jenkins_home_path', help='the path of jenkins home.', type=str)
    p.add_argument('-t', default=tomcat_home, dest='tomcat_home_path', help='the path of tomcat home.', type=str)
    args = p.parse_args()
    operate(args.code_home_path, args.jenkins_home_path, args.tomcat_home_path)

#!/usr/bin/env Python3
import socket

'''Get Local Machine Info'''
def print_machine_info():
    host_name = socket.gethostname()
    host_ip_address = socket.gethostbyname(host_name)
    print("Host Name is: " + host_name)
    print("Host IP Address is: " + socket.gethostbyname(host_name))

'''Get Remote Machine Info'''
def get_remote_machine_info():
    remote_host = 'www.baidu.com'
    try:
        print(remote_host + " IP Address: " + socket.gethostbyname(remote_host))
    except socket.error as err_msg:
        print(remote_host + " error message is: " + err_msg)

if __name__ == '__main__':
    print_machine_info()
    print(help(socket.gethostname))

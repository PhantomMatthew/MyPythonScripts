#!/usr/bin/env Python3
import socket
from binascii import hexlify


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

ip_addrs = ['127.0.0.1', '192.168.199.204']

def convert_ip4_address():
    for ip_addr in ip_addrs:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        #print("IP Address: " + ip_addr + " => Packed: " + hexlify(packed_ip_addr) + ", Unpacked: " + unpacked_ip_addr)
        print("IP Address: %s => Packed: %s, Unpacked: %s" % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))


if __name__ == '__main__':
    print_machine_info()
    print(help(socket.gethostname))
    get_remote_machine_info()
    convert_ip4_address()
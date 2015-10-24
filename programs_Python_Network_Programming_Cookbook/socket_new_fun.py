#!/usr/bin/python
import socket

def print_machine_info():
    host = socket.gethostname()
    ip_address = socket.gethostbyname("www.google.com")
    print host
    print ip_address


if __name__ == '__main__':
    print_machine_info()





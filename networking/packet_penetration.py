#!/usr/bin/python
#Packet sniffer in python
#For Linux
# added a new line in master for testing 
# test from remote server

import socket

#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
 
# receive a packet and display it
while True:
 print s.recvfrom(65565)

# adding few more comments



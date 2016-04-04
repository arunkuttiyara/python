#!/usr/bin/python
#Packet sniffer in python
#For Linux
# 4 Apr 2016, 6:55

import socket

# added a new line
#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
 
# receive a packet and display it
while True:
 print s.recvfrom(65565)

# adding few more comments



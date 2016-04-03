#!/usr/bin/python
#Packet sniffer in python
#For Linux

import socket

# added a new line
#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
 
# receive a packet and display it
while True:
 print s.recvfrom(65565)




#!/usr/bin/python


import smtplib, email, sys, time, os

print "starting the program"

emailid = "arunkuttiyara@gmail.com"
password = "KUTTIYARa7731"

smtpHost = "smtp.gmail.com"
port = 587

try:
    print "test ..... 0"
    server = smtplib.SMTP(smtpHost,port)
    print "test ..... 1"
    server.ehlo()
    print "test ..... 2"
    server.starttls()
    print "test ..... 3"
    server.ehlo()
    print "test ..... 4"
    server.login(emailid,password)
    print "login successful 5\n"
    
except:
    print "login unsuccessful ***** \n"
    pass

print "completed \n"



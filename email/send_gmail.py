#!/usr/bin/python
	
def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
   
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    
    except:
        print "failed to send mail"

if __name__ == '__main__':
    print "starting sending mail"
    send_email("arunkuttiyara@gmail.com","password","arunkuttiyara@yahoo.com","test","test_BODY")
    print "sending mail : done "





#   try:
#       server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#       server_ssl.ehlo()
#        #server.starttls()
#        server_ssl.login(gmail_user, gmail_pwd)
#        server_ssl.sendmail(FROM, TO, message)
#        server_ssl.close()
#        print 'successfully sent the mail'
#    except:
#        print "failed to send mail"

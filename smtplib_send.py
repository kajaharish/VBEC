#!/usr/bin/python

import smtplib

sender = 'helmetmail05@gmail.com'
receivers = 'abhisheksinghchaudhary77@gmail.com' #bcc
message = """From: Harish Kaja
To: {}
Subject: SMTP e-mail test

This is a test e-mail message.
""".format(receivers)

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com',587)
   smtpObj.starttls()
   smtpObj.login("helmetmail05@gmail.com", "qwerty@123")
   smtpObj.sendmail(sender,receivers, message)
   print ("Successfully sent email to",receivers)
except SMTPException:
   print ("Error: unable to send email")

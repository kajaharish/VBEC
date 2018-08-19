#!/usr/bin/python

import smtplib

import first


class Send:

   def sendMail(self,receiverId,subject,body):
       sender = 'helmetmail05@gmail.com'
       message = """From: {}
To: {}
Subject: {}
       
{}
""".format(obj2.fetchCredential()[2],receiverId,subject,body)

       try:
           smtpObj = smtplib.SMTP('smtp.gmail.com',587)
           smtpObj.starttls()
           smtpObj.login(obj2.fetchCredential()[0], obj2.fetchCredential()[1])
           smtpObj.sendmail(sender,receiverId, message)
           return ("Successfully sent email to",receiverId)
       except smtplib.SMTPException:
           return ("Error: unable to send email")
       except TypeError:
           return ("No credentials have been provided")

obj2 = first.Menu()
# obj4 = Send()
# obj4.sendMail("helmetmail05@gmail.com","Drag","body")
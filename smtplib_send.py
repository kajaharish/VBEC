#!/usr/bin/python

import smtplib

class Send:

   def sendMail(self,receiverId,subject,body):
       sender = 'helmetmail05@gmail.com'
       message = """From: Harish Kaja
To: {}
Subject: {}
       
{}
""".format(receiverId,subject,body)

       try:
          smtpObj = smtplib.SMTP('smtp.gmail.com',587)
          smtpObj.starttls()
          smtpObj.login("helmetmail05@gmail.com", "qwerty@123")
          smtpObj.sendmail(sender,receiverId, message)
          print("Successfully sent email to",receiverId)
       except smtplib.SMTPException:
          print("Error: unable to send email")
#obj4 = Send()
#Send().sendMail()
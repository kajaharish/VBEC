import smtplib
from email.mime.text import MIMEText

class Send:

    def send_mails(self):

        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465
        username = ''
        password = ''
        sender = ''
        receivers = ['', '']

        msg = MIMEText('Hi, how are you today?')
        msg['Subject'] = 'Hello'
        msg['From'] = sender
        msg['To'] = ', '.join(receivers)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, receivers, msg.as_string())
        server.quit()


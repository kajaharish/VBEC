import imaplib

import mailparser

import first


class Body:

    def fetchBody(self,id):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(obj11.fetchCredential()[0], obj11.fetchCredential()[1])
        mail.list()
        mail.select("inbox")

        result, data = mail.search(None, "ALL")

        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[id]

        result, data = mail.fetch(latest_email_id, "(RFC822)")  # fetch the email body (RFC822) for the given ID

        raw_email = data[0][1]  # here's the body, which is raw text of the whole email

        mail5 = mailparser.parse_from_bytes(raw_email)

        body = str(mail5.body.split("--- mail_boundary ---")[0])
        return body

obj11 = first.Menu()
# obj10 = Body()
# obj10.fetchBody(-3)

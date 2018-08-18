import imaplib

import mailparser

import first


class Inbox:

    def fetchAll(self):
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login('helmetmail05@gmail.com', 'qwerty@123')
            mail.list()
            mail.select("inbox")  # connect to inbox.

            result, data = mail.search(None, "ALL")

            ids = data[0]  # data is a list.
            id_list = ids.split()  # ids is a space separated string
            i = 1

            for x in reversed(range(-10,0)):

                latest_email_id = id_list[x]  # get the latest

                result, data = mail.fetch(latest_email_id, "(RFC822)")  # fetch the email body (RFC822) for the given ID

                raw_email = data[0][1]  # here's the body, which is raw text of the whole email
                mail5 = mailparser.parse_from_bytes(raw_email)

                # print(mail5.body)
                for name in mail5.from_:
                    self.audioString = str(str(i)+ ". Name is "+ name[0]+ ". Mail ID is"+ name[1]+ ", Subject, is, "+ mail5.subject)
                    obj7.textToSpeech(self.audioString)
                    i += 1

        except IndexError:
            obj7.textToSpeech("\nNo more messages")

        except imaplib.IMAP4.error:
            obj7.textToSpeech("Authentication Error! please check your credentials")




obj6 = Inbox()
obj7 = first.Menu()
obj6.fetchAll()
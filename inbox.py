import imaplib
import sys

import mailparser

import first


class Inbox:
    lower = -4
    upper = 0

    def fetchAll(self,lower,upper):
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login('helmetmail05@gmail.com', 'qwerty@123')
            mail.list()
            mail.select("inbox")  # connect to inbox.

            result, data = mail.search(None, "ALL")

            ids = data[0]  # data is a list.
            id_list = ids.split()  # ids is a space separated string
            i = 1

            for x in reversed(range(lower,upper)):

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
            #self.outcome = False
            sys.exit()

        except imaplib.IMAP4.error:
            obj7.textToSpeech("Authentication Error! please check your credentials")

    def fetchInbox(self):
        self.fetchAll(Inbox.lower,Inbox.upper)
        obj7.textToSpeech("Do you want to read more messages ?")
        if obj7.hear() in ["yes"]:
            Inbox.lower -= 5
            Inbox.upper -= 5
            self.fetchInbox()




obj6 = Inbox()
obj7 = first.Menu()

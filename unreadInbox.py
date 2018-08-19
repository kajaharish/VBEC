import imaplib
import sys

import mailparser

import FetchBody
import first


class Unread:
    lower = -4
    upper = 0

    def fetchUnread(self,lower,upper):
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login(obj8.fetchCredential()[0], obj8.fetchCredential()[1])
            mail.list()
            mail.select("inbox")  # connect to inbox.

            result, data = mail.search(None, '(UNSEEN)')

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
                    self.audioString = str(str(i)+ ". Name is "+ name[0]+ ". Mail ID is"+ name[1]+ ", Subject, is, "+ mail5.subject )
                    obj8.textToSpeech(self.audioString)
                    obj8.textToSpeech("Do you want to read the body of this message?")
                    if obj8.hear() in ["yes", "ya", "yeah"]:
                        obj8.textToSpeech(obj10.fetchBody(x))
                    mail.store(latest_email_id, '-FLAGS', '\\Seen')
                    i += 1

        except IndexError:
            obj8.textToSpeech("\nNo new messages")
            #self.outcome = False
            sys.exit()

        except imaplib.IMAP4.error:
            obj8.textToSpeech("Authentication Error! please check your credentials")

    def fetch(self):
        self.fetchUnread(Unread.lower, Unread.upper)
        obj8.textToSpeech("Do you want to read more messages ?")
        if obj8.hear() in ["yes"]:
            Unread.lower -= 5
            Unread.upper -= 4
            self.fetch()

obj9 = Unread()
obj8 = first.Menu()
obj10 = FetchBody.Body()
# obj9.fetch()

import imaplib
import sys

import mailparser

import FetchBody
import first


class Inbox:
    lower = -4
    upper = 0

    def fetchAll(self,lower,upper):
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login(obj7.fetchCredential()[0], obj7.fetchCredential()[1])
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
                    self.audioString = str(str(i)+ ". Name is "+ name[0]+ ". Mail ID is"+ name[1]+ ", Subject, is, "+ mail5.subject )
                    obj7.textToSpeech(self.audioString)
                    obj7.textToSpeech("Do you want to read the body of this message?")
                    if obj7.hear() in ["yes", "ya", "yeah"]:
                        obj7.textToSpeech(obj8.fetchBody(x))
                    i += 1

        except IndexError:
            obj7.textToSpeech("\nNo more messages")
            #self.outcome = False
            sys.exit()

        except imaplib.IMAP4.error:
            obj7.textToSpeech("Authentication Error! please check your credentials")

        except TypeError:
            return ("No credentials have been provided")

    def fetchInbox(self):
        self.fetchAll(Inbox.lower,Inbox.upper)
        obj7.textToSpeech("Do you want to read more messages ?")
        if obj7.hear() in ["yes"]:
            Inbox.lower -= 5
            Inbox.upper -= 4
            self.fetchInbox()




obj6 = Inbox()
obj7 = first.Menu()
obj8 = FetchBody.Body()
# obj6.fetchInbox()

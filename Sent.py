import imaplib

import mailparser

import first


class SentBox:
    lower = -4
    upper = 0

    def fetchAll(self,lower,upper):
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login(obj7.fetchCredential()[0], obj7.fetchCredential()[1])
            mail.list()
            mail.select('"[Gmail]/Sent Mail"')  # connect to inbox.

            result, data = mail.search(None, "ALL")

            ids = data[0]  # data is a list.
            id_list = ids.split()  # ids is a space separated string
            i = 1

            for x in reversed(range(lower,upper)):

                latest_email_id = id_list[x]  # get the latest

                result, data = mail.fetch(latest_email_id, "(RFC822)")  # fetch the email body (RFC822) for the given ID

                raw_email = data[0][1]  # here's the body, which is raw text of the whole email
                mail5 = mailparser.parse_from_bytes(raw_email)
                for name in mail5.from_:
                    self.audioString = str(str(i)+ ". receiver's E-Mail ID is "+ mail5.to[0][1]+ ", Subject, is, "+ mail5.subject )
                    obj7.textToSpeech(self.audioString)
                    obj7.textToSpeech("Do you want to read the body of this message?")
                    if obj7.hear() in ["yes", "ya", "yeah"]:
                        obj7.textToSpeech(str(mail5.body.split("--- mail_boundary ---")[0]))

                    i += 1

        except IndexError:
            obj7.textToSpeech("\nNo more messages")
            #self.outcome = False
            return False

        except imaplib.IMAP4.error:
            obj7.textToSpeech("Authentication Error! please check your credentials")
            return False

        except TypeError:
            obj7.textToSpeech("No credentials have been provided")
            return False

    def fetchSentBox(self):
        if self.fetchAll(SentBox.lower,SentBox.upper) == True:
            obj7.textToSpeech("Do you want to read more messages ?")
            if obj7.hear() in ["yes"]:
                SentBox.lower -= 5
                SentBox.upper -= 4
                self.fetchSentBox()
        else:
            return



obj6 = SentBox()
obj7 = first.Menu()


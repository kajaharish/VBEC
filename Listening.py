import speech_recognition as sr

import FetchBody
import contacts
import first
import inbox
import smtplib_send
import unreadInbox


class Listen:
    r = sr.Recognizer()
    def repeatName(self):
        obj3.textToSpeech("Speak the receiver name")
        self.nameId = obj3.hear()
        self.Id = obj5.fetch(self.nameId)
        if self.Id is None:
            obj2.repeatName()
        else:
            return self.Id

    def repeatSubject(self):
        obj3.textToSpeech("Speak the Subject")
        self.subject = obj3.hear()
        return self.subject

    def repeatBody(self):
        obj3.textToSpeech("Speak the Content of body")
        self.body = obj3.hear()
        return self.body

    def changes(self):
        obj3.textToSpeech("do you wish to make some changes in name, subject, body? If yes then please say the header name or else say NO!")
        self.change = obj3.hear()
        if self.change in ["name"]:
            obj2.repeatName()
            obj2.changes()
        elif self.change in ["subject"]:
            obj2.repeatSubject()
            obj2.changes()
        elif self.change in ["body"]:
            obj2.repeatBody()
            obj2.changes()
        else:
            return True

    def process(self):
        obj3.mainMenu()
        obj3.hear()
        if obj3.command in ["1","one","compose a mail","send a mail", "send mail", "compose an email", "compose email"]:
            obj2.repeatName()
            obj2.repeatSubject()
            obj2.repeatBody()
            obj2.changes()
            obj3.textToSpeech(obj4.sendMail(self.Id, self.subject, self.body))
            obj2.process()


        elif obj3.command in ["2","two", "to","list new messages","read new messages","list unread messages" ]:
            obj9.fetch()
            obj2.process()


        elif obj3.command in ["3", "tree", "three", "check new mails", "new mails", "is there any new mail"]:
            obj6.fetchInbox()
            obj2.process()

        elif obj3.command in ["4","four","check sent mails","go to sentbox","go to sent box"]:
            print("done4")

        elif obj3.command in ["5","five","add credentials","save credentials","","check sent mails","check sent box" ]:
            obj3.addCredential()
            obj2.process()

        elif obj3.command in ["6","six","show current mail id"]:
            obj3.textToSpeech(obj3.fetchCredential()[0])
            print(obj3.fetchCredential()[0])
            obj2.process()

        elif obj3.command in ["7","seven","add another contact","add a contact","save another contact","save a contact"]:
            obj5.save()
            obj2.process()

        elif obj3.command in ["8","eight","delete Contact","delete a contact","remove a contact" ]:
            self.erase = str(input("Enter the name of the contact details you wish to erase:"))
            obj5.delete(self.erase)
            obj2.process()

        elif obj3.command in ["9", "nine", "show all contacts", "show contacts", "list all contacts", "compose an email","compose email"]:
            obj5.show()
            obj2.process()

        else:
            obj3.textToSpeech("No such cammand")
        return

obj2 = Listen()
obj3 = first.Menu()
obj4 = smtplib_send.Send()
obj5 = contacts.Contact()
obj6 = inbox.Inbox()
obj9 = unreadInbox.Unread()
obj10 = FetchBody.Body()


#obj3.mainMenu()
#obj3.textToSpeech("Issue a command")
#obj3.welcome()
obj2.process()

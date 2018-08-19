import speech_recognition as sr

import FetchBody
import contacts
import first
import inbox
import smtplib_send

r = sr.Recognizer()
class Listen:

    # def hear(self):
    #     with sr.Microphone() as source:
    #         #self.speak("Ready...")
    #         r.pause_threshold = 0.5
    #         r.adjust_for_ambient_noise(source, duration=1)
    #         audio = r.listen(source)
    #         self.speechToText(audio)
    #     return self.command
    #
    # def speechToText(self,audio):
    #     try:
    #         self.command = r.recognize_google(audio).lower()
    #         obj3.textToSpeech('You said: ' + self.command + '\n')
    #         print(self.command)
    #         #self.process(self.command)
    #         return self.command
    #
    #     except sr.UnknownValueError:
    #         obj3.textToSpeech('Your last command couldn\'t be heard')
    #         self.command = self.hear()

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
        obj3.hear()
        if obj3.command in ["1","one","compose a mail","send a mail", "send mail", "compose an email", "compose email"]:
            obj2.repeatName()
            obj2.repeatSubject()
            obj2.repeatBody()
            obj2.changes()
            obj4.sendMail(self.Id, self.subject, self.body)

        elif obj3.command in ["2","two", "to","list new messages","read new messages","list unread messages" ]:
            #obj5.fetch()

            #obj3.textToSpeech(obj10.fetchBody(-1))
            pass

        elif obj3.command in ["3", "tree", "three", "check new mails", "new mails", "is there any new mail"]:
            obj6.fetchInbox()

        elif obj3.command in ["4","four","Check read emails","check read emails","go to read emails","go to readmails"]:
            print("done4")

        elif obj3.command in ["5","five","go to sent box","open sent box","","check sent mails","check sent box" ]:
            print("done5")

        elif obj3.command in ["6","six","compose a mail","send a mail","send mail","compose an email","compose email" ]:
            print("done5")
        elif obj3.command in ["7","seven","add another contact","add a contact","save another contact","save a contact"]:
            obj5.save()

        elif obj3.command in ["8","eight","compose a mail","send a mail","send mail","compose an email","compose email" ]:
            self.erase = str(input("Enter the name of the contact details you wish to erase:"))
            obj5.delete(self.erase)

        elif obj3.command in ["9", "nine", "show all contacts", "show contacts", "list all contacts", "compose an email","compose email"]:
            obj5.show()

        else:
            obj3.textToSpeech("No such cammand")
        return

obj2 = Listen()
obj3 = first.Menu()
obj4 = smtplib_send.Send()
obj5 = contacts.Contact()
obj6 = inbox.Inbox()
obj10 = FetchBody.Body()
#obj4.sendMail("kajaharish.4hud@gmail.com","hello","kya chlar ra")

#obj3.mainMenu()
#obj3.textToSpeech("Issue a command")
obj2.process()

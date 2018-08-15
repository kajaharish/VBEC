import speech_recognition as sr

import first
import smtplib_send

r = sr.Recognizer()
class Listen:

    def hear(self):
        with sr.Microphone() as source:
            #self.speak("Ready...")
            r.pause_threshold = 0.5
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            self.speechToText(audio)
        return self.command

    def speechToText(self,audio):
        try:
            self.command = r.recognize_google(audio).lower()
            obj3.textToSpeech('You said: ' + self.command + '\n')
            print(self.command)
            #self.process(self.command)
            return self.command

        except sr.UnknownValueError:
            obj3.textToSpeech('Your last command couldn\'t be heard')
            self.command = self.hear()



    def process(self):
        self.hear()
        if self.command in ["1","one","compose a mail","send a mail","send mail","compose an email","compose email" ]:
            obj3.textToSpeech("Speak the receiver Mail ID")
            self.receiverId = self.hear()
            self.Id = self.receiverId.replace(" ","")
            print(self.Id)


            obj3.textToSpeech("Speak the Subject")
            self.subject = self.hear()
            obj3.textToSpeech("Speak the Content of body")
            self.body = self.hear()
            obj4.sendMail(self.receiverId,self.subject,self.body)

        elif self.command in ["2","two","open inbox","check inbox","go to inbox","inbox" ]:
            print("done2")
        elif self.command in ["3","three","check new mails","new mails","is there any new mail"]:
            print("done3")
        elif self.command in ["4","four","Check read emails","check read emails","go to read emails","go to readmails"]:
            print("done4")
        elif self.command in ["5","five","go to sent box","open sent box","","check sent mails","check sent box" ]:
            print("done5")
        elif self.command in ["6","six","compose a mail","send a mail","send mail","compose an email","compose email" ]:
            print("done6")
        else:
            obj3.textToSpeech("No such cammand")
        return

obj2 = Listen()
obj3 = first.Menu()
obj4 = smtplib_send.Send()
obj4.sendMail("kajaharish.4hud@gmail.com","hello","kya chlar ra")
#obj3.mainMenu()
#obj3.textToSpeech("Issue a command")
obj2.process()

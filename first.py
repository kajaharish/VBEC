import os

import speech_recognition as sr
from gtts import gTTS

r = sr.Recognizer()
class Menu:

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
            self.textToSpeech('You said: ' + self.command + '\n')
            print(self.command)
            #self.process(self.command)
            return self.command

        except sr.UnknownValueError:
            self.textToSpeech('Your last command couldn\'t be heard')
            self.command = self.hear()

    def textToSpeech(self,audioString):
        self.tts = gTTS(text = audioString, lang = "en")
        self.fileName = "audio.mp3"
        self.tts.save(self.fileName)
        os.system("mpg321 audio.mp3")
        os.remove("audio.mp3")
        return


    def mainMenu(self):
        self.textToSpeech("""Hi, Welcome to Talkmail.        
        Please Select a desired option:
        1. Compose a Mail, 2. Go to Inbox, 3. Check New Mails, 4. Check read Mails, 5. Goto Sent Mails, 6. Go to Draft, 7. Add Contact, 8. Delete Contact,
        9. show all contacts
        
        """)
        return


#obj1 = Menu()
#obj1.mainMenu()
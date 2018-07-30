import speech_recognition as sr
from gtts import gTTS
import time
import os

class main:


    def speak(self, audioString):
        print(audioString)
        self.tts = gTTS(text = audioString, lang = 'en')
        self.filename = "audio.mp3"
        self.tts.save(self.filename)
        os.system("mpg321 audio.mp3")
        #os.remove(self.filename)

    def menu(self):
        self.options = ["1. Compose Mail", "2. Inbox", "3. Receive New Mails", "4. Goto Sent Mails"]
        self.speak("Speak the desired number for what you want to do.")
        for choice in self.options:
            self.speak(choice)

#initialization
#time.sleep(2)
spk = main()
spk.speak("Hello, Welcome to TalkMail.")
spk.menu()
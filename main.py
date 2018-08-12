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
        os.remove(self.filename)

    def menu(self):
        self.options = ["1. Compose Mail", "2. Inbox", "3. Receive New Mails", "4. Goto Sent Mails"]
        self.speak("Speak the desired number for what you want to do.")
        for choice in self.options:
            self.speak(choice)

        self.listenTome()

    def listenTome(self):
        "listens for commands"

        r = sr.Recognizer()

        with sr.Microphone() as source:
            #self.speak("Ready...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            self.command = r.recognize_google(audio).lower()
            self.speak('You said: ' + self.command + '\n')
            #self.confirm()

        # loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            print('Your last command couldn\'t be heard')
            self.command = self.listenTome()

        return self.command


    def confirm(self):

        confir = sr.Recognizer()

        with sr.Microphone() as source:
            confir.pause_threshold = 1
            confir.adjust_for_ambient_noise(source, duration=1)
            confir_audio = confir.listen(source)

        try:
            self.speak("Say Yes to confirm, or No to try again.")
            self.confirmation = confir.recognize_google(confir_audio).lower()
            self.task()

        except sr.UnknownValueError:
            self.speak('Your last command couldn\'t be heard')
            self.confirmation = self.confirm()

        return self.confirmation()


    def task(self):
        if "Yes" in self.confirmation:
            print("Selected option is" + self.command)
        elif "No" in self.confirmation:
            self.speak("Ready...")
            self.listenTome()

#initialization
#time.sleep(2)
#spk = main()
#spk.speak("Hello, Welcome to TalkMail.")
#spk.menu()
test = main()
test.listenTome()
test.confirm()
#test.speak("Hello")
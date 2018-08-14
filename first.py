from gtts import gTTS
import os

class Menu:

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
        1. Compose a Mail, 2. Go to Inbox, 3. Check New Mails, 4. Check read Mails, 5. Goto Sent Mails, 6. Go to Draft
        """)
        return


#obj1 = Menu()
#obj1.mainMenu()
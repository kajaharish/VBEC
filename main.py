import speech_recognition as sr
from gtts import gTTS
import time
import os


def speak(audioString):
    print(audioString)
    tts = gTTS(text = audioString, lang = 'en')
    filename = "audio.mp3"
    tts.save(filename)
    os.system("mpg321 audio.mp3")
    os.remove(filename)

def mainMenu():
    mainMenu = ["1. Login", "2. Sign Up"]
    speak("What do you want to do?")
    speak("Speak the desired number for choice.")
    for line in mainMenu:
        speak(line)


def subMenu():
    subMenu = ["1. Compose Mail", "2. Inbox", "3. Receive New Mails", "4. Goto Sent Mails"]
    speak("Speak the desired number for choice.")
    for line in subMenu():
        speak(line)

#initialization
#time.sleep(2)
speak("Hello, Welcome to Voice Based Mail Client")
mainMenu()
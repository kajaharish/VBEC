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

"""
def getCredentials():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

speak("Kindly speak your credenials as asked and wait for the next:")
speak("Speak your password:")
"""

def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        speak('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        speak("Your last command couldn\'t be heard")
        command = myCommand()

    return command

myCommand()
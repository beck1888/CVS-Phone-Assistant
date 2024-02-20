import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[113].id)
    engine.say(text)
    engine.runAndWait()
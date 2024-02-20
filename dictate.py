import speech_recognition as sr

def dictate():
    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    user_said = r.recognize_google(audio)

    return str(user_said)
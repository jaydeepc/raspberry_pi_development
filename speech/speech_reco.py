import speech_recognition as sr
import pyttsx


engine = pyttsx.init()
engine.setProperty('rate', 70)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[15].id)

r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    print "Listening....."
    audio = r.listen(source)                  # listen for the first phrase and extract it into audio data

try:
    engine.say(r.recognize(audio))    # recognize speech using Google Speech Recognition
    engine.runAndWait()
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
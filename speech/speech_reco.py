import speech_recognition as sr
import pyaudio


r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    print "Listening....."
    audio = r.listen(source)                  # listen for the first phrase and extract it into audio data

try:
    print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
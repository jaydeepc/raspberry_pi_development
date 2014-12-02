import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 70)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[24].id)
engine.say("Saanvi")

engine.runAndWait()
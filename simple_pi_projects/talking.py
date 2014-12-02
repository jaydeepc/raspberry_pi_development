import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 70)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[14].id)
engine.say("Saanvi is having hickups")

engine.runAndWait()
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 150)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say("Hello Sir. My name is Pi.")
engine.runAndWait()
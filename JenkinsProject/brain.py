import speech_recognition as sr
import pyttsx
import datetime

engine = pyttsx.init()
engine.setProperty('rate', 150)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[15].id)

user_command = ""
WORDS = {
    "hi": "Hello, Sir",
    "build": "Sure Sir, just give me a second.",
    "goodbye": "Good bye, sir. Let me know when you need me",
    "what is the time now": datetime.datetime.now().strftime('%I:%M%p').lstrip('0')
}

while user_command is "":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print "Listening....."
        audio = r.listen(source)

    try:
        user_command = r.recognize(audio)
        print "You said: {0}".format(user_command)

    except LookupError:
        print("Could not understand audio")

    if user_command.lower() in WORDS.keys():
        engine.say(WORDS.get(user_command))
    else:
        engine.say("Sorry sir, I can not understand you!")

    engine.runAndWait()
    user_command = "" if user_command <> "goodbye" else user_command
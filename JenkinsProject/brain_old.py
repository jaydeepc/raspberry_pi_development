import speech_recognition as sr
import datetime
from subprocess import call

user_command = ""


def introduce():
    return "Hello. My name is Root. I am currently working as a QA helper."


WORDS = {
    "root": "Yes, Sir?",
    "build": "Sure Sir, just give me a second.",
    "goodbye": "Good bye, sir. Let me know when you need me",
    "what is the time now": datetime.datetime.now().strftime('%I:%M%p').lstrip('0'),
    "who is saanvi": "Sir, your daughter's name is Saanvi.",
    "who are you": introduce()
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
        call(["mpg123", "http://www.translate.google.com/translate_tts?tl=en&q={0}&key=AIzaSyDkKEm081DUEZFXiW1pFx6gN1JHNqg1qus&".format(WORDS.get(user_command).replace(" ", "%20"))])
    else:
        call(["mpg123", "http://www.translate.google.com/translate_tts?tl=en&q={0}&key=AIzaSyDkKEm081DUEZFXiW1pFx6gN1JHNqg1qus&".format("Sorry sir, I can not understand you!").replace(" ", "%20")])

    user_command = "" if user_command <> "goodbye" else user_command



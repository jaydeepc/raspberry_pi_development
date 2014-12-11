import requests
from subprocess import call
import datetime

host = "http://www.translate.google.com/translate_tts?tl=en"

WORDS = {
    "root": "Yes, Sir?",
    "build": "Sure Sir, just give me a second.",
    "goodbye": "Good bye, sir. Let me know when you need me",
    "what is the time now": datetime.datetime.now().strftime('%I:%M%p').lstrip('0'),
    "who are you": "Hello. My name is Root. I am currently working as a QA helper"
}
word = ""
while word is "":
    try:
        word = raw_input("What you want me to say:")
    except LookupError:
        print "No Command"

    if word.lower() in WORDS.keys():
        call(["mpg123", "http://www.translate.google.com/translate_tts?tl=en&q={0}&key=AIzaSyDkKEm081DUEZFXiW1pFx6gN1JHNqg1qus&".format(WORDS.get(word))])
    else:
        call(["say", "Sorry sir, I can not understand you!"])

    word = "" if word <> "goodbye" else word





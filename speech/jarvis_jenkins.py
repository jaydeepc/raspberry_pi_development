import speech_recognition as sr
from jenkinsapi.jenkins import Jenkins


user_command = ""
r = sr.Recognizer()
with sr.Microphone() as source:
    print "Listening....."
    audio = r.listen(source)

try:
    print("You said " + r.recognize(audio))
    user_command = r.recognize(audio)

except LookupError:
    print("Could not understand audio")


jenkins_instance = Jenkins('http://65.50.13.61:8080')

jenkins_instance.build_job(user_command)

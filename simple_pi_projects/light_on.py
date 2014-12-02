import RPi.GPIO as GPIO, feedparser
import time
import pyttsx

engine = pyttsx.init()
engine.setProperty('rate', 70)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[14].id)

USERNAME="jaydeepc@thoughtworks.com"
PASSWORD="Password@w00m"

led_green = 12
GPIO_PIN=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

url_str = "https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom"
print url_str
while True:
        newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
        if newmails > 1:
                GPIO.output(led_green, GPIO.HIGH)
		GPIO.output(GPIO_PIN, GPIO.LOW)
                engine.say("You Got Mail!")
		engine.runAndWait()
        else:
                GPIO.output(GPIO_PIN, GPIO.LOW)
		GPIO.output(led_green, GPIO.LOW)

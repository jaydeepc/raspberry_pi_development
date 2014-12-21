import Mobility as move
from subprocess import check_output, call

call(["mpg123", "http://www.translate.google.com/translate_tts?tl=en&q={0}&key=AIzaSyDkKEm081DUEZFXiW1pFx6gN1JHNqg1qus&".format("For how long sir?".replace(" ", "%20"))])
length = check_output(["speech-recog.sh"])

move.init()
move.go_forward(int(length))
move.kill()
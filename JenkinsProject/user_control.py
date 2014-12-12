import Mobility as move

key_press = ""
while key_press is not "t":
    key_press = raw_input()
    if key_press.lower() == 'w':
        move.init()
        move.go_forward(0)
        move.kill()
    elif key_press.lower() == 's':
        move.init()
        move.go_backward(0)
        move.kill()

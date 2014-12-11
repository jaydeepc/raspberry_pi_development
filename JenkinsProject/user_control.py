import Mobility as move
import Tkinter as tk


def key_input(event):
    move.init()
    print 'Key:', event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        move.go_forward(sleep_time)
    elif key_press.lower() == 's':
        move.go_backward(sleep_time)


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
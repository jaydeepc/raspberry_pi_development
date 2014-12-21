import Mobility as move
import time

sides = input("How many sides?")
size = input("How big?")
full_turn = .97*4

for x in range(0, sides):
    move.init()
    move.go_forward(size)
    time.sleep(.5)
    move.turn_right(full_turn/sides)
    move.kill()
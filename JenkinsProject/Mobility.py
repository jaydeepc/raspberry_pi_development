import RPi.GPIO as gpio
import time


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)


def kill():
    gpio.cleanup()


def go_forward(tf):
    # init()
    gpio.output(7, True)
    gpio.output(13, True)
    time.sleep(tf)
    # gpio.output(7, False)
    # gpio.output(13, False)
    # kill()


def go_backward(tf):
    # init()
    gpio.output(11, True)
    gpio.output(15, True)
    time.sleep(tf)
    # gpio.output(11, False)
    # gpio.output(15, False)
    # kill()


def turn_right(tf):
    # init()
    gpio.output(7, True)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.output(7, False)
    gpio.output(15, False)
    # kill()


def turn_left(tf):
    # init()
    gpio.output(13, True)
    gpio.output(11, True)
    time.sleep(tf)
    gpio.output(13, False)
    gpio.output(11, False)
    time.sleep(tf)
    # kill()

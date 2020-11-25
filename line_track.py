import RPi.GPIO as gpio
from move import Move
import configparser
import time


config = configparser.ConfigParser()
config.read("config.ini")
move = Move(config["Move"])

# pins
L = 13
M = 19
R = 26

gpio.setmode(gpio.BCM)
gpio.setup(L, gpio.IN)
gpio.setup(M, gpio.IN)
gpio.setup(R, gpio.IN)

while True:
    if(not L):
        move.forward()
        print('forward')
    elif not R:
        move.turnRight()
        print('right')
    elif not L:
        move.turnLeft()
        print('left')

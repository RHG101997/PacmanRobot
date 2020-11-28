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
    if(not gpio.input(M)):
        # move.forward()
        print('forward')
    elif (not gpio.input(R)):
        move.turnLeft()
        print('right')
    elif (not gpio.input(L)):
        move.turnRight()
        print('left')
    elif (not gpio.input(M) and not gpio.input(R) and not gpio.input(L)):
        move.stop()
        print('end')
        break
    else:
        move.stop()
        print("stop")

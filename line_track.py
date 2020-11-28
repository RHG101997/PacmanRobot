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


time.sleep(10)
while True:
    if(not gpio.input(M)):
        move.reverse()
        print('forward')
    elif (not gpio.input(R)):
        move.turnRight()
        print('right')
    elif (not gpio.input(L)):
        move.turnLeft()
        print('left')
    elif (not(gpio.input(M) and gpio.input(R) and gpio.input(L))):
        move.stop()
        print('stop')

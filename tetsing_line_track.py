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
    time.sleep(0.2)

    print("L: " + str(not gpio.input(L)) +" M: "+ str(not gpio.input(M)) + " R: " + str(not  gpio.input(R)) +" Stop: " + str((not gpio.input(M) and not gpio.input(R) and not gpio.input(L))))
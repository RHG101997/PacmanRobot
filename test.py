from move import Move
import configparser
import time


config = configparser.ConfigParser()
config.read("config.ini")
move = Move(config["Move"])

# 1400  arounf 90 degree
move.moveBy(1000)
move.turnByRight(1400)







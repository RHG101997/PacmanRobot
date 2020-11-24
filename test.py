from move import Move
import configparser
import time


config = configparser.ConfigParser()
config.read("config.ini")
move = Move(config["Move"])

# 1400  arounf 90 degree
# move.turnByRight(1400)
move.turnLeftByTime(1)






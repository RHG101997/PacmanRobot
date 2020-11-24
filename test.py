from move import Move
import configparser
import time


config = configparser.ConfigParser()
config.read("config.ini")
move = Move(config["Move"])

# 1400  arounf 90 degree
# print("forward")
# move.moveBy(1000)
print("right")
move.turnByRight(1400)
print("done")






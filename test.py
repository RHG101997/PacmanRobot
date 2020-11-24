from move import Move
import configparser
import time


config = configparser.ConfigParser()
config.read("config.ini")
move = Move(config["Move"])

# 1400  arounf 90 degree

# print("right")
# move.turnByRight(1400)
# print("done")
# print("right")
# move.turnByLeft(1400)


# print("forward")
# move.moveBy(1000)


# print("done")


move.moveBy(3165) # feet
move.turnRightByAngle(1495)
move.moveDistance(39) # feet


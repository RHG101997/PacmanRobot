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
# move.turnByRight(1495) # 1495
# move.moveBy(4885) # fee


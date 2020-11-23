from move import Move
import configparser
import time


config = configparser.ConfigParser()
config.read("config.ini")
move = Move(config["Move"])

print("Forward")
move.forward()
time.sleep(3)
move.stop()
print("Right")
move.turnRightByTime(2)
print("Left")
move.turnLeftByTime(2)



from move import Move
import configparser
import time


config = configparser.ConfigParser()
config.read("config.ini")
move = Move(config["Move"])


# move 65 millimeters
print("Forward")
# move.moveBy(2552)
move.forward()
time.sleep(2)
move.stop()

move.turnLeftByAngle(90)





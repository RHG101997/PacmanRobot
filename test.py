from move import Move
import configparser



config = configparser.ConfigParser()
config.read("config.ini")
move = Move(config["Move"])

print("Forward")
move.forward()
print("Right")
move.turnRightByTime(2)
print("Left")
move.turnLeftByTime(2)



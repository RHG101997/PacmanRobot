import configparser
from move import Move
from vision import Vision

# Importing config
config = configparser.ConfigParser()
config.read("config.ini")

# File to handle beging
move = Move(config["Move"])
move.calibrateRobot()
colorLower = (0, 154, 156)
colorUpper = (255, 255, 255)
vs = Vision(config['Vision'],move,colorLower,colorUpper)
vs.followTarget()




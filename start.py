from move import Move
from vision import Vision

# File to handle beging
move = Move()
move.calibrateRobot()
colorLower = (0, 154, 156)
colorUpper = (255, 255, 255)
vs = Vision(move,colorLower,colorUpper)
vs.followTarget()



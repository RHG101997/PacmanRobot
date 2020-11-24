import configparser
from move import Move
from vision import Vision
from target import Target

def importHSV(config,name):
    # the values for specific target
    l_h = int(config[name]["l_h"])
    l_s = int(config[name]["l_s"])
    l_v = int(config[name]["l_v"])
    u_h = int(config[name]["u_h"])
    u_s = int(config[name]["u_s"])
    u_v = int(config[name]["u_v"])
    return (l_h,l_s,l_v),(u_h,u_s,u_v) 

# Importing config
config = configparser.ConfigParser()
config.read("config.ini")

# importing information of target
colorLower , colorUpper = importHSV(config,"Target")
# creating target
target = Target(colorLower,colorUpper)

# Setting up movement for Robot
move = Move(config["Move"])
# Calibrate(for angle turning angles)


# Setting up target and following 
vs = Vision(config['Vision'],move,target)
vs.centerTarget()




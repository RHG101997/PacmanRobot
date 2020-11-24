from move import Move
import configparser
import time


config = configparser.ConfigParser()
config.read("config.ini")
move = Move(config["Move"])


move.moveBy(2552)






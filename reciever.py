import socket
import threading
import os
from move import Move
import configparser


def action(msg,move):
    if(msg == "w"):
        print("Foward")
        move.forward()
    elif (msg == "s"):
        print("Reverse")
        move.reverse()
    elif (msg == "a"):
        print("Left")
        move.turnLeft()
    elif (msg == "d"):
        print("Right")
        move.turnRight()
    else:
        print("Stopped")
        move.stop()
     
        

# Importing config
config = configparser.ConfigParser()
config.read("config.ini")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
port  = 1235
move = Move(config["Move"])
print("Host: " + str(hostname) + "Port:" + port)


s.bind((host, port))
print("Waiting")
s.listen(3)
notDone = True

while notDone:
    conn, addr = s.accept()
    print("Connected")
    while True:
        msg = conn.recv(1024)
        if(msg.decode("utf-8") == "q"):
            notDone = False
            break
        else:
            action(msg.decode("utf-8"),move)

conn.close()
s.close()

import keyboard
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.0.0.130"
port = 1235

s.connect((host,port))

while True:  # making a loop
    try:  
        if(keyboard.is_pressed('q')):  # if key 'q' is pressed 
            s.send(bytes("q","utf-8"))
        elif (keyboard.is_pressed('w')):
            s.send(bytes("w","utf-8"))
        elif (keyboard.is_pressed('s')):
            s.send(bytes("s","utf-8"))
        elif (keyboard.is_pressed('a')):
            s.send(bytes("a","utf-8"))
        elif (keyboard.is_pressed('d')):
            s.send(bytes("d","utf-8"))
        else:
            s.send(bytes('stop',"utf-8"))      
    except:
        break  
s.close()
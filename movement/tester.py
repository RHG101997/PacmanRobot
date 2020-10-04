import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

speed = 75
en1 = 25
en2 = 27
gpio.setmode(gpio.BCM)

gpio.setup(en1,gpio.OUT) #pwm
gpio.setup(en2,gpio.OUT) 

gpio.setup(17, gpio.OUT) #right wheels
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT) #left wheels
gpio.setup(24, gpio.OUT)

gpio.setup(21, gpio.IN) # check if object detected

p1 = gpio.PWM(en1,1000)
p2 = gpio.PWM(en2,1000)

p1.start(speed)
p2.start(speed)


def forward():
 p1.ChangeDutyCycle(speed)
 p2.ChangeDutyCycle(speed)
 gpio.output(17, False)
 gpio.output(22, True)
 gpio.output(23, True)
 gpio.output(24, False)
 time.sleep(0.030)
 stop()

def reverse():
 p1.ChangeDutyCycle(speed)
 p2.ChangeDutyCycle(speed)
 gpio.output(17, True)
 gpio.output(22, False)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(0.030)
 stop()
 
 
def turnRight():
 gpio.output(17, False)
 gpio.output(22, True)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(0.1)
 stop()
 
def turnLeft():
 gpio.output(17, True)
 gpio.output(22, False)
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(0.1)
 stop()


def stop():
 gpio.output(17, False)
 gpio.output(22, False)
 gpio.output(23, False) 
 gpio.output(24, False)
 
 
def checkFront():
    if not gpio.input(21):
        return True
    else:
        return False

 
def key_input(event):
    key_press = event.char
    
    print("Detect: " + str(checkFront()))
    if checkFront:
        #print("Detect: " + str(gpio.input(21)))
        if key_press.lower() == "w":
            forward()
        elif key_press.lower() == "s":
            reverse()
        elif key_press.lower() == "d":
            turnRight()
        elif key_press.lower() == "a":
            turnLeft()
    

comm = tk.Tk()
comm.bind('<KeyPress>', key_input)
comm.mainloop()
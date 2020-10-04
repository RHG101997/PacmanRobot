import RPi.GPIO as GPIO
import time

sensor = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)



print "IR Sensor Ready....."
print " "

try: 
   while True:
      if GPIO.input(sensor):
          print "Object Detected"
          time.sleep(0.2)
      else:
          print "Not"


except KeyboardInterrupt:
    GPIO.cleanup()
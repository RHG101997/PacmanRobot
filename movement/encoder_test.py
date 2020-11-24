import RPi.GPIO as GPIO

rigth_A_pin = 21
right_B_pin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(rigth_A_pin, GPIO.IN)
GPIO.setup(right_B_pin, GPIO.IN)

outcome = [0,-1,1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0]
last_AB = 0b00
counter = 0

while True:
    A = GPIO.input(rigth_A_pin)
    B = GPIO.input(right_B_pin)
    current_AB = (A<<1) | B
    pos = (last_AB << 2) | current_AB
    counter += outcome[pos]
    last_AB = current_AB
    print(counter)
    
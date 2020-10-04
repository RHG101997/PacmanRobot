from move import Move
import time


#Initializing Move
move = Move()
move.changeSpeed(50)


def testTime(angle):
    print("Please Block The front sensor to begin.")
    while(not move.checkFront()): 
        print("Waiting")
        time.sleep(2) 

    begin_time = time.time()
    move.turnLeft()
    time.sleep(0.5) #allowing the car to move
    # Waiting for next sensor update
    while(not move.checkFront()):
        pass
    # Calculate time
    result = time.time()-begin_time
    move.stop()
    return (angle,result)


test_time = testTime(90)
print(str(test_time[0])+"degree turn was: " + str(test_time[1]))

test2 = (90*test_time[1])/test_time[0]
time.sleep(5)
print("Turning 180 degree Test: " + str(test2)+ "secs")
move.turnRightByTime(test2)



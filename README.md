# PacmanRobot Resources
![Pacman game](https://attend.ieee.org/southeastcon-2021/wp-content/uploads/sites/213/image.png)
---

## Information:

This project is a robot that will follow the rules of a competition in IEEE SoutheastCon.
[Competition Website](https://attend.ieee.org/southeastcon-2021/student-program/hardware-competition/)

[Rules](https://attend.ieee.org/southeastcon-2021/wp-content/uploads/sites/213/Hardware-Rules-v2.0.pdf)


## How it Works

1. The initial script is **start.py**
    * This script will import the values from the config.ini
    * Creat all the objects that the robot will need to run like: Vision and Move classes
2. The classes will pull the information for their respective function from the config file as well
    * This was done for the purpose of modularity and faster configuration.
    * All the changes to the project should be done thorugh this file
3. Move class will handle:
    * Calibration: turning the robot 360 degress and getting calculating the time
    * This script will also move the robot and controll all the pins related to movement
4. Vision class will handle:
    * This class talk to the camera and also performs the proccessing requiered to detect objects
    * Some calculatation will be performed to redirect the robot and take action.

---

### Vision

![Object detection](/imgs/obj_detect.jpg=250x)

* The image above show a ball been detected(Yellow circle)
* After the position on camera is acquired, we calculate the distance from center(Redline)
* The size of that line will indicate
    1. How much degrees robot needs to turn
    2. (Left or Right) Which direction the object is on
* The field of view is important because the calculation requires:  

**angle_turn** = *((field_of_view/2)*(lenght_red_line_in_pixels))/(width_of_screen_in_pixels/2)*

## References
[OpenCV](https://opencv.org/)

[RaspberryPI](https://www.raspberrypi.org/)


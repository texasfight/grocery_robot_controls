import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
from gpiozero import Motor, Servo, DistanceSensor, LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


green_led = LED(14)
green_led.blink(n=5)

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_36h11)
aruco_params = cv2.aruco.DetectorParameters_create()

STRAIGHT = [0, 1, 4, 5, 11]
RIGHT = [2, ]
LEFT = [3, ]
STOP = [1, 4, 6]
KILL = [10, ]

PWM_FACTORY = PiGPIOFactory()

# Initialize devices
servo = Servo(12, pin_factory=PWM_FACTORY, min_pulse_width=10/10000, max_pulse_width=21/10000)
distance_front = DistanceSensor(echo=18, trigger=24, pin_factory=PWM_FACTORY)
distance_left = DistanceSensor(echo=17, trigger=27, pin_factory=PWM_FACTORY)
distance_right = DistanceSensor(echo=5, trigger=6, pin_factory=PWM_FACTORY)
red_led = LED(15)


main_motor = Motor(20, 16)

TURNING_RIGHT = False
TURNING_LEFT = False


def stop_signal(direction: str):
    print(f"Too close: {direction}!")
    red_led.on()
    main_motor.stop()

# Start capturing video data
current_node = None
vs = VideoStream(src=0).start()
while True:

    # Fast stop  on
    if distance_front.distance * 100 < 25:
        stop_signal("front")
        continue
    elif distance_right.distance * 100 < 10:
        stop_signal("right")
        continue
    elif distance_left.distance * 100 < 10:
        stop_signal("left")
        continue


    # read in and resize the data
    frame = vs.read()
    frame = imutils.resize(frame, width=600)


    red_led.off()
    # detect markers and IDs
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

    current_node = ids[0][0] if ids else current_node

    if current_node in KILL:
        main_motor.stop()
        servo.mid()
        RIGHT = [2, ]
        STOP = [1, 4, 6]
        LEFT = [3, ]
    elif current_node == 8:
        main_motor.forward(.9)
        servo.mid()
        TURNING_LEFT = False
        TURNING_RIGHT = False
        RIGHT = [3, ]
        LEFT = [2, ]
        STOP = [5, 1, 4]
    elif current_node in STOP:
        main_motor.stop()
        servo.mid()
        sleep(5)
        STOP.remove(current_node)
    elif current_node in STRAIGHT:
        TURNING_LEFT = False
        TURNING_RIGHT = False
        main_motor.forward(.9)
        servo.mid()
    elif current_node in RIGHT:
        TURNING_LEFT = False
        main_motor.forward(.7)
        if not TURNING_RIGHT:
            servo.mid()
            sleep(1)
        servo.min()
        TURNING_RIGHT = True
    elif current_node in LEFT:
        TURNING_RIGHT = False
        main_motor.forward(.7)
        if not TURNING_LEFT:
            servo.mid()
            sleep(1)
        servo.max()
        TURNING_LEFT = True


cv2.destroyAllWindows()
vs.stop()

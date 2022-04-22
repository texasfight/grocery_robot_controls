import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
from gpiozero import Motor, Servo, DistanceSensor, LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_36h11)
aruco_params = cv2.aruco.DetectorParameters_create()

PWM_FACTORY = PiGPIOFactory()

# Initialize devices
servo = Servo(12, pin_factory=PWM_FACTORY)
distance_front = DistanceSensor(24, 18, pin_factory=PWM_FACTORY)
# TODO: Fill the pins of the side sensors
distance_left = DistanceSensor()
distance_right = DistanceSensor()

# Start capturing video data
vs = VideoStream(src=0).start()
while True:
    # read in and resize the data
    frame = vs.read()
    frame = imutils.resize(frame, width=600)

    # detect markers and IDs
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

    # Sort corner by height. The first corner should be the top_left
    corners_sorted = sorted(corners[0], key=lambda x: x[1])
    top_left = corners[0][0]
    if corners_sorted.index(top_left) <= 1:
        in_reverse = True
    else:
        reverse = False






    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()

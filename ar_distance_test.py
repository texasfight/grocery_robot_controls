import cv2
import numpy as np
from imutils.video import VideoStream
import imutils

from gpiozero import Motor, Servo, DistanceSensor, LED
from gpiozero.pins.pigpio import PiGPIOFactory


aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_36h11)

vs = VideoStream(src=0).start()


PWM_FACTORY = PiGPIOFactory()
distance_front = DistanceSensor(echo=17, trigger=27, pin_factory=PWM_FACTORY)
distance_right = DistanceSensor(echo=18, trigger=24, pin_factory=PWM_FACTORY)
aruco_params = cv2.aruco.DetectorParameters_create()

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=600)

    if distance_front.distance * 100 < 10:
        print("Too Close!!!!")
        continue
    elif distance_right.distance * 100 < 10:
        print("right too close!!!")
        continue

    corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

    if ids is not None:
        print(f"Detected Tag: {ids.flatten()}")

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()

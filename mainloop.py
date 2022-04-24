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

PWM_FACTORY = PiGPIOFactory()

# Initialize devices
servo = Servo(12, pin_factory=PWM_FACTORY)
distance_front = DistanceSensor(echo=18, trigger=24, pin_factory=PWM_FACTORY)
distance_left = DistanceSensor(echo=5, trigger=6, pin_factory=PWM_FACTORY)
distance_right = DistanceSensor(echo=17, trigger=27, pin_factory=PWM_FACTORY)
red_led = LED(15)


main_motor = Motor(20, 16)

def stop_signal(direction: str):
    print(f"Too close in the {direction}!")
    red_led.on()
    main_motor.stop()
    servo.mid()

# Start capturing video data
running = False
current_node = None
vs = VideoStream(src=0).start()
while True:
    # read in and resize the data
    frame = vs.read()
    frame = imutils.resize(frame, width=600)

    if distance_front.distance * 100 < 10:
        stop_signal("front")
        continue
    elif distance_right.distance * 100 < 10:
        stop_signal("right")
        continue
    elif distance_left.distance * 100 < 10:
        stop_signal("left")
        continue

    red_led.off()
    # detect markers and IDs
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

    new_id = ids[0][0] if ids else None

    if new_id:
        current_node = new_id
        # Sort corner by height. The first corner should be the top_left
        corners_sorted = sorted(corners[0], key=lambda x: x[1])
        top_left = corners[0][0]
        if np.where(corners_sorted == top_left)[0] <= 1:
            in_reverse = True
        else:
            in_reverse = False

    if current_node == 1:
        if in_reverse:
            servo.min()
        else:
            servo.max()
        main_motor.start()







    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()

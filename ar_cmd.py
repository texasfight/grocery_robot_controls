import cv2
import numpy as np
from imutils.video import VideoStream
import imutils

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_APRILTAG_36h11)

vs = VideoStream(src=0).start()

aruco_params = cv2.aruco.DetectorParameters_create()

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=600)

    corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

    if ids:
        print(f"Detected Tag: {ids}")

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()

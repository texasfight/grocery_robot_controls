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

    if len(corners) > 0:
        ids = ids.flatten()
        for markerCorner, markerID in zip(corners, ids):
            corners = markerCorner.reshape((4,2))
            corners = [[int(coord) for coord in corner] for corner in corners]

            for i in range(len(corners)):
                cv2.line(frame, corners[i], corners[(i + 1) % 4], (0, 255, 0), 2)

            cv2.putText(frame, str(markerID), (corners[0][0], corners[0][1] - 15), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()

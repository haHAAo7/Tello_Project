import cv2
import numpy as np
from djitellopy import Tello

from drone import tello
from parameters import hsv_params, detection_params
from image_functions import stackImages, getContours, display


cap = cv2.VideoCapture(0)
tello.connect()
tello.streamon()
# tello.takeoff()

hsv_params()
detection_params()

while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (640, 480))
    imgContour = img.copy()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    imgBlur = cv2.GaussianBlur(result, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
    getContours(imgDil, imgContour)
    display(imgContour)

    imgStack = stackImages(0.7, ([img, result],
                                 [imgDil, imgContour]
                                 ))

    cv2.imshow('Image', imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        tello.streamoff()
        # tello.land()
        break

cap.release()
cv2.destroyAllWindows()

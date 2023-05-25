import cv2


def empty(_):
    pass


def hsv_params():
    cv2.namedWindow("HSV")
    cv2.resizeWindow("HSV", 640, 240)
    cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
    cv2.createTrackbar("HUE Max", "HSV", 30, 179, empty)
    cv2.createTrackbar("SAT Min", "HSV", 255, 255, empty)
    cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
    cv2.createTrackbar("VALUE Min", "HSV", 36, 255, empty)
    cv2.createTrackbar("VALUE Max", "HSV", 134, 255, empty)


def detection_params():
    cv2.namedWindow("Parameters")
    cv2.resizeWindow("Parameters", 640, 240)
    cv2.createTrackbar("Threshold1", "Parameters", 106, 255, empty)
    cv2.createTrackbar("Threshold2", "Parameters", 60, 255, empty)
    cv2.createTrackbar("Area", "Parameters", 6897, 35000, empty)

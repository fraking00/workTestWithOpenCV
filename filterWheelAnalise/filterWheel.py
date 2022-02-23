import numpy as np
import cv2 as cv 

#for video capturing by your webcam
camera = cv.VideoCapture(0)

while(1):

    #reading the image
    _, frame = camera.read()

    #color reading conversion
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #color limits in hsv
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    lower_white = np.array([0,0,168])
    upper_white = np.array([172,111,255])

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    #color masks and composition of masks with or and and
    yellow_mask = cv.inRange(hsv, lower_yellow, upper_yellow)
    blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
    white_mask = cv.inRange(hsv, lower_white, upper_white)
    sum_mask = white_mask | blue_mask | yellow_mask
    Wcommon_allfilter_mask = white_mask & blue_mask & yellow_mask
    Wcommon_WhandY_mask = yellow_mask & white_mask

    #result of composition
    res_blue = cv.bitwise_and(frame, frame, mask= blue_mask)
    res_white = cv.bitwise_and(frame, frame, mask = white_mask)
    res_yellow = cv.bitwise_and(frame, frame, mask = yellow_mask)
    res_sum = cv.bitwise_and(frame, frame, mask = sum_mask)
    res_Wcommon_allfilter = cv.bitwise_and(frame, frame, mask = Wcommon_allfilter_mask)
    res_Wcommon_WhandY = cv.bitwise_and(frame, frame, mask = Wcommon_WhandY_mask)

    #window after the selection of the wheel tipe
    cv.imshow('frame',frame)
    cv.imshow('yellow_filter',res_yellow)
    cv.imshow('blue_filter',res_blue)
    cv.imshow('white_filter',res_white)
    cv.imshow('sum_filter',res_sum)
    cv.imshow('ALLCOMMON_filter',res_Wcommon_allfilter)
    cv.imshow('Y&W_filter',res_Wcommon_WhandY)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

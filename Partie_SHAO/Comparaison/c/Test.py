import cv2
import numpy as np
import sys

kernel_15 = np.ones((15,15),np.uint8)
kernel_50 = np.ones((50,50),np.uint8)

cube_rgb = cv2.imread('blue.jpg')
cube_gray = cv2.cvtColor(cube_rgb, cv2.COLOR_BGR2GRAY)# en gray
cube_hsv = cv2.cvtColor(cube_rgb,cv2.COLOR_BGR2HSV)# en hsv
cube_gray = cv2.adaptiveThreshold(cube_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

lower_red = np.array([156, 43, 46])
upper_red = np.array([182, 255, 255])
red_mask = cv2.inRange(cube_hsv, lower_red, upper_red)
red_erosion = cv2.erode(red_mask, kernel_15, iterations = 1)
red_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = red_erosion)

lower_orange = np.array([11, 43, 46])
upper_orange = np.array([25, 255, 255])
orange_mask = cv2.inRange(cube_hsv, lower_orange, upper_orange)
orange_erosion = cv2.erode(orange_mask, kernel_15, iterations = 1)
orange_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = orange_erosion)

lower_green = np.array([35,43,46])
upper_green = np.array([77,255,255])
green_mask = cv2.inRange(cube_hsv, lower_green, upper_green)
green_erosion = cv2.erode(green_mask, kernel_15, iterations = 1)
green_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = green_mask)

lower_white = np.array([0,0,220])
upper_white = np.array([180,30,255])
white_mask = cv2.inRange(cube_hsv, lower_white, upper_white)
white_erosion = cv2.erode(white_mask, kernel_15, iterations = 1)
white_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = white_mask)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
blue_mask = cv2.inRange(cube_hsv, lower_blue, upper_blue)
blue_erosion = cv2.erode(blue_mask, kernel_15, iterations = -1)
blue_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = blue_mask)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
blue_mask = cv2.inRange(cube_hsv, lower_blue, upper_blue)
blue_erosion = cv2.erode(blue_mask, kernel_15, iterations = -1)
blue_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = blue_mask)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
blue_mask = cv2.inRange(cube_hsv, lower_blue, upper_blue)
blue_erosion = cv2.erode(blue_mask, kernel_15, iterations = 1)
blue_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = blue_mask)





cv2.namedWindow('image',0)
#cv2.imshow('image1',red_res)
#cv2.imshow('image2',orange_res)
#cv2.imshow('image3',green_res)
cv2.imshow('image4',blue_res)
#cv2.imshow('image5',white_res)
#cv2.imshow('image6',yellowe_res)


cv2.waitKey(0)
cv2.destroyAllWindows()
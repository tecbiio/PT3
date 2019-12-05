import cv2
import numpy as np
import sys

kernel_15 = np.ones((15,15),np.uint8)
kernel_50 = np.ones((50,50),np.uint8)

cube_rgb = cv2.imread('up.jpg')
cube_gray = cv2.cvtColor(cube_rgb, cv2.COLOR_BGR2GRAY)# en gray
cube_hsv = cv2.cvtColor(cube_rgb,cv2.COLOR_BGR2HSV)# en hsv
cube_gray = cv2.adaptiveThreshold(cube_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

lower_red = np.array([170, 110, 145])
upper_red = np.array([182, 240, 255])
red_mask = cv2.inRange(cube_hsv, lower_red, upper_red)
red_erosion = cv2.erode(red_mask, kernel_15, iterations = 1)
red_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = red_erosion)

lower_orange = np.array([3, 115, 195])
upper_orange = np.array([9, 190, 255])
orange_mask = cv2.inRange(cube_hsv, lower_orange, upper_orange)
orange_erosion = cv2.erode(orange_mask, kernel_15, iterations = 1)
orange_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = orange_erosion)

cv2.namedWindow('image',0)
cv2.imshow('image1',red_res)
cv2.imshow('image2',orange_res)

cv2.waitKey(0)
cv2.destroyAllWindows()
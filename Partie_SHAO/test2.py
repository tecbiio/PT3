import cv2
import numpy as np
from copy import deepcopy
import math

imgobj = cv2.imread('/Users/romainshao/Downloads/img/31.jpg')

gray = cv2.cvtColor(imgobj, cv2.COLOR_BGR2GRAY)

hsv=cv2.cvtColor(imgobj,cv2.COLOR_BGR2HSV)

gray = np.float32(gray)

dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
imgobj[dst>0.01*dst.max()]=[0,0,255]

lower_blanc=np.array([0,0,211])
upper_blanc=np.array([180,30,255])

mask1 = cv2.inRange(hsv,lower_blanc,upper_blanc)
res=cv2.bitwise_and(imgobj,imgobj,mask=mask1)


cv2.namedWindow('dst',cv2.WINDOW_NORMAL)
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.imshow('dst',imgobj)
cv2.imshow('img',res)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
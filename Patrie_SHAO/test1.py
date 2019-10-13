import numpy as np
import cv2

 #read image avec color
#img = cv2.imread('/Users/romainshao/Downloads/img/333.jpeg',cv2.IMREAD_COLOR)
#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#im = cv2.imread('/Users/romainshao/Downloads/img/333.jpeg')
#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,127,255,0)
#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#img = cv2.drawContours(img, contours, 3, (0,255,0), 3)

img = cv2.imread('/Users/romainshao/Downloads/img/21.jpeg',cv2.IMREAD_COLOR)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#pour blue
lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])

#pour vert
lower_vert=np.array([35,43,46])
upper_vert=np.array([77,255,255])

#pour rouge
lower_rouge=np.array([156,43,46])
upper_rouge=np.array([[180,255,255]])

#pour blanc
lower_blanc=np.array([0,0,211])
upper_blanc=np.array([180,30,255])

#pour orange
lower_orange=np.array([11,43,46])
upper_orange=np.array([25,255,255])

#pour jaune
lower_jaune=np.array([26,43,46])
upper_jaune=np.array([34,255,255])

mask1 = cv2.inRange(hsv,lower_blue,upper_blue)
mask2 = cv2.inRange(hsv,lower_vert,upper_vert)
mask3 = cv2.inRange(hsv,lower_rouge,upper_rouge)
mask4 = cv2.inRange(hsv,lower_blanc,upper_blanc)
mask5 = cv2.inRange(hsv,lower_orange,upper_orange)
mask6 = cv2.inRange(hsv,lower_jaune,upper_jaune)

#res=cv2.bitwise_and(img,img,mask=mask1)
res=cv2.bitwise_and(img,img,mask=mask2)
#res=cv2.bitwise_and(img,img,mask=mask3)
#res=cv2.bitwise_and(img,img,mask=mask4)
#res=cv2.bitwise_and(img,img,mask=mask5)
#res=cv2.bitwise_and(img,img,mask=mask6)


#cv2.imshow('img',img)
#cv2.imshow('mask',mask)
#cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('res',res)
k=cv2.waitKey(0)&0xFF
if k == ord('q'):
	cv2.destroyAllWindows()

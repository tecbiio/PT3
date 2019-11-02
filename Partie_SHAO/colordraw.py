# -*- coding:utf-8 -*-
import cv2
import numpy as np
import sys
from numpy import *

draw = np.zeros((480,640, 3), dtype="uint8")    
def drawcolor(get_str):
    #strcolor={'U':(0,255,255),'R':(0,255,0),'F':(0,0,255),'D':(255,255,255),'L':(255,191,0),'B':(0,128,255)}  
    #strcolor="URFDLB"  
    draw_str=[]
    #BGR:
    U=(0,255,255)
    R=(0,255,0)
    F=(0,0,255)
    D=(255,255,255)
    L=(255,191,0)
    B=(0,128,255) 
    for key in get_str:
        if key=='U':
            draw_str.append(U)
        elif key=='R':
            draw_str.append(R)
        elif key=='F':
            draw_str.append(F)
        elif key=='D':
            draw_str.append(D)
        elif  key=='L':
            draw_str.append(L)
        elif  key=='B':
            draw_str.append(B)   
#上面 dessus 
    cv2.rectangle(draw, (160, 160-150), (160+50,160-100), draw_str[0],-1)
    cv2.rectangle(draw, (160+50, 160-150), (160+100, 160-100), draw_str[1], -1)
    cv2.rectangle(draw, (160+100, 160-150), (160+150,160-100),draw_str[2], -1)
    cv2.rectangle(draw, (160, 160-100), (160+50, 160-50), draw_str[3], -1)
    cv2.rectangle(draw, (160+50, 160-100), (160+100, 160-50),draw_str[4],-1)
    cv2.rectangle(draw, (160+100,160-100), (160+150, 160-50),draw_str[5], -1)
    cv2.rectangle(draw, (160,160-50), (160+50, 160),draw_str[6], -1)
    cv2.rectangle(draw, (160+50, 160-50), (160+100,160),draw_str[7], -1)
    cv2.rectangle(draw, (160+100,160-50), (160+150, 160),draw_str[8], -1)
    
#右面 droit
    cv2.rectangle(draw, (310, 160), (310+50,160+50),draw_str[9],-1)
    # Color 2
    cv2.rectangle(draw, (310+50, 160), (310+100, 160+50), draw_str[10], -1)
    # Color 3
    cv2.rectangle(draw, (310+100, 160), (310+150,160+50),draw_str[11], -1)
    # Color 4
    cv2.rectangle(draw, (310, 160+50), (310+50, 160+100),draw_str[12], -1)
    # Color 5
    cv2.rectangle(draw, (310+50, 160+50), (310+100, 160+100),draw_str[13],-1)
    # Color 6
    cv2.rectangle(draw, (310+100,160+50), (310+150, 160+100),draw_str[14], -1)
    # Color 7
    cv2.rectangle(draw, (310, 160+100), (310+50, 160+150), draw_str[15], -1)
    # Color 8
    cv2.rectangle(draw, (310+50, 160+100), (310+100,160+150),draw_str[16], -1)
    # Color 9
    cv2.rectangle(draw, (310+100,160+100), (310+150, 160+150),draw_str[17], -1)
    
#前面 Avant
    cv2.rectangle(draw, (160, 160), (160+50,160+50), draw_str[18],-1)
    # Color 2
    cv2.rectangle(draw, (160+50, 160), (160+100, 160+50), draw_str[19], -1)
    # Color 3
    cv2.rectangle(draw, (160+100, 160), (160+150,160+50), draw_str[20], -1)
    # Color 4
    cv2.rectangle(draw, (160, 160+50), (160+50, 160+100), draw_str[21], -1)
    # Color 5
    cv2.rectangle(draw, (160+50, 160+50), (160+100, 160+100), draw_str[22],-1)
    # Color 6
    cv2.rectangle(draw, (160+100,160+50), (160+150, 160+100), draw_str[23], -1) 
    # Color 7
    cv2.rectangle(draw, (160, 160+100), (160+50, 160+150),draw_str[24], -1)
    # Color 8
    cv2.rectangle(draw, (160+50, 160+100), (160+100,160+150),draw_str[25], -1)
    # Color 9
    cv2.rectangle(draw, (160+100,160+100), (160+150, 160+150),draw_str[26], -1)
   
#下面 dessous
    cv2.rectangle(draw, (160, 160+150), (160+50,160+200),draw_str[27],-1)
    # Color 2
    cv2.rectangle(draw, (160+50, 160+150), (160+100, 160+200), draw_str[28], -1)
    # Color 3
    cv2.rectangle(draw, (160+100, 160+150), (160+150,160+200), draw_str[29], -1)
    # Color 4
    cv2.rectangle(draw, (160, 160+200), (160+50, 160+250),draw_str[30], -1)
    # Color 5
    cv2.rectangle(draw, (160+50, 160+200), (160+100, 160+250), draw_str[31],-1)
    # Color 6
    cv2.rectangle(draw, (160+100,160+200), (160+150, 160+250),draw_str[32], -1)
    # Color 7
    cv2.rectangle(draw, (160, 160+250), (160+50, 160+300), draw_str[33], -1)
    # Color 8
    cv2.rectangle(draw, (160+50, 160+250), (160+100, 160+300),draw_str[34], -1)
    # Color 9
    cv2.rectangle(draw, (160+100,160+250), (160+150,  160+300), draw_str[35], -1)
    
#左面 Gauche
    cv2.rectangle(draw, (160-150, 160), (160-100,160+50), draw_str[36],-1)
    # Color 2
    cv2.rectangle(draw, (160-100, 160), (160-50, 160+50), draw_str[37], -1)
    # Color 3
    cv2.rectangle(draw, (160-50, 160), (160,160+50), draw_str[38], -1)
    # Color 4
    cv2.rectangle(draw, (160-150, 160+50), (160-100, 160+100), draw_str[39], -1)
    # Color 5
    cv2.rectangle(draw, (160-100, 160+50), (160-50, 160+100), draw_str[40],-1)
    # Color 6
    cv2.rectangle(draw, (160-50,160+50), (160, 160+100), draw_str[41], -1)
    # Color 7
    cv2.rectangle(draw, (160-150, 160+100), (160-100, 160+150), draw_str[42], -1)
    # Color 8
    cv2.rectangle(draw, (160-100, 160+100), (160-50,160+150), draw_str[43], -1)
    # Color 9
    cv2.rectangle(draw, (160-50,160+100), (160, 160+150), draw_str[44], -1)
    
#后面 Derrière
    cv2.rectangle(draw, (460, 160), (460+50,160+50),  draw_str[45],-1)
    # Color 2
    cv2.rectangle(draw, (460+50, 160), (460+100, 160+50), draw_str[46], -1)
    # Color 3
    cv2.rectangle(draw, (460+100, 160), (460+150,160+50),  draw_str[47], -1)
    # Color 4
    cv2.rectangle(draw, (460, 160+50), (460+50, 160+100), draw_str[48], -1)
    # Color 5
    cv2.rectangle(draw, (460+50, 160+50), (460+100, 160+100),  draw_str[49],-1)
    # Color 6
    cv2.rectangle(draw, (460+100,160+50), (460+150, 160+100),  draw_str[50], -1)
    # Color 7
    cv2.rectangle(draw, (460, 160+100), (460+50, 160+150),  draw_str[51], -1)
    # Color 8
    cv2.rectangle(draw, (460+50, 160+100), (460+100,160+150),  draw_str[52], -1)
    # Color 9
    cv2.rectangle(draw, (460+100,160+100), (460+150, 160+150), draw_str[53], -1)
   
    
    cv2.imshow('draw',draw)
    cv2.namedWindow('draw',cv2.WINDOW_NORMAL)



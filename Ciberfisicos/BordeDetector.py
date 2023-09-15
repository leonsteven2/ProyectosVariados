import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _,th = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
    contornos, jerarquia = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contornos, -1, (0,0,255), 3)

    if len(contornos) > 0:
        cnt = contornos[0]
        M = cv2.moments(cnt)
        if M["m00"] == 0:
            M["m00"] = 1
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])
        cv2.circle(frame, (cX,cY),5,(0,0,255),-1)
        cv2.putText(frame,"Enemigo",(cX-100,cY-50),1,3,(0,0,255),1)

    cv2.imshow('camara1' ,frame)
    cv2.imshow('camara2', th)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


import cv2
import numpy as np
cam = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)

while (True):
	ret,frame = cam.read()

	"SE DECLARA EL RANGO MINIMO Y MAXIMO DE COLOR A DETECTAR PARA EL AMIGO (B,G,R)"
	rangomaxAmigo = np.array([50,255,50])
	rangominAmigo = np.array([0,51,0])
	mascaraAmigo = cv2.inRange(frame, rangominAmigo, rangomaxAmigo)
	openingAmigo = cv2.morphologyEx(mascaraAmigo, cv2.MORPH_OPEN, kernel)
	x,y,w,h = cv2.boundingRect(openingAmigo)

	"ENCERRAMOS EN UN RECTANGULO VERDE Y UN PUNTO ROJO EN EL CENTRO AL AMIGO"
	cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 4)
	cv2.circle(frame, (x1 + w1 // 2, y1 + h1 // 2), 6, (0, 0, 255), -1)



	print("w1: "+str(w1))
	print("h1: "+str(h1))

	cv2.imshow('camara' ,frame)
	k = cv2.waitKey(1) & 0xFF
	if k==27:
		break
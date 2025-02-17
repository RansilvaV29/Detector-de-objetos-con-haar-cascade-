import cv2 
import numpy as np
import imutils 
import os 


datos = 'n'
if not os.path.exists(datos):
    print('Carpeta creada: ', datos)
    os.makedirs(datos)


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

x1, y1 = 190, 80
x2, y2 = 450, 400

count = 0
while True:
    ret, frame = cap.read()
    if ret == False: break
    imAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    objeto = imAux[y1:y2, x1:x2]
    objeto = cv2.resize(objeto, (150, 150), interpolation=cv2.INTER_CUBIC)

    k = cv2. waitKey(1)

    if k == 27:
        break
    if k == ord('s'):
        cv2.imwrite(datos + '/objeto_{}.jpg'.format(count), objeto)
        print('Imagen almacenada: ', datos + '/objeto_{}.jpg'.format(count))
        count = count + 1

    cv2.imshow('frame', frame)
    cv2.imshow('objeto', objeto)
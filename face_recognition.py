import cv2 as cv
import numpy as np

frameWidth = 800
frameHeight = 600
faceCascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
minArea = 500
color = (255, 0, 255)

cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 100)

while True:
    success, img = cap.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    count = 0
    for (x, y, w, h) in faces:
        # area = w*h
        # if area > minArea:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv.putText(img, 'Face', (x, y-5), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
        # imgRoi = img[y:y+h, x:x+w]
        # cv.imshow('ROI', imgRoi)
        print(f'face {count+1}')
        count += 1
        print(x, y, x + w, y + h)
    cv.imshow('video', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

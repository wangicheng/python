# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 19:55:24 2017

@author: DAKS
"""
import cv2

face_patterns = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

sample_image = cv2.imread('./opencv2.jpg')

faces = face_patterns.detectMultiScale(sample_image,scaleFactor=1.1,minNeighbors=8,minSize=(50, 50))

for (x, y, w, h) in faces:
    cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite('./opencv2-ok.jpg', sample_image);
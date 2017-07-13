# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 19:55:24 2017

@author: DAKS
"""

# coding:utf-8
import importlib,sys
importlib.reload(sys)

import cv2
# 待檢測的圖片路徑
imagepath = r'./opencv1.jpg'

face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

# 讀取圖片
image = cv2.imread(imagepath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 探測圖片中的人臉
faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.15,
            minNeighbors = 5,
            minSize = (5,5),
            flags = cv2.CASCADE_SCALE_IMAGE
        )

print ("發現{0}個人臉!".format(len(faces)))

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    #cv3.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)


cv2.imshow("Find Faces!",image)
cv2.waitKey(0)
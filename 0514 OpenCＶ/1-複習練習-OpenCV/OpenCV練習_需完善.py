#!/usr/bin/env python
# author: Chen0514練習
# -*- coding: utf-8 -*-

import numpy as np
import cv2
# 顯示圖片
# 圖片1
img = cv2.imread('eggplant.jpg')
colors= img.shape[2]
width= img.shape[1]
high=img.shape[0]
# 顯示方塊
img[0,0]=[0,0,255]   # [y,x]=[B,G,R]
img[0:10,0:10]=[0,255,0]
img[302-10:,:10]=[0,255,255]
img[high-10:,width-10:]=[0,0,255]
img[:10,width-10:]=[255,0,0]

cv2.imshow('eggplant',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 圖片2
img2 = cv2.imread('eggplant2.jpg')
cv2.imshow('eggplant2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 複製 貼上

img3=img2
img3[450:450+img.shape[0],15:15+img.shape[1]]=img
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 設計動畫 小的移動
img2 = cv2.imread('eggplant2.jpg')
t1=0
i=10
while True:
    img3 = img2.copy()
    img3[t1:t1+478,t1:t1+850] = img
    cv2.imshow('image', img3)
    t1=t1+i
    if (t1<img3.shape[1]-1) and (t1>1):
        i=i
    else:
        i=-i
    k = cv2.waitKey(100)   # 2 ms
    if k == 27:                       # wait for 27 ASCII的 ESC key to exit
        cv2.destroyAllWindows()
        break
    elif k == ord('s'):                # wait for 's' key to save and exit
        cv2.imwrite('test.png', img)   # png, bmp, jpg

# 儲存
cv2.imwrite("test.png",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
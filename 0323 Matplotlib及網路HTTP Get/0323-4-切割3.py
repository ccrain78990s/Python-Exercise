#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"
#參考網址 ↓
#https://matplotlib.org/stable/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py
import matplotlib.pyplot as plt
t1=[1,2,3,4]
t2=[2,4,6,8]
plt.subplot(3,1,1,facecolor='y')    #facecolor背景顏色
plt.plot(t1, t2, 'ro')

plt.subplot(3,1,3)
plt.plot(t2, t2, 'ys')

plt.subplot(3,3,4)
plt.plot(t2, t2, 'm^')

plt.subplot(3,3,5)
plt.plot(t2, t2, 'k*')





plt.show()
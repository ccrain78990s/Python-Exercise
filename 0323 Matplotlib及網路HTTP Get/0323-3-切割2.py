#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import matplotlib.pyplot as plt
t1=[1,2,3,4]
t2=[2,4,6,8]
plt.subplot(4,1,1,facecolor='y')    #facecolor背景顏色
plt.plot(t1, t2, 'ro')

plt.subplot(4,1,(2,3))
plt.plot(t2, t2, 'ys')


plt.subplot(4,3,10)
plt.plot(t2, t2, 'm^')

plt.subplot(4,3,12)
plt.plot(t2, t2, 'k*')

plt.show()
#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
v = np.array([9, 10], dtype=np.float64)

# 加法
print(x + y)        # 輸出 [[ 6.0  8.0] [10.0 12.0]]
print(np.add(x, y)) # 輸出 [[ 6.0  8.0] [10.0 12.0]]
print(x + 10)       # 輸出 [[11. 12.] [13. 14.]]
# 減法
print(x - y)        # 輸出 [[-4.0 -4.0] [-4.0 -4.0]]
print(np.subtract(x, y)) # 輸出 [[-4.0 -4.0] [-4.0 -4.0]]
print(x -[1,2])     # 輸出 [[0. 0.]  [2. 2.]]
#print(x-1)
""" 
1 2
3 4

1 2
1 2
"""
print("=========小練習==========")
x2=np.array([[1,2,3],[4,5,6]])
#[[0,0,0],[3,3,3]]
print(x2-[1,2,3])
#print(x2-[1,2])  #會錯
print(x2-[[1],[1]])
print(x2-1)
print(x2-[1])
print(x2-[[1],[2]])
print("========================")
# 乘法
print(x * y)
print(np.multiply(x, y)) # 輸出  [[ 5.0 12.0][21.0 32.0]]
# 除法
print(x / y)
print(np.divide(x, y))# 輸出 [[ 0.2  0.33333333] [ 0.42857143  0.5]]
# 平方
print(x **2)
#開根號
print(np.sqrt(x))# 輸出[[ 1. 1.41421356] [ 1.73205081  2.]]


#******↓ 線性代數相關  矩陣相乘
#矩陣乘法，兩個數組的點積 Dot product
#x = np.array([[1,2],[3,4]], dtype=np.float64)
#y = np.array([[5,6],[7,8]], dtype=np.float64)

print(x.dot(y))        # 輸出    [[19. 22.] [43. 50.]]      19= 1*5+ 2*7  22=1*6+2*8 43=3*5+4*7 50=3*6+4*8
print(np.dot(x, y))   # [[5+14 , 6+16] []]

"""
1 2   5  6
3 4   7  8
"""

print("========小練習========")
x = np.array([[1,2],[3,4]], dtype=np.float64)
# np.eye  # 相乘eye
x2=np.eye(2,2)
print(x * x2)
print(x.dot(x2))

#x=切割成以下
#x1=[1,2]
#x2=[3,4]
#然後相減
#=x1-x2
#[-2,-2]
x1=x[0,]
x2=x[1,]
print(x1-x2)

#均一化
x = np.array([[1,2],[3,4]], dtype=np.float64)
#請把x轉換成[[0,?],[?,1]]
x=x-1  #先減掉最小的
x=x/3  #再除以最大的
print(x)
#標準化
#請把x轉換成[[0.25,0.5],[0.72,1]]
x = np.array([[1,2],[3,4]], dtype=np.float64)
print(x/4)
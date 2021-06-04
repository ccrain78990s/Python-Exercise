#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1, :]
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

"""
1 2
5 6 
"""
# print(a[0:2, 0:2])
# print(a[:2, :2])
print("===0427練習===")
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b=a[0:2,0:2]
print(b)
c=a[1:,1:]
print(c)
d=a[:,1:2]
print(d)
e=a[:,1]
print(e)
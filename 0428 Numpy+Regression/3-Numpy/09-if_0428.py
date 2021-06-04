#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"


import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
bool_idx =  (a % 2)==0      #寫法1
bool_idx =  ((a % 2)==0)    #寫法2
print(bool_idx)
print(a[bool_idx])
print(a[a > 10])
print(a[a%2==1]*10)


#print(a[(a > 10) & (a%2==0)])
#print(a[(a > 10) | (a%2==0)])


print("===小練習===")
b = np.array([[10,20,30,40],        # 英文
              [50,60,70,80],        # 國文
              [90,100,110,120]])    # 數學

# 每個同學總成績
A=b[:,:1].sum()
print("A同學總成績",A)
B=b[:,1:2].sum()
print("B同學總成績",B)
C=b[:,2:3].sum()
print("C同學總成績",C)
D=b[:,3:].sum()
print("D同學總成績",D)
#print(np.sum(b,axis=0))
# 英文科平均分數
print("英文科平均分數",b[:1,:].mean())
#print(b[0].mean())
# 國文不及格分數
b2=b[1:2,:]
not60=b2[b2 < 60]
print("國文不及格分數",not60)
# 找出>60分數
print(">60分數",b[b>60])
# 找出 >60 並且 <=100  分數
print(">60 並且 <=100  分數",b[(b>60) & (b<=100)])
# 找出C同學不及格分數
c=b[:,2]
print("c同學不及格分數",c[c<60])


b = np.array([[10,20,30,40],        # 英文
              [50,60,70,80],        # 國文
              [90,100,110,120]])    # 數學
#標準化
print(b/120)
#均一化
b2=b-10
b2=b2/(120-10)
print(b2)

# -1 ~ 1
b3=b-b.mean()
b3=b3/(120-b.mean())
print(b3)

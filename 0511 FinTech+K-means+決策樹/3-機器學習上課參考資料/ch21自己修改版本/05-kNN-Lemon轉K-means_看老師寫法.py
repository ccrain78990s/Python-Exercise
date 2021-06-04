#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

X=[[9,9],[9.2,9.2],[9.6,9.2],[9.2,9.2],[6.7,7.1],[7,7.4],[7.6,7.5],
   [7.2,10.3], [7.3,10.5], [7.2,9.2], [7.3,10.2], [7.2,9.7], [7.3,10.1], [7.3,10.1],
   [27.2,20.3], [27.3,20.5], [27.2,29.2], [27.3,20.2], [27.2,29.7], [27.3,20.1], [27.3,20.1],
   [37.2,30.3], [37.3,30.5], [37.2,39.2], [37.3,30.2], [37.2,39.7], [37.3,30.1], [37.3,30.1],
   ]
y=[0,0,0,0,0,0,0,
   1,1,1,1,1,1,1,
   2,2,2,2,2,2,2,
   3,3,3,3,3,3,3,
   ]

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)

neigh.fit(X, y)

print("===KNN===")
print("預測答案＝",neigh.predict([[37.2,38.2],]))
print("預測樣本距離＝",neigh.predict_proba([[37.2,38.2]]))   #      測試數據X的返回概率估計。


# K-means

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn import metrics


X=[[9,9],[9.2,9.2],[9.6,9.2],[9.2,9.2],[6.7,7.1],[7,7.4],[7.6,7.5],
   [7.2,10.3], [7.3,10.5], [7.2,9.2], [7.3,10.2], [7.2,9.7], [7.3,10.1], [7.3,10.1],
   [27.2,20.3], [27.3,20.5], [27.2,29.2], [27.3,20.2], [27.2,29.7], [27.3,20.1], [27.3,20.1],
   [37.2,30.3], [37.3,30.5], [37.2,39.2], [37.3,30.2], [37.2,39.7], [37.3,30.1], [37.3,30.1],
   ]
y=[0,0,0,0,0,0,0,
   1,1,1,1,1,1,1,
   2,2,2,2,2,2,2,
   3,3,3,3,3,3,3,
   ]

lemon_X_train , lemon_X_test , lemon_y_train , lemon_y_test = train_test_split(X,y,test_size=0.2)


# KMeans 演算法
kmeans  = KMeans(n_clusters = 2)
kmeans_fit =kmeans.fit(lemon_X_train)



print("===K-means===")
print("實際",lemon_y_train)
print("預測",kmeans_fit.labels_)
#調整標籤的數字
lemon_y_train[lemon_y_train==1]=11
lemon_y_train[lemon_y_train==0]=1
lemon_y_train[lemon_y_train==11]=0
print("調整",lemon_y_train)

score = metrics.accuracy_score(lemon_y_train,kmeans.predict(lemon_X_train))
print('準確率:{0:f}'.format(score))
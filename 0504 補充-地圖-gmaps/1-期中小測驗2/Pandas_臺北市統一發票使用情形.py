#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen 0504"
import pandas as pd
df = pd.read_csv('臺北市統一發票使用情形.csv',encoding='big5')


print("===第一題===")
print(df.describe())
print("===第二題===")
# 第二題
# 延續上題
# 計算  每一張的平均[銷售額]  和
#      [年底使用家數[家]] / [全年銷售額[千元]]

df["每一張平均銷售額_千元"]=df["全年銷售額_千元"]/df["全年使用張數_張"]
print(df[["年別","稅別","每一張平均銷售額_千元"]])
print("全年平均每家銷售額_千元",df['全年銷售額_千元']/df['年底使用家數_家'])

print("===第三題===")
# 第三題
# 延續上題,  印出所有 	[稅別]=一般稅額 的 [全年銷售額[千元]
df2=df[df['稅別']=='一般稅額']
#print(df2)
print(df2[["年別","稅別","全年銷售額_千元"]])
print("===第四題===")
# 第四題
# 延續上題,   圖型化   所有	[稅別]=一般稅額 的 [全年銷售額[千元]
# x 用[年度], y  用 "[稅別]=一般稅額 的 [全年銷售額[千元]"

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  # 中文化

plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）


df2.plot(x='年別', y='全年銷售額_千元', color='blue')
plt.title('稅別:一般稅額之全年銷售額')
plt.show()

print("===第五題===")
# 第五題
# 並把 [稅別]=一般稅額 的資料抽取出來
# 新增一個欄位[label]
# [全年銷售額[千元]> 平均   , [label]=1
# [全年銷售額[千元] <= 平均 , [label]=0
mean=df['全年銷售額_千元'].mean()
print(mean)



df.loc[df['全年銷售額_千元'] > mean, 'label'] =1
df.loc[df['全年銷售額_千元'] <= mean, 'label'] =0
print(df)
df.to_csv('forKNN.csv')
#df['label'][df['全年銷售額_千元'] > mean]=1
#df['label'][df['全年銷售額_千元'] <= mean]=0

print("===第六題===")
#第六題
# 把上一提的資料, 轉成 numpy ,
# 並把 [全年銷售額[千元] 當成 x (features),
#     [label] 當成 y
# 帶入 KNN 的演算法
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv('forKNN.csv')
df2=df[df['稅別']=='一般稅額']
print(df2.head(100))
X= df2[['全年銷售額_千元']]
X=X.to_numpy()
Y= df2[['label']] # 2D
Y=Y.to_numpy()
t1=Y.shape[0]
Y=np.reshape(Y,(t1,))  # 2D 轉 1D

X_train , X_test , y_train , y_test = train_test_split(X,Y,test_size=0.2)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

print("預測",knn.predict(X_test))
print("實際",y_test)
print('準確率: %.2f' % knn.score(X_test, y_test))

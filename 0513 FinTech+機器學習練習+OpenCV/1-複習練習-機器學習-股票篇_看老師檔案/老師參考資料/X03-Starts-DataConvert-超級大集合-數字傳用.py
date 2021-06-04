#!/usr/bin/env python
# -*- coding=utf-8 -*-
# pip install seaborn
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics

#read data
df = pd.read_excel ('Stars.xls',0)
print(df.head())
############
# 文字分類 轉 數字分類
df["ColorNo"]=df.Color.astype("category").cat.codes                     # 文字分類轉成數字
df["Spectral_ClassNo"]=df.Spectral_Class.astype("category").cat.codes   # 文字分類轉成數字






#############
print("資料拆切---")
# 決定X 分類 和Y分類 要用的欄位
dfX=df[["L","R","A_M","ColorNo","Spectral_ClassNo","Spectral_Numer"]]
dfY=df["Temperature"]
X=dfX.to_numpy()
Y=dfY.to_numpy()
X_train ,X_test ,Y_train ,Y_test = train_test_split(X,Y,test_size=0.1)

#############
print("迴歸計算----------------------------------------")
from sklearn import linear_model
reg = linear_model.LinearRegression()    # 初使化
reg.fit(X_train,Y_train)
Y_test_predict= reg.predict(X_test)
print("regr.coef_ 係數:",reg.coef_)
print("reg.singular_ 單數:",reg.singular_)
print("---")
print(".               實際答案:",Y_test)
print("LinearRegression預測答案:",Y_test_predict)

print("Lass      計算--------------------------------------")
from sklearn import linear_model


model =linear_model.Lasso(alpha=0.1)
model.fit(X_train,Y_train)
Y_test_predict=model.predict(X_test)


print(".               實際答案:",Y_test)
print("Lass            預測答案:",Y_test_predict)
# print('.                 準確率:',metrics.accuracy_score(Y_test,Y_test_predict))    #算準確率

print("GaussianProcessRegressor      計算--------------------------------------")
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel


kernel = DotProduct() + WhiteKernel()
model= GaussianProcessRegressor(kernel=kernel, random_state=0)

model.fit(X_train,Y_train)
Y_test_predict=model.predict(X_test)

print(".               實際答案:",Y_test)
print("GaussianProcessRegressor   預測答案:",Y_test_predict)
# print('.                 準確率:',metrics.accuracy_score(Y_test,Y_test_predict) )    #算準確率


print("svm.SVR       計算--------------------------------------")
from sklearn import svm

model= svm.SVR()
model.fit(X_train,Y_train)
Y_test_predict=model.predict(X_test)

print(".               實際答案:",Y_test)
print("svm.SVR   預測答案:",Y_test_predict)
# print('.                 準確率:',metrics.accuracy_score(Y_test,Y_test_predict) )    #算準確率


print("svm.SVC      計算--------------------------------------")
from sklearn.model_selection import cross_val_score
model= svm.SVC(kernel='linear', C=1, random_state=42)
model.fit(X_train,Y_train)
Y_test_predict=model.predict(X_test)

print(".               實際答案:",Y_test)
print("svm.SVC         預測答案:",Y_test_predict)
# print('.                 準確率:',metrics.accuracy_score(Y_test,Y_test_predict) )    #算準確率



#############
print("畫seaborn 圖---")
df2=df[["Temperature","L","R","A_M","ColorNo","Spectral_ClassNo","Spectral_Numer","Type"]]
sns.set_theme(style="ticks")
#sns.set_theme(style="whitegrid")
sns.pairplot(df2)
plt.show()

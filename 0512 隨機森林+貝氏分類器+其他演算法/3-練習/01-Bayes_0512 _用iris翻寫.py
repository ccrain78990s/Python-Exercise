#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "C"
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets

# 載入資料
iris = datasets.load_iris()
# 資料拆切
iris_X_train , iris_X_test , iris_y_train , iris_y_test = train_test_split(iris.data,iris.target,test_size=0.2)


model = GaussianNB()
model.fit(iris_X_train,iris_y_train)
print(model.class_prior_ )
print(model.get_params() )

#Predict Output
predicted= model.predict(iris_X_test)
print(predicted)
print(model.predict_proba(iris_X_test))



#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import datasets

# 載入資料
iris = datasets.load_iris()
# 資料拆切
iris_X_train , iris_X_test , iris_y_train , iris_y_test = train_test_split(iris.data,iris.target,test_size=0.2)


model = RandomForestClassifier(n_estimators=100, max_depth=10,
                             random_state=2)
model.fit(iris_X_train, iris_y_train)

print("預測答案:",model.predict(iris_X_test))
print("實際答案:",iris_y_test)
print('準確率: %.2f' % model.score(iris_X_test, iris_y_test))


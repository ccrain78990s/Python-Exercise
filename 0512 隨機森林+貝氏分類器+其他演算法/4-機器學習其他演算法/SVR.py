#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
#https://scikit-learn.org/stable/modules/svm.html#svm-regression

from sklearn import svm
X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X, y)

print(regr.predict([[1, 1]]))

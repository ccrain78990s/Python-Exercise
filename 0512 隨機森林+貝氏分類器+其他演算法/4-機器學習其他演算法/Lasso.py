#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
#https://scikit-learn.org/stable/modules/linear_model.html#lasso
from sklearn import linear_model
reg = linear_model.Lasso(alpha=0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])

print(reg.predict([[1, 1]]))
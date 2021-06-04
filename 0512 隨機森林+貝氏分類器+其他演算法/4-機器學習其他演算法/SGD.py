#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
#https://scikit-learn.org/stable/modules/sgd.html
import numpy as np
from sklearn.linear_model import SGDClassifier
X=np.array([[180, 85],[174, 80],[170, 75],
      [167, 45],[158, 52],[155, 44]])
y = np.array([0,0,0,1,1,1])



clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
clf.fit(X, y)

print(clf.predict([[180, 85]]))




#clf = SGDClassifier(loss="log", max_iter=5).fit(X, y)
#clf.predict_proba([[180, 85]])


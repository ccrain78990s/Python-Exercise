#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

"""
其他參考網址
https://iter01.com/555869.html
"""


import numpy as np
from sklearn import tree
#from sklearn.externals.six import StringIO
import pydot
from os import system
import six


# Load the diabetes dataset
#iris = datasets.load_iris()

#iris_X_train , iris_X_test , iris_y_train , iris_y_test = train_test_split(iris.data,iris.target,test_size=0.2)



X=np.array([[180, 85],[174, 80],[170, 75],
      [167, 45],[158, 52],[155, 44]])
Y = np.array(['man', 'man','man','woman', 'woman',  'woman'])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

tree.export_graphviz(clf,out_file='tree.dot')

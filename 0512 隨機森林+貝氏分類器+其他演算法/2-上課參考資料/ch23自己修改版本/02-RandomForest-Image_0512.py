#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

from sklearn.ensemble import RandomForestClassifier

import numpy as np
from sklearn.datasets import make_classification

X, Y = make_classification(n_samples=10,
                           n_features=3,            # 特徵值
                           n_informative=2,         # 分類有幾種  label
                           n_redundant=0,
                           random_state=0,
                           shuffle=True)

model = RandomForestClassifier(n_estimators=100, max_depth=10,
                             random_state=2)
model.fit(X, Y)
print(model.feature_importances_)
print(model.predict([[0,0,0]]))
estimator = model.estimators_[5]

from sklearn.tree import export_graphviz
export_graphviz(estimator, out_file='tree.dot',
                feature_names = ["A","B","C"],
                class_names = ["0","1"],
                rounded = True, proportion = False,
                precision = 2, filled = True)

# 補充 : https://towardsdatascience.com/visualizing-decision-trees-with-python-scikit-learn-graphviz-matplotlib-1c50b4aa68dc
"""
#import os
#os.system('dot -Tpng tree.dot -o tree2.png')


# 自己補充 視覺化模型
# Convert to png using system command (requires Graphviz)
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree2.png'])

# Display in jupyter notebook
from IPython.display import Image
Image(filename = 'tree.png')
"""

"""
import pydot

(graph,) = pydot.graph_from_dot_file('C:/Users/User/Desktop/ch23自己修改版本/tree.dot')
graph.write_png('somefile.png')
"""


#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
#https://scikit-learn.org/stable/modules/gaussian_process.html
#https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor

from sklearn.datasets import make_friedman2
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
X, y = make_friedman2(n_samples=500, noise=0, random_state=0)
kernel = DotProduct() + WhiteKernel()
gpr = GaussianProcessRegressor(kernel=kernel,
        random_state=0)
gpr.fit(X, y)
gpr.score(X, y)

print(gpr.predict(X[:2,:], return_std=True))

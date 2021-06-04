#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"



import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd


# Load the diabetes dataset
iris = datasets.load_iris()

print("iris.data.shape=", iris.data.shape)   # features
print("dir(iris)", dir(iris))
print("iris.target.shape=", iris.target.shape)  # label
try:
    print("iris.feature_names=", iris.feature_names)
except:
    print("No iris.feature_names=")

import xlsxwriter
import pandas as pd

try:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
except:
    df = pd.DataFrame(iris.data, columns= ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])

df['target'] = iris.target

print(df.head())
df.to_csv("iris.csv", sep=',')
"""
writer = pd.ExcelWriter('iris.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
"""

dataframe=pd.read_csv('iris.csv')

# 畫seaborn 圖
df111 = dataframe[['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)','target']]
df222=df111[0:]
import seaborn as sns
sns.set_theme(style="ticks")
# df = sns.load_dataset("penguins")
sns.pairplot(df222,hue='target') #, hue="PM2.5")
#sns.pairplot(df2, hue="PM2.5")
plt.show()



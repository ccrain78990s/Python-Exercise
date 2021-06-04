#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
from IPython.display import display
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',50)
#pd.set_option('display.width', None)

df = pd.read_csv('上市公司2021EPS.csv',encoding="utf-8",sep=",")
df2=df.head(7)
print(df.head(7))
t1=df[['公司代號','公司名稱','產業別']]
print(t1[0:7])

display(df2)





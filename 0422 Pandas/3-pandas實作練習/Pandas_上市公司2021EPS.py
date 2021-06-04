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
#print(df.head(7))
#t1=df[['公司代號','公司名稱','產業別']]
#print(t1[0:7])
print("===資料大小===")
print(df.shape)
print("===欄位名稱===")
print(df.columns)
print("===索引指數===")
print(df.index)
print("===相關資訊===")
print(df.info())
print("===統計描述===")
print(df.describe())
print("===最大營業收入===")
print(df.營業收入.max())
print("===最大營業收入位置===")
print(df.營業收入.idxmax())
print("===最大營業收入資料全部顯示===")
print(df[268:269].transpose())
print("===最大營業收入===")
print(df.營業收入.min())
print("===最大營業收入偏度===")
print(df.營業收入.skew())
print("===最大營業收入峰度===")
print(df.營業收入.kurt())
print("===最大營業收入中位數===")
print(df.營業收入.median())

print("===================================================================")
print("====基本每股盈餘 Top10====")
print(df.sort_values(by=['基本每股盈餘(元)'], ascending=False)[:10])
print("====營業收入 Top10====")
print(df.sort_values(by=['營業收入'], ascending=False)[:10])
print("====營業外收入及支出 Top10====")
print(df.sort_values(by=['營業外收入及支出'], ascending=False)[:10])
print("====營業外收入及支出 > 營業收入Top10====")
df['營業外-營業內']=df['營業外收入及支出']-df['營業收入']
print(df.sort_values(by=['營業外-營業內'], ascending=False)[:10])
#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen 0504"
import pandas as pd
df = pd.read_csv('臺北市統一發票使用情形.csv',encoding='big5')
print(df.head10)


print("===第一題===")
print(df.describe())
print("===第二題===")
df['每一張平均銷售額']=df['全年銷售額[千元]']/df['全年使用張數[張]']
print(df['全年銷售額[千元]'].mean)
print("===第三題===")
print("===第四題===")
print("===第五題===")
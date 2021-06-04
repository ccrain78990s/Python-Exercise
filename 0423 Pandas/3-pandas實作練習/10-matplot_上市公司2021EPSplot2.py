#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "CHEN"

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）


df = pd.read_excel('上市公司2021EPS.xls', '上市公司2021EPS')

print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
# 第一題  X用 [公司名稱] Y  [營業收入] 畫出 圖表
# 第二題  [電子零組件業] 的資料,   X用 [公司名稱] Y  [營業收入] 畫出 圖表
# 第三題  [每一個 產業] 的資料,   X用 [公司名稱] Y  [營業收入] 畫出 同一個圖表
# 第四題  [半導體業, 電子零組件業,航運業] 的資料,   X用 [公司名稱] Y  [營業收入] 畫出 同一個圖表
print("===1.===")
df.plot(x='公司名稱', y='營業收入',grid=True, color='blue')
#plt.xticks(rotation=85)
plt.show()


# 1. 抓到有哪些 產業別
"""
distincts=df['產業別'].unique().tolist()
print(distincts)
"""

# 2. 計算 每一個  產業別 [營業收入]  加起來
"""
totalList=[]
for distinct in distincts:
    print(distinct)
    df1 = df[(df["產業別"] ==distinct)]
    total=df1["營業收入"].sum()
    print(distinct,total)
    totalList.append(total)
"""

# 3. bar

# 4. pie


"""

# 3 filter'

print("--------------------")
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())



# 4 Calculation
print("--------------------")
df['diff'] = df['Close']-df['Open']
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
df['day'] = pd.DatetimeIndex(df['Date']).day
print(df.head())
print("April Volume sum=%.2f" % df[df['month'] == 4][['Volume']].sum())
print("April Open mean=%.2d" % df[df['month'] == 4][['Open']].mean())







#  5 matplotlib
import matplotlib.pyplot as plt
#plt.plot(['2008-01-02','2008-01-03','2008-01-04',],[50,80,40])

df.plot(x='Date', y='Open',grid=True, color='blue')
plt.show()


import matplotlib.pyplot as plt
df.plot(y='diff',grid=True, color='red',kind='hist')
plt.show()




fig, ax = plt.subplots()
#print(df.groupby('month')[0])   #  [1,2,3,4,5,6,7,8,9,10,11,12]
for name, group in df.groupby('month'):
    group.plot(x='day', y='Open', ax=ax, label=name)
plt.show()

fileds=['Open','Close','High']
fig, ax = plt.subplots()
for name in fileds:
    df.plot(x='Date', y=name, ax=ax, label=name)
plt.show()

dfMonths = df.loc[df['month'].isin([1,2,3,4,5,6,7])]  # 在特定的資料中, 找出
print(dfMonths)
dfMonthsPivot = dfMonths.pivot_table(values = 'High', columns = 'month', index = 'day')
dfMonthsPivot.plot(kind = 'box',title = 'Months High')
plt.show()


"""
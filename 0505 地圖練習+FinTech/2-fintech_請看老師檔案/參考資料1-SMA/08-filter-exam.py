#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import pandas as pd
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())


# 3 filter'
t1=df['Date'] == '2018-01-05'
t2=df[t1]
print(t1)
print(t2)

print("--------------------")
print(df['Date'] == '2018-01-05')
print(df[df['Date'] == '2018-01-05'])

print("------------------- 找出Open> 44.0")

print(df[df['Open'] >44.0])
t1=df[df['Open'] >44.0]
print(t1.count())
print(df[df['Open'] >44.0].count())
print("--------------------")

# & |
# & and
# |  or
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 57])
print(df[['Date','Open']])
print(df[['Date','Open']][:5])


print(df[['Date','Open']][:100])   # < 42

# 前面100筆  Open<42
t1=df[:100]
t2=t1['Open']<42
t3=t1[t2]
print("前面100筆  Open<42")
print(t3)
# Open<42 顯示 10 筆
t0=df['Open'] <42
t1=df[t0]
t2=t1[:10]
print(df[df['Open']<42][:10])
print("<42 顯示 10 筆")
print(t2)

print("-----------------")


t1=df.sort_values(by=['Volume'])                           # 依照數字小的排列
print(df.sort_values(by=['Volume'])[:5])                   # 找出 最小的 5 筆
t2=df.sort_values(by=['Volume'], ascending=False)          # 依照數字大的排列
t3=df.sort_values(by=['Open','Volume'], ascending=False)   # 依照數字大的排列
print(df.sort_values(by=['Volume'], ascending=False)[:5])  # 找出 最大的 5 筆

# Close 價格最低的 low 5
print("-------Close 價格最低的 low 5")
t1=df.sort_values(by=['Close'])                           # 依照Close 數字小的排列
print(df.sort_values(by=['Close'])[:5])                   # 找出Close 最小的 5 筆

# Close 價格最高的 Top 5
print("---------Close 價格最高的 Top 5")
t2=df.sort_values(by=['Close'], ascending=False)          # 依照Close 數字大的排列
t3=t2[:5]                                                 # 依照Close數字最大的 5 筆
print(t3)
# 計算 漲跌 的價格 漲跌=Close-Open
df["漲跌"]=df["Close"]-df["Open"]                          # 漲跌
print(df.head(5))
# 找出 漲最多的 top 5
print(df.sort_values(by=['漲跌'], ascending=False)[:5])    #  [漲跌] 數字大的排列
print("-----------------")

t1=df['Open'].rolling(2)
print(t1)
t1=df['Open'].rolling(2).sum()
print(t1)

t1=df['Open'][:30]
t2=t1.rolling(7)
t3=t2.mean()
print(t3)

print(df['Close'][:30].rolling(7).mean())
print(df['Close'].rolling(7).mean())
print(df['Close'].rolling(7).mean().head(10))   #SMA 7
df["SMA7"]=df['Close'].rolling(7).mean()        #SMA7  計算
#1.  SMA30   ,30   close
print(df['Close'].rolling(30).mean().head(10))   #SMA 30
df["SMA30"]=df['Close'].rolling(30).mean()        #SMA30  計算

# SMA7 > SMA30
t1=df["SMA7"]>df["SMA30"]
df["SMA7Big30"]=t1 # SMA7 > SMA30
df["買賣訊號"]=df["SMA7Big30"].diff()         #  找出和其一筆不一樣的資料
# df["買賣訊號"]==True  df["SMA7Big30"]==True 買
buy=df[(df['買賣訊號'] == True) & (df['SMA7Big30'] ==True)]
print(buy)   #<------
#  df["買賣訊號"]==True  df["SMA7Big30"]==False 賣
sell=df[(df['買賣訊號'] == True) & (df['SMA7Big30'] ==False)]
print(sell)   #<------
# Close
buyprice=buy["Close"].sum()
sellprice=sell["Close"].sum()
total=sellprice-buyprice
print("總獲利:",total)

"""
buy.reset_index()
sell.reset_index()
print(buy.info())
print(sell.info())
total=buy["Close"]-sell["Close"]
print(total)
total=(buy["Close"]-sell["Close"]).sum()
print(total)
print(df.head(50))
"""



#2.  close  Top 5
print(df.sort_values(by=['Close'], ascending=False)[:5])



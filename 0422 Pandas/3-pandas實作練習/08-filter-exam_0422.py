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
# & |
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 57])
#print(df[df['Open'] > 44.0])
print(df[['Date','Open']])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())
print(df['Open'].rolling(7).mean())

print(df['Open'].rolling(7).mean().head(10))   #SMA 7




#1.  SMA30   ,30   close
print(df['Close'].rolling(30).mean().head(40))   #SMA 30
#2.  close  Top 5
print(df.sort_values(by=['Close'], ascending=False)[:5])

print("==小練習 前100筆 < 42==")
df2=df[:100]
df2=df2[df2['Open']<42]
print(df2)
print("==小練習 < 42 前10筆==")
df3=df[df['Open']<42]
df3=df3[:10]
print(df3)
print("==小練習 close low 5==")
print(df.sort_values(by=['Close'])[:5])
print("==小練習 close top 5==")
print(df.sort_values(by=['Close'], ascending=False)[:5])
print("==小練習 計算漲跌==")
df['漲跌']=df['Close']-df['Open']
print(df.head(5))
print("==小練習 漲福最多 top5==")
print(df.sort_values(by=['漲跌'], ascending=False)[:5])


print("==小練習 SMA3 & SMA5==")
df['SMA3']=df['Close'].rolling(3).mean()
df['SMA5']=df['Close'].rolling(5).mean()

df['3大於5']=df['SMA3']> df['SMA5']
df['買賣訊號']=df['3大於5'].diff()
print(df[30:])

print("===買買買===")
print(df[(df['3大於5']==True) & (df['買賣訊號']==True )])
buy=df[(df['3大於5']==True) & (df['買賣訊號']==True )]

print("===賣賣賣===")
print(df[(df['3大於5']==False) & (df['買賣訊號']==True )])
sell=df[(df['3大於5']==False) & (df['買賣訊號']==True )]

print("===獲利率===")
total=sell['Close'].sum()-buy['Close'].sum()
print(total)
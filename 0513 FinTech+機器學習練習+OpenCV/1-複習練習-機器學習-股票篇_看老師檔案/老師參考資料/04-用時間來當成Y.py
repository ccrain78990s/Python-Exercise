#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"
import pandas as pd
#import pandas.io.data as web
# python 2.x
# pip install pandas_datareader
# python 3.x
# pip3 install https://github.com/pydata/pandas-datareader.git
from pandas_datareader import data, wb
import pandas_datareader.data as web

import datetime
import time


import PKStock

#from mpl_finance import candlestick_ohlc
#import matplotlib.dates as mpl_dates


StockID="2330.tw"
start_date = '2010-01-01'
end_date = time.strftime("%Y-%m-%d")
"""
panel_data = data.DataReader(StockID, 'yahoo', start_date, end_date)

writer=pd.ExcelWriter(StockID+'.xlsx')
panel_data.to_excel(writer,StockID)
workbook = writer.book
worksheet = writer.sheets[StockID]
writer.save()
"""



"""
df = pd.read_excel(StockID+'.xlsx', StockID)
print(df.head())




print(df.head())
print(type(df))

df["date_id"]=df["Date"]
df=df.rename(columns={"Date": "date","Open": "open","Close": "close",
                      "High": "high","Low": "low"})

# df['date'] = df['date'].apply(mpl_dates.date2num)
# df = df.loc[:, ['date', 'open', 'high', 'low', 'close']]

#--------------------------------
#設定index 為日期
df.set_index('date_id', inplace = True)
print(df.head())

#--------------------------------
##接著 TA-Lib 登場~~
from talib import abstract  # abstract  是 talib 裡面計算指標用的


# #SMA5 30天平均
df["SMA5"]=abstract.SMA(df,5)
# #SMA5 100天平均
df["SMA10"]=abstract.SMA(df,10)
#--------------------------------
# rsv
print(df.head(-5))
df["rsv"] =(df['close']-df['close'].rolling(window=9).min())/(df['close'].rolling(window=9).max()-df['close'].rolling(window=9).min())*100


#--------------------------------
# KD
(K, df)=PKStock.mathK(df,'close',9,'K')
(D, df)=PKStock.mathD(df,'close',9,'D')


#-------------------------------
#RSI 9


df['RSI']=abstract.RSI(df,9)

#-----------
# MACD值
t1=abstract.MACD(df)
df['macd']=t1["macd"]
df['macdsignal']=t1["macdsignal"]
df['macdhist']=t1["macdhist"]

#-----------
#WILLR值
df['WILLR']=abstract.WILLR(df,9)


print(df.head(-5))
#----------

writer=pd.ExcelWriter(StockID+'_計算.xlsx')
df.to_excel(writer,StockID)
writer.save()


"""


df = pd.read_excel(StockID+'_計算.xlsx', StockID)

print(df.shape[0])
StartID=40
df=df[StartID:]    # 移除前面40筆
df["Y"]=0.0
print(df.head(5))
print(df.shape[0])
i=StartID
# df.at[42,'Y']=50
# df.iloc[41]["Y"] = 123


while i<df.shape[0]+StartID-1:
    t1=df["close"][i+1] # 明天的close
    df.at[i,'Y']= t1    # 放在今天的 Y
    i=i+1


df=df[:-1]    # 移除最後一筆

writer=pd.ExcelWriter(StockID+'_計算加上Y.xlsx')
df.to_excel(writer,StockID)
writer.save()


# 自己利用老師資料補的
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics

#read data
df = pd.read_excel ('2330.tw_計算加上Y.xls',0)
print(df.head())
############
# 文字分類 轉 數字分類
#df["ColorNo"]=df.Color.astype("category").cat.codes                     # 文字分類轉成數字
#df["Spectral_ClassNo"]=df.Spectral_Class.astype("category").cat.codes   # 文字分類轉成數字


#############
print("資料拆切---")
# 決定X 分類 和Y分類 要用的欄位

dfX=df[['high','low','open','close','Volume','Adj Close','SMA5','SMA10','rsv','RSV','K','D','RSI','macd','macdsignal','macdhist','WILLR']]
dfY=df['Y']
X=dfX.to_numpy()
Y=dfY.to_numpy()
X_train ,X_test ,Y_train ,Y_test = train_test_split(X,Y,test_size=0.1)

#############
print("迴歸計算----------------------------------------")
from sklearn import linear_model
reg = linear_model.LinearRegression()    # 初使化
reg.fit(X_train,Y_train)
Y_test_predict= reg.predict(X_test)
print("regr.coef_ 係數:",reg.coef_)
print("reg.singular_ 單數:",reg.singular_)
print("---")
print(".               實際答案:",Y_test)
print("LinearRegression預測答案:",Y_test_predict)


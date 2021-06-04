#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Chen"

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
# pip install yfinance
# pip install pandas_datareader
from pandas_datareader import data, wb
import pandas_datareader.data as web

# import fix_yahoo_finance as yf
# yf.pdr_override()

# pip install yfinance
import yfinance as yf


# 抓取資料存成 excel/csv

df = web.get_data_yahoo("2330", start="2010-01-01", end="2021-05-12")
print(df.head())
writer=pd.ExcelWriter('2330.xlsx')
df.to_excel(writer,'2330')
writer.save()


# WILLR威廉
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates
from matplotlib.font_manager import FontProperties
from talib import abstract
import PKStock
import pandas as pd
df = pd.read_excel('2330.xlsx', '2330')


df=df.rename(columns={"Date": "date","Open": "open","High": "high","Low": "low","Close": "close","Volume":"volume"})
#--------------------------------
#print(df.head())

#--------------------------------
#畫面分割
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
#--------------------------------
# K線圖
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates
ohlc = df.loc[:, ['date', 'open', 'high', 'low', 'close']]
ohlc['date'] = pd.to_datetime(ohlc['date'])
ohlc['date'] = ohlc['date'].apply(mpl_dates.date2num)
ohlc = ohlc.astype(float)
candlestick_ohlc(ax1, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)
ax1.set_title("K ")
#--------------------------------
#畫技術指標-
#WILLR

df.set_index('date', inplace = True)
print(abstract.WILLR(df))
abstract.WILLR(df).plot(ax=ax2,figsize=(16,8))         # WILLR 威廉指標 介紹
ax2.set_title("WILLR")
plt.show()



# MA5
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_excel('2330.xlsx', '2330')
#print(df.head())
#print(type(df))

df=df.rename(columns={"Close": "close", "Date": "date"})  #注意:  Ta-Lib ["close"]  ["date"]
print(df.head())
#--------------------------------
#設定index 為日期
df.set_index('date', inplace = True)                      #注意:  Ta-Lib 一定要指定時間
#print(df.head())
#--------------------------------
#畫收盤價
df['close'].plot(figsize=(16, 8), label='close')

#--------------------------------
##接著 TA-Lib 登場~~
from talib import abstract   # abstract  是 talib 裡面計算指標用的

# #SMA5 5天平均
#print(abstract.SMA(df,5))            # SMA5 5天平均一句指令就搞定~
#print(abstract.SMA(df,5).head(10))
t1=abstract.SMA(df,5)

abstract.SMA(df,5).plot(figsize=(16, 8), label='SMA5')

#--------------------------------
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.title('2330 Close')
plt.show()

#RSI
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from talib import abstract
import PKStock
import pandas as pd
df = pd.read_excel('2330.xlsx', '2330')
#print(df.head())
#print(type(df))

df=df.rename(columns={"Date": "date","Open": "open","High": "high","Low": "low","Close": "close","Volume":"volume"})
#--------------------------------
#設定index
#print(df.head())
#設定index為時間
df.set_index('date', inplace = True)

#--------------------------------
#畫技術指標-KD值
#用talib的abstract畫的RSI
print(abstract.RSI(df["close"],timeperiod=14))   #RSI 14筆
df['close'].plot(secondary_y=True, label='close', alpha = 0.2)#畫收盤價
abstract.RSI(df,timeperiod=14).plot(figsize=(16,8))
plt.title("RSI")
plt.show()

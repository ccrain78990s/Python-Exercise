#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "Powen Ko, www.powenko.com 柯博文老師"
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
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

df=df.rename(columns={"Date": "date","Open": "open","High": "high","Low": "low","Close": "close","Volume":"volume"})
#--------------------------------
print(df.head())


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
ax1.set_title("K線圖")
#--------------------------------
#畫技術指標-
#用talib的abstract畫的MACD

df.set_index('date', inplace = True)
print(abstract.MACD(df))
abstract.MACD(df).plot(ax=ax2,figsize=(16,8))
ax2.set_title("MACD")
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']
plt.show()



df['MACD'] = abstract.MACD(df)
print(df['MACD'].head())

#--------------------------------
# Create a function to signal when to buy and sell an asset
def buy_sell(signal,checkFiled):
    sigPriceBuy = []
    sigPriceSell = []
    total=0
    buyPrice=0
    flag = -1
    for i in range(0, len(signal)):
        # if sma30 > sma100  then buy else sell
        if signal['MACD'][i]  >0:
            if flag != 1:
                sigPriceBuy.append(signal[checkFiled][i])
                sigPriceSell.append(np.nan)
                flag = 1
                buyPrice=signal[checkFiled][i]
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
            # print('Buy')
        # elif signal[checkFiled][i]> buyPrice :
        elif signal['MACD'][i] < 0:
            if flag != 0:
                sigPriceSell.append(signal[checkFiled][i])
                sigPriceBuy.append(np.nan)
                flag = 0
                t獲利=signal[checkFiled][i]-buyPrice
                total=total+t獲利
                print("此獲利:", t獲利, "買價:", buyPrice, "賣價:", signal[checkFiled][i],"目前獲利:",total)
                buyPrice=0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
            # print('sell')
        else:  # Handling nan values
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    print("一共獲利:",total,"現在手上股票買價:",buyPrice)
    return (sigPriceBuy, sigPriceSell)


x = buy_sell(df,'close')
df['Buy_Signal_Price'] = x[0]
df['Sell_Signal_Price'] = x[1]



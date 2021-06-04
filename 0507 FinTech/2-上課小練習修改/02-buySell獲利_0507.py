#導入套件
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


from talib import abstract

import pandas as pd
df = pd.read_excel('2002.xlsx', '2002')
print(df.head())
print(type(df))

df=df.rename(columns={"Close": "close", "Date": "date"})
#--------------------------------
#設定index 為日期
#df.set_index('date', inplace = True)

print(df.head())

#--------------------------------
#畫收盤價
df['close'].plot(figsize=(16, 8), label='close')

# #SMA5 30天平均
df["SMA30"]=abstract.SMA(df,30)
print(df["SMA30"].head(50))

# #SMA5 100天平均
df["SMA100"]=abstract.SMA(df,100)
print(df["SMA100"].head(50))

#--------------------------------
# Create a function to signal when to buy and sell an asset
def buy_sell(signal,checkFiled):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1
    for i in range(0, len(signal)):
        # if sma30 > sma100  then buy else sell
        if signal['SMA30'][i] > signal['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(signal[checkFiled][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
            # print('Buy')
        elif signal['SMA30'][i] < signal['SMA100'][i]:
            if flag != 0:
                sigPriceSell.append(signal[checkFiled][i])
                sigPriceBuy.append(np.nan)
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
            # print('sell')
        else:  # Handling nan values
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return (sigPriceBuy, sigPriceSell)


x = buy_sell(df,'close')
df['Buy_Signal_Price'] = x[0]
df['Sell_Signal_Price'] = x[1]




# print(df)
#----------------------------------------------------------------

df2 = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])

print("----")
print(df2)
print("----")
print(df2[df2[1]==3])
print("----")
t1=pd.isnull(df2[1])
print(t1)
t1=pd.notnull(df2[1])
print(t1)
print("----")
print(df2[t1])


print("----------------------------------------------------------------")
print(type(df))
t_Buy=pd.notnull(df['Buy_Signal_Price'])
#print(t1)
print("----")
print("buy date")
print(df[t_Buy])

print("----------------------------------------------------------------")
print(type(df))
t_Sell=pd.notnull(df['Sell_Signal_Price'])
#print(t1)
print("----")
print("sell date")
print(df[t_Sell])

#--------------------------------
##計算獲利
print("----------------------------------------------------------------")
print("buy and sell date")
t_BuySell=df[t_Buy]
t_BuySell=t_BuySell.append(df[t_Sell])
# t_BuySell.set_index('date', inplace = True)
print(t_BuySell.head(5))
print(type(df))
#print(t_BuySell["date"])
#t_BuySell=t_BuySell.sort_index(by=['date'], ascending=True)
t_BuySell=t_BuySell.sort_values(by=['date'], ascending=True)

print(t_BuySell)

def CalculateProfit(df,Buy,Sell):
    print("----------------------------------------------------------------")
    currentPrice=-1
    profit=0
    for i in df.index:
        t1=df[Buy][i]
        if(math.isnan(t1)==False and currentPrice==-1):
            currentPrice=df[Buy][i]
            print("Buy price="+str(df[Buy][i])," date="+str(df["date"][i]))
        t2=df[Sell][i]
        if(math.isnan(t2)==False and currentPrice>-1):
            t3=currentPrice=df[Sell][i]-currentPrice
            profit=profit+currentPrice
            print("Sell price="+str(df[Sell][i])," date="+str(df["date"][i]) + " ,profit=" + str(t3)+" ,Total profit=" + str(profit))
            currentPrice=-1
    return profit,currentPrice
tProfit,currentPrice=CalculateProfit(t_BuySell,'Buy_Signal_Price','Sell_Signal_Price')
print("這段時間一共賺賠"+str(tProfit),"  目前手上持有的股票價格是:"+str(currentPrice))

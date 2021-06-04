#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "Powen Ko, www.powenko.com 柯博文老師"

import numpy as np
import math


#--------------------------------
# 找尋交叉時間
# FindCrossover(df,"close","SMA30","SMA100")
# 範例程式： 08_SMA30_100_buySell獲利_類別化.py
def FindCrossover(signal,checkFiled,iField1,iField2):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1
    for i in range(0, len(signal)):
        # if sma30 > sma100  then buy else sell
        if signal[iField1][i] > signal[iField2][i]:
            if flag != 1:
                sigPriceBuy.append(signal[checkFiled][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
            # print('Buy')
        elif signal[iField1][i] < signal[iField2][i]:
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

#--------------------------------
# 移除掉NAN 的資料
# 例如要處調 欄位 Buy_Signal_Price 和 Sell_Signal_Price 資料是NAN就整筆移除
# t1=PKStock.RemoveNanData(df,"date",'Buy_Signal_Price','Sell_Signal_Price'))
# print("買賣時間點"+str(t1))
# 範例程式： 08_SMA30_100_buySell獲利_類別化.py
def RemoveNanData(df,sort,*iField):
    import pandas as pd
    df_new = pd.DataFrame()
    for name in iField:
        t_Buy = pd.notnull(df[name])
        df_new = df_new.append(df[t_Buy])
    df_new = df_new.sort_values(by=[sort], ascending=True)
    return df_new
#--------------------------------
# 透過買賣訊號，計算出獲利
# tProfit=CalculateProfit(t_BuySell,'Buy_Signal_Price','Sell_Signal_Price')
# print("這段時間一共賺賠"+str(tProfit))
# 範例程式： 08_SMA30_100_buySell獲利_類別化.py
def CalculateProfit(df,Buy,Sell):
    BuyPrice=-1
    profit=0
    for i in df.index:
        t1=df[Buy][i]
        if(math.isnan(t1)==False and BuyPrice==-1):
            BuyPrice=df[Buy][i]
        t2=df[Sell][i]
        if(math.isnan(t2)==False and BuyPrice>-1):
            t3=currentPrice=t2-BuyPrice
            profit=profit+t3
            BuyPrice=-1
    return profit,BuyPrice

#--------------------------------
# 找尋止損點時間
# (sigStopLossPoint, df)=PKStock.FindStopLossPoint(df,'close','Buy_Signal_Price','Stop_Loss_Price',5)  #低過5％就賣
# 範例程式： 09_SMA30_100_buySell獲利_止損點.py
def FindStopLossPoint(df,closeField,buyField,StopLossField,StopLossPointPercentage):
    import pandas as pd
    #sigStopLossPoint = []
    buyPrice=-1
    checkPrice=-1
    flag = -1
    sigStopLossPoint= []
    for i in df.index:
        if(pd.notnull(df[buyField][i])):
            buyPrice=df[buyField][i]
        if(buyPrice>-1):
            checkPrice=buyPrice-((buyPrice*StopLossPointPercentage)/100)
            close=df[closeField][i]
            if(close<checkPrice):
                sigStopLossPoint.append(close)
                buyPrice = -1
                checkPrice = -1
                flag = -1
            else:
                sigStopLossPoint.append(np.nan)
        else:
            sigStopLossPoint.append(np.nan) # 資料不處理 NAN
    df[StopLossField]=sigStopLossPoint
    return (sigStopLossPoint, df)


#--------------------------------
# 合併欄位combine
# 用在當「止損」和「死亡交叉」同時要判斷
# (Sell_signal, df)=PKStock.combineColumns(df,'Sell_signal','Sell_Signal_Price','Stop_Loss_Price')
# 範例程式： 09_SMA30_100_buySell獲利_止損點.py
def combineColumns(df,TargetField,*iField):
    import pandas as pd
    Price=-1
    sigStopLossPoint= []
    for i in df.index:
        t_priceAll=-1
        for name in iField:
            t_price=-1
            if(pd.notnull(df[name][i])):
                t_price =df[name][i]
            if(t_price>t_priceAll):
                t_priceAll=t_price
        if(t_priceAll==-1):
            sigStopLossPoint.append(np.nan)
        else:
            sigStopLossPoint.append(t_priceAll)
    df[TargetField] = sigStopLossPoint
    return (sigStopLossPoint, df)
#--------------------------------
# 計算SMA
# 開始計算RSV值，使用 rolling(window=day) 畫出『移動平均線』，這裡後面加上 .min及 .max取區間最小(大)值
#(rsv, df)=PKStock.mathRSV(df,'close',9,'RSV')
# 範例程式： 12_K線D線.py
def mathSMA(df,closeField,iWindow,TargetField):
    SMA = df[closeField].rolling(window=iWindow).sum()/iWindow

    # 3. 因為 rolling 採用9天內的資料來計算，所以前8天不會有值，這裡用np.nan_to_num 的方法將前8筆改為 0，而資料自動轉成array型態
    # 把前8筆NaN改為0
    #rsv = np.nan_to_num(rsv)
    df[TargetField] = SMA
    return (SMA, df)
#--------------------------------
# 計算RSV
# 開始計算RSV值，使用 rolling(window=day) 畫出『移動平均線』，這裡後面加上 .min及 .max取區間最小(大)值
#(SMA10, df)=PKStock.mathSMA(df,'close',10,'SMA10')
# 範例程式： 12_K線D線.py
def mathRSV(df,closeField,iWindow,TargetField):
    rsv = (df[closeField] - df[closeField].rolling(window=iWindow).min()) / (
                df[closeField].rolling(window=iWindow).max() - df['close'].rolling(window=iWindow).min()) * 100

    # 3. 因為 rolling 採用9天內的資料來計算，所以前8天不會有值，這裡用np.nan_to_num 的方法將前8筆改為 0，而資料自動轉成array型態
    # 把前8筆NaN改為0
    #rsv = np.nan_to_num(rsv)
    df[TargetField] = rsv
    return (rsv, df)



#--------------------------------
# 計算K值
# 開始計算RSV值，使用 rolling(window=day) 畫出『移動平均線』，這裡後面加上 .min及 .max取區間最小(大)值
#(SMA10, df)=PKStock.mathSMA(df,'close',10,'SMA10')
# 範例程式： 12_K線D線.py
def mathK(df,closeField,iWindow,TargetField):
    # K值稱為快速平均值，反應較靈敏。D值稱為慢速平均值，反應較不靈敏。若K值大於D值，代表目前處於漲勢；相反地，當K值小於D值時，代表目前處於跌勢，一般來說，數值50被認為是多空平衡位置。大於50時，多方力道強；小於50時，空方力道強。
    # 80以上俗稱「超買區」，代表多頭強勢，買氣旺盛。
    # 20以下俗稱「超賣區」，代表空頭強勢，賣氣旺盛。
    # 創建KD值
    # 5. 開始創建K值，因前8筆 RSV 都沒有值，無法算出K值，所以我們給前8筆(k1)一個初始值a，用 append 添加8次
    # 創建K值

    import pandas as pd
    if 'A' in df.columns:
        t1=0
    else:
        (rsv, df) = mathRSV(df, 'close', iWindow, 'RSV')

    k1 = []
    day8=(iWindow-1)
    for a in range(day8):
        a = 50  # 74.02
        k1.append(a)
    k1 = pd.DataFrame(k1)
    k1.columns = ['K']
    #print(k1)
    # 6. 第9筆之後就可以開始計算，我們把結果放入k2，而一開始的初始值k_temp為a，用 append 添加 df長度的次數(df-8+8)
    k2 = []
    k_temp = a
    for i in range(len(df) - day8):
        # 當日K值=前一日K值 * 2/3 + 當日RSV * 1/3
        k_temp = k_temp * 2 / 3 + df['RSV'][i + day8] * (1 / 3)
        k2.append(k_temp)
    k2 = pd.DataFrame(k2)
    k2.columns = ['K']

    # 7. 用 concat 將k1、k2疊加起來
    K = pd.concat([k1, k2])

    # 8. 最後用老方法設定index，並加入到df的K欄位裡
    K.index = df['date'].index


    df[TargetField] = K
    return (K, df)


#--------------------------------
# 計算K值
# 開始計算RSV值，使用 rolling(window=day) 畫出『移動平均線』，這裡後面加上 .min及 .max取區間最小(大)值
#(SMA10, df)=PKStock.mathSMA(df,'close',10,'SMA10')
# 範例程式： 12_K線D線.py
def mathD(df,closeField,iWindow,TargetField):
    # K值稱為快速平均值，反應較靈敏。D值稱為慢速平均值，反應較不靈敏。若K值大於D值，代表目前處於漲勢；相反地，當K值小於D值時，代表目前處於跌勢，一般來說，數值50被認為是多空平衡位置。大於50時，多方力道強；小於50時，空方力道強。
    # 80以上俗稱「超買區」，代表多頭強勢，買氣旺盛。
    # 20以下俗稱「超賣區」，代表空頭強勢，賣氣旺盛。
    # 創建KD值
    # 5. 開始創建K值，因前8筆 RSV 都沒有值，無法算出K值，所以我們給前8筆(k1)一個初始值a，用 append 添加8次
    # 創建K值

    import pandas as pd
    if 'K' in df.columns:
        t1=0
    else:
        (rsv, df) = mathK(df, 'close', iWindow, 'RSV')

    # D值就用上述方法再做一次，公式記得要調整~
    # 創建D值
    d1 = []
    day8=iWindow-1
    for b in range(day8):
        b = 50  # 81.58
        d1.append(b)
    d1 = pd.DataFrame(d1)
    d1.columns = ['D']
    d2 = []
    d_temp = b
    for j in range(len(df) - day8):
        # 當日D值=前一日D值 * 2/3 + 當日K值 * 1/3
        # 0.3 , 0.18
        d_temp = d_temp * 2 / 3 + df['K'][j + day8] * (1 / 3)
        d2.append(d_temp)
    d2 = pd.DataFrame(d2)
    d2.columns = ['D']
    D = pd.concat([d1, d2])

    D.index = df['date'].index
    df['D'] = D['D']


    #print(D.head())
    #D.index = df['date'].index
    df['D'] = D
    #df.head(10)
    #print(df.head(50))

    # 8. 最後用老方法設定index，並加入到df的K欄位裡
    #D.index = df['date'].index
    #df[TargetField] = D['D']
    return (D, df)



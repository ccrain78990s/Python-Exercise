#導入套件
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#專門做『技術分析』的套件
# pip3 install TA-Lib
# 設定方法：
# Windows
# http://yhhuang1966.blogspot.com/2018/05/python-ta-lib.html
"""
下載 
https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
pip3 install TA_Lib-0.4.17-cp36-cp36m-win_amd64.whl 
注意 36 是python 3.6 的意思
"""
# Mac 安裝方法:
"""  
brew install ta-lib
pip install ta-lib
"""
#  樹梅派 安裝方法:
"""


$ wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.17-src.tar.gz 
$ tar -xvf ta-lib-0.4.17-src.tar.gz 
$ cd ta-lib   
$ ./configure --prefix=/usr 
$ sudo make   
$ sudo make install   
$ sudo pip3 install TA-Lib 
"""



import pandas as pd
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))
#*******************************遊戲規則:換小寫
df=df.rename(columns={"Close": "close", "Date": "date"})
#--------------------------------
#設定index 為日期******************
df.set_index('date', inplace = True)

print(df.head())

#--------------------------------
#畫收盤價
df['close'].plot(figsize=(16, 8), label='close')



#--------------------------------
##接著 TA-Lib 登場~~
from talib import abstract   # abstract  是 talib 裡面計算指標用的

# #SMA5 5天平均
print(abstract.SMA(df,5).head(10))      # 一句指令就搞定~


abstract.SMA(df,5).plot(figsize=(16, 8), label='SMA5')
abstract.SMA(df,10).plot(figsize=(16, 8), label='SMA10')
abstract.SMA(df,20).plot(figsize=(16, 8), label='SMA20')
abstract.SMA(df,60).plot(figsize=(16, 8), label='SMA60')
abstract.SMA(df,240).plot(figsize=(16, 8), label='SMA240')


#--------------------------------
plt.legend(loc='upper left', shadow=True, fontsize='x-large')
plt.title('AAPL Close')
plt.show()
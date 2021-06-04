#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"


import pandas as pd
onestock = pd.read_excel('2014.xlsx', '2014')
df = pd.read_excel('stocks.xlsx', 'stocks')
print(df.head())
print(type(df))
# 2
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
panel_data=df

print(panel_data.head())

start_date = '2010-01-01'
end_date = '2021-05-06'

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data['Close']

# Getting all weekdays between 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing prices in adj_close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)

# Reindexing will insert missing values (NaN) for the dates that were not present
# in the original set. To cope with this, we can fill the missing by replacing them
# with the latest available price for each instrument.
#close = close.fillna(method='ffill')
#close.fillna(method='ffill', inplace = True)


#print(all_weekdays)

#print(close.head(10))
#print(close.describe())

#--------------------------------------
# Get the MSFT timeseries. This now returns a Pandas Series object indexed by date.
#msft = close.loc[:, 'MSFT']

close=onestock['Close']

# Calculate the 20 and 100 days moving averages of the closing prices
short_rolling_msft = close.rolling(window=5).mean()   # 　SMA 　10筆 平均
long_rolling_msft = close.rolling(window=10).mean()  # SMA 100筆 平均



import matplotlib.pyplot as plt
# Plot everything by leveraging the very powerful matplotlib package
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(close.index, close, label='2014')
ax.plot(short_rolling_msft.index, short_rolling_msft, label='5 days rolling')
ax.plot(long_rolling_msft.index, long_rolling_msft, label='10 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()
plt.show()
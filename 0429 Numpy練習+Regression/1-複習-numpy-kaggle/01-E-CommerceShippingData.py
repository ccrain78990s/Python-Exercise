#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "Chen"
# 0429 小練習
import pandas as pd
import numpy as np

"""
資料來源:
https://www.kaggle.com/prachi13/customer-analytics

ID：客戶的ID號。
倉庫區：公司有大倉庫，分為A，B，C，D，E等區。
裝運方式：公司以多種方式裝運產品，例如船舶，飛行和公路。
客戶服務電話：從詢價到詢價的電話數量。
客戶評價：公司已對每個客戶進行了評價。1是最低的（最差），5是最高的（最好）。
產品成本：以美元表示的產品成本。
先前購買：先前購買的數量。
產品重要性：公司根據低，中，高等各種參數對產品進行了分類。
性別：男性和女性。
提供的折扣：針對該特定產品提供的折扣。
以克為單位的重量：以克為單位的重量。
準時到達：它是目標變量，其中1表示未按時到達產品，0表示已按時到達。
"""



# pandas 讀取檔案
df = pd.read_csv('Train.csv')
print(df.head())
print(type(df))
# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

# Pandas 轉 Numpy
np1=df.to_numpy()
print(np1)


# 2.什麼是客戶評價？產品按時交貨了嗎？
print("全部客戶評價:",np1[:,4])
print("平均客戶評價",np1[:,4].mean())
print("客戶評價中位數",np.median(np1[:,4]))
print("是否準時交貨資料",np1[:,11])
print("不準時交貨筆數",np.sum(np1[:,11]))
print("準時交貨筆數",10999-(np.sum(np1[:,11])))
print("準時交貨比率",1-np1[:,11].mean())
# 3.是否正在回答客戶查詢？
print("全部是否正在回答客戶查詢:",np1[:,3])
# 4.如果產品重要性高。擁有最高評價或準時交貨？
print("產品重要性高低",np1[:,7])
high_import=np1[np1[:,7]=='high']
print(high_import[high_import[:,4]==5])
print("產品重要性高時交貨率",np.mean(high_import[:,11]))
# 產品重要性高 最高評價5
print("產品重要性高 最高評價5",np1[(np1[:,4]==5) & (np1[:,7]=='high')])
# 產品重要性中 最高評價5
print("產品重要性中 最高評價5",np1[(np1[:,4]==5) & (np1[:,7]=='medium')])
# 產品重要性低 最高評價5
print("產品重要性低 最高評價5",np1[(np1[:,4]==5) & (np1[:,7]=='low')])


(unique, counts) = np.unique(np1[:,7]=='high', return_counts=True)
frequencies = np.asarray((unique, counts)).T
print("產品重要性_高_次數",frequencies[1][1])
(unique, counts) = np.unique(np1[:,7]=='medium', return_counts=True)
frequencies = np.asarray((unique, counts)).T
print("產品重要性_中_次數",frequencies[1][1])
(unique, counts) = np.unique(np1[:,7]=='low', return_counts=True)
frequencies = np.asarray((unique, counts)).T
print("產品重要性_低_次數",frequencies[1][1])


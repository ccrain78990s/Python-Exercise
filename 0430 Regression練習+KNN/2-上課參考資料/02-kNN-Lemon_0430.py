#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

X=[[9,9],[9.2,9.2],[9.6,9.2],[9.2,9.2],[6.7,7.1],[7,7.4],[7.6,7.5],
   [7.2,10.3], [7.3,10.5], [7.2,9.2], [7.3,10.2], [7.2,9.7], [7.3,10.1], [7.3,10.1]]
y=[1,1,1,1,1,1,1,
   2,2,2,2,2,2,2]
# ↑ 資料要對齊唷 Y建議從0開始 0,1

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)        # 沒寫的話 預設5

neigh.fit(X, y)
print("預測答案＝",neigh.predict([[7,9],[9,10]]))
print("預測樣本距離＝",neigh.predict_proba([[7,9],[9,10]]))   # 測試數據X的返回概率估計。 (X為類別1的機率 X為類別2的機率)
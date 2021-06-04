#!/usr/bin/env python
# -*- coding=utf-8 -*-
# 0422 練習
__author__ = "Chen"

"""
sno(站點代號)、sna(場站中文名稱)、tot(場站總停車格)、sbi(場站目前車輛數量)、
sarea(場站區域)、mday(資料更新時間)、lat(緯度)、lng(經度)、ar(地點)、
sareaen(場站區域英文)、snaen(場站名稱英文)、aren(地址英文)、
bemp(空位數量)、act(全站禁用狀態)、srcUpdateTime、updateTime、infoTime、infoDate
"""

import pandas as pd
import json
from pandas import json_normalize
# 調整顯示樣子
from IPython.display import display
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
#顯示所有列
pd.set_option('display.max_columns', None)
#顯示所有行
pd.set_option('display.max_rows', None)
#設置value的顯示長度為100，默認為50
pd.set_option('max_colwidth',50)
#pd.set_option('display.width', None)

df = pd.read_json('https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f')
#print(df.head(10))
print(df.head(5))
print(type(df))
print(df.index)
df = json_normalize(df['retVal']) #Results contain the required data
print(df.head(5))
#print(df[['sbi','tot']])

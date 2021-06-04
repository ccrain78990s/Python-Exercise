#!/usr/bin/env python
# -*- coding=utf-8 -*-
# 0422練習
__author__ = "Chen"
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
from IPython.display import display
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',50)
#pd.set_option('display.width', None)

df = pd.read_excel('106學年國民小學學生裸眼視力檢查報表.xls', '報表程式')   ###
print("====練習1====")
print(df.head(50))
print(df.info())
"""
from pandas import ExcelWriter
writer = ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='noahtest')
writer.save()
"""
print("====練習2====")
print(df[['公立檢查人數','公立視力不良','公立視力不良率']] )
print("====練習3====")
print(df[['性別及年級別','公立檢查人數','公立視力不良','公立視力不良率']][15:18] )
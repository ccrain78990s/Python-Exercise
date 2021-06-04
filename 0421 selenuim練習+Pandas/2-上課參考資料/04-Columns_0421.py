# -*- coding: utf-8 -*-

__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import pandas as pd
import numpy as np
DataFrame = pd.read_csv('ExpensesRecord.csv')
print("======")
print(DataFrame["說明"])
print("======")
print(DataFrame["消費縣市"])
print("======")
print(DataFrame["支出方法"])
print("======")
print(DataFrame[["說明","支出金額"]] )
print("======")
print(DataFrame["說明"][2])
print(DataFrame["說明"][9])
print("======")
print(DataFrame["說明"][1:5])
print("======")
print("===切割練習1===")
print(DataFrame["支出金額"][2:8])       # 110~280
print("===切割練習2===")
print(DataFrame["支出金額"][22:29])     # 104~15
print("===切割練習3===")
print(DataFrame["支出金額"][22])        # 104
print("===切割練習4===")
print(DataFrame[["說明","支出金額"]][3:5])
print("===補充===")
t1=DataFrame[["說明","支出金額"]]
print(t1[0:1][0:])

print("======")
df = pd.DataFrame({'Math': [90, 91,92, 93, 94],'English': np.arange(80,85,1) })
print(df[["Math","English"]])


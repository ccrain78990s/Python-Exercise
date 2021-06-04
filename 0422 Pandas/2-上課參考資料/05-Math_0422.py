# -*- coding: utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import pandas as pd
DataFrame = pd.read_csv('ExpensesRecord.csv')
DataFrame["單價"]=DataFrame["支出金額"]/DataFrame["數量"]
print(DataFrame[["數量","單價","支出金額"]] )

# 美金版本的
# 日幣版本的
print("=====練習=====")
DataFrame["美金價格"]=DataFrame["支出金額"]/28.06
DataFrame["日幣價格"]=DataFrame["支出金額"]/0.26
print(DataFrame[["數量","單價","支出金額","美金價格","日幣價格"]] )

#DataFrame.to_csv('ExpensesRecord2.csv')
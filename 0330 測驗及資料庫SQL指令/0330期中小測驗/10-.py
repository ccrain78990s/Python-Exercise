#!/usr/bin/env
__author__ = "Chen"

import matplotlib.pyplot as plt
import csv

with open('opendata10706L010.csv', 'r',encoding="utf-8") as fin:
        read = csv.reader(fin, delimiter=',')
        header = next(read)   # 讀擋頭
        print(header)
        GPS=next(read)        # 讀 GPS
        x=0
        for row in read:

            if row[2]=="陳":
                print("區域別:",row[1],"姓氏:",row[2],"性別:",row[3],"人口數:",row[4])

            #plt.plot(int(x), float(row[1]), 'ro',label="")
            x=x+1



# 1. 印出所有資料




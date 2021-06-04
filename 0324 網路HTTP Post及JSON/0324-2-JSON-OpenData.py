#!/usr/bin/env python
# -*- coding=utf-8 -*-
import json
import matplotlib.pyplot as plt

# Reading data back
with open('桃園公共自行車即時服務資料.json', 'r',encoding="utf-8") as f:
    # str1=f.read()
    data = json.load(f)

print(data)
# 第一題
print("===第一題===")
# "sna" : "中央大學圖書館"
print(data['retVal']['2001']['sna'])
# "tot" : "60"
print(data['retVal']['2001']['tot'])
# "sbi" : "24"
print(data['retVal']['2001']['sbi'])
# 第二題
# 迴圈把所有的sna tot sbi 印出來
print("===第二題===")
d=data['retVal']

for year in d:
    info=d[year]
    sna=info['sna']
    tot=info['tot']
    sbi=info['sbi']

    print('站名: %s 總停車格: %s 可借車位數: %s'
          % (sna,tot,sbi))

# 第三題:
#   迴圈把所有的  如果剩下的車輛,少於一半  印出來
print("===第三題===")
d=data['retVal']

for year in d:
    info=d[year]
    sna=info['sna']
    tot=info['tot']
    sbi=info['sbi']
    if int(sbi) < (int(tot)*0.5):
        print('站名: %s 總停車格: %s 可借車位數: %s' % (sna,tot,sbi),"車輛少於一半")

# 第四題:
# matplot lib
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py
print("===第四題===")
import matplotlib.pyplot as plt
# ↓顯示中文方法
from matplotlib.font_manager import FontProperties # 步驟一

plt.rcParams['font.sans-serif'] = ['SimSun'] # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

listSna=[]
listTot=[]
listSbi=[]
listBemp=[]

d=data['retVal']

for year in d:
    info=d[year]
    sna=info['sna']
    listSna.append(str(sna))
    tot=info['tot']
    listTot.append(int(tot))
    sbi=info['sbi']
    listSbi.append(int(sbi))
    bemp=info['bemp']
    listBemp.append(int(bemp))


labels = listSna
sbi_means = listSbi
bemp_means = listBemp



fig, ax = plt.subplots()

ax.bar(labels, sbi_means, label='sbi 可借數量')
ax.bar(labels, bemp_means, bottom=sbi_means,
       label='bemp 已借走數量')

ax.set_ylabel('Quantity')
ax.set_title('sbi & bemp')
ax.legend()

plt.show()


# 參數說明 http://www-ws.gov.taipei/001/Upload/public/mmo/dot/YouBike_JSON%E6%AA%94%E6%A1%88%E8%AA%AA%E6%98%8E(%E4%BF%AE%E6%AD%A3%E7%89%88)_%E5%B1%80%E7%B6%B2.pdf

"""
參數 參數定義 參數別解
"sno" 站點代號 同左
"sna" 場站名稱(中文) 同左
"tot" 場站總停車格 同左
"sbi" 場站目前車輛數量 可借車位數
"sarea" 場站區域(中文) 同左
"mday" 資料更新時間 同左
"lat" 緯度 同左
"lng" 經度 同左
"ar" 地址(中文) 同左
"sareaen" 場站區域(英文) 同左
"snaen" 場站名稱(英文) 同左
"aren" 地址(英文) 同左
"bemp" 空位數量 可還車位數
"act" 全站禁用狀態 場站暫停營運

"""
#!/usr/bin/env python
# -*- coding=utf-8 -*-
# 0325 複習
"""
參考資料:

https://data.tycg.gov.tw/opendata/datalist/datasetMeta/outboundDesc?id=88bdf93f-1b8d-4e8d-ade5-16670d909f38&rid=0c7bcfbf-b151-4411-b888-9ff685ff7a75
"""
"""

項次(項次)、清運序(清運序)、行政區(行政區)、清運路線名稱(清運路線名稱)、清運點名稱(清運點名稱)、
一般垃圾清運時間(一般垃圾清運時間)、廚餘回收清運時間(廚餘回收清運時間)、資源回收清運時間(資源回收清運時間)

"""

import json
import sys

try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

import ssl
context = ssl._create_unverified_context()

url="https://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json"
req=httplib.Request(url)

try:
    reponse = httplib.urlopen(req, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read().decode("utf-8")
            print(contents)
        else:
            contents = reponse.read()
        data = json.loads(contents)


except:                                                                 #  處理網路連線異常
    print("error")

print(data['result']['records'])
print(data['result']['records'][0]['清運點名稱'])


print("===所有公車輛數===")
t1=len(data['result']['records'])
print(t1)

print("===全部公車資料===")
x=0
while x < t1:
    print("車ID:", data['result']['records'][x]['_id'],
          "清運點路線:", data['result']['records'][x]['清運路線名稱'],
          "清運點:", data['result']['records'][x]['清運點名稱'],
          "一般垃圾清運時間:", data['result']['records'][x]['一般垃圾清運時間'],
          "資源回收清運時間:", data['result']['records'][x]['資源回收清運時間'],
          "廚餘回收清運時間:", data['result']['records'][x]['廚餘回收清運時間'],)
    x=x+1

print("===今天可以到垃圾的日子***===")
import time,datetime
def get_week_day(date):
    week_day_dict=\
       {
        0:'一',
        1: '二',
        2: '三',
        3: '四',
        4: '五',
        5: '六',
        6: '日'
                }
    day=date.weekday()
    return week_day_dict[day]
from datetime import datetime
now = datetime.now()            #現在時間
week=get_week_day(now)
print("現在: 星期",week)
current_time = now.strftime("%Y-%m-%d  %H:%M")
print("現在時間 :", current_time)


t1=len(data['result']['records'])
x=0
while x < t1:
    txt = data['result']['records'][x]['一般垃圾清運時間']
    position = txt.find(week)

    if position > 0:
        print("車ID:", data['result']['records'][x]['_id'],
              "清運點路線:", data['result']['records'][x]['清運路線名稱'],
              "清運點:", data['result']['records'][x]['清運點名稱'],
              "一般垃圾清運時間:", data['result']['records'][x]['一般垃圾清運時間'],
              "資源回收清運時間:", data['result']['records'][x]['資源回收清運時間'],
              "廚餘回收清運時間:", data['result']['records'][x]['廚餘回收清運時間'],)
    x=x+1
#加上時間(幾點幾分) ?
#加上經緯度(找哪裡最近 ?
#
#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
"""
Mac 的使用者　如果出現　SSL Certificate Error
請執行以下的程式，HTTPS 就能工作
/Applications/python 3.6/Install Certificates.command
"""

import json
import sys
import datetime

try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

import ssl
context = ssl._create_unverified_context()

url="http://data.taipei/opendata/datalist/datasetMeta/download?id=ea732fb5-4bec-4be7-93f2-8ab91e74a6c6&rid=bf073841-c734-49bf-a97f-3757a6013812"
url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
req=httplib.Request(url)
try:
    reponse = httplib.urlopen(req, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read();
        else:
            contents = reponse.read()
        data = json.loads(contents)

        # 紀錄更新時間
        time = datetime.datetime.now()
        print("更新時間:" + str(time.hour) + ":" + str(time.minute))



        start_time = datetime.datetime.strptime(str(time.date()) + '9:30', '%Y-%m-%d%H:%M')
        end_time = datetime.datetime.strptime(str(time.date()) + '13:30', '%Y-%m-%d%H:%M')

        # 判斷爬蟲終止條件
        if time >= start_time and time <= end_time:
            s.enter(1, 0, stock_crawler, argument=(targets,))

        if (len(data)>1):
            with open('桃園公共自行車即時服務資料-更.json', 'w') as f:
                json.dump(data, f)

except:                                                                 #  處理網路連線異常
    print("error")

with open('桃園公共自行車即時服務資料-更.json', 'r',encoding="utf-8") as f:
    # str1=f.read()
    data = json.load(f)


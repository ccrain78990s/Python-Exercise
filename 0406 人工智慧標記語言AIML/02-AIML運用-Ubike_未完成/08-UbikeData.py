#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "CHEN"


import json
import sys 
import urllib.request as httplib  # 3.x
import ssl
from datetime import datetime


sna="中壢火車站"
if len(sys.argv)>1:
    sna=sys.argv[1]


context = ssl._create_unverified_context()
url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
req = httplib.Request(url)
try:
    reponse = httplib.urlopen(req, context=context)
    if reponse.code==200:
        contents = reponse.read() #.decode("UTF-8")
        #print(contents)
        data = json.loads(contents)
        if(len(data)>1):                        # 確認是否有資料
            now = datetime.now()  # 現在時間
            current_time = now.strftime("%Y%m%d%H%M%S")  # 印出時間的格式
            print("現在時間 =", current_time)
            with open('c:\\桃園自行車'+str(current_time)+'.json', 'w') as f:   # 處存
                json.dump(data, f)

        t1 = data["retVal"]
        for t2 in t1:
            t_sna = t1[t2]["sna"]
            # print(t_sna, sna,t2)
            if t_sna.find(sna) >= 0:
                print("位置:", t1[t2]["sna"], " tot:", t1[t2]["sna"], " sbi:", t1[t2]["sbi"])

except:                                         #  處理網路連線異常
        print("error")


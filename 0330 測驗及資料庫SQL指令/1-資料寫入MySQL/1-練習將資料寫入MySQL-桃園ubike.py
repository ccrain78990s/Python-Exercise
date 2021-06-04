#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "chen # JSON檔案"
"""
Mac 的使用者　如果出現　SSL Certificate Error
請執行以下的程式，HTTPS 就能工作
/Applications/python 3.6/Install Certificates.command
"""

import json
import sys 
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

# 連接資料庫MySQL
import pymysql as MySQLdb             #  pip install MySQLdb
db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

import ssl
context = ssl._create_unverified_context()

url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
req=httplib.Request(url)
try:
        reponse = httplib.urlopen(req, context=context)
        if reponse.code == 200:
            if (sys.version_info > (3, 0)):
                contents = reponse.read()
            else:
                contents = reponse.read()
            data = json.loads(contents)
            print(data)






            print("=====第二題：　顯示全部的=======")
            print(len(data["retVal"]))   # 有幾筆的資料

            d=data["retVal"]
            for id in d:        #修改此處
                """
                print("中文場站名稱:", data["result"]["records"][x]["項次"],
                      ",清運序:", data["result"]["records"][x]["清運序"],
                      ",行政區", data["result"]["records"][x]["行政區"],
                      ",清運路線名稱:", data["result"]["records"][x]["清運路線名稱"],
                      ",清運點名稱:", data["result"]["records"][x]["清運點名稱"],
                      ",一般垃圾清運時間:", data["result"]["records"][x]["一般垃圾清運時間"],
                      ",廚餘回收清運時間:", data["result"]["records"][x]["廚餘回收清運時間"],
                      ",資源回收清運時間:", data["result"]["records"][x]["資源回收清運時間"])
                """
                a=d[id]["sna"]
                b=d[id]["tot"]
                c=d[id]["sbi"]
                d1=d[id]["lat"]
                e=d[id]["lng"]
                f=d[id]["bemp"]
                g=d[id]["act"]
                h=d[id]["sno"]
                i=d[id]["sarea"]
                j=d[id]["mday"]
                k=d[id]["ar"]
                l=str(d[id]["sareaen"]).replace("'","-")        #
                m=str(d[id]["snaen"]).replace("'","-")
                n=str(d[id]["aren"]).replace("'","-")
                #將資料寫入你的資料庫
                sql="INSERT INTO `ubiketaoyuan` (`id`, `sna中文場站名稱`, `tot場站總停車格`, `sbi可借車位數`, `lat緯度`, `lng經度`, `bemp可還空位數`, `act場站是否暫停營運`, `sno站點代號`, `sarea中文場站區域`, `mday資料更新時間`, `ar中文地址`, `sareaen英文場站區域`, `snaen英文場站名稱`, `aren英文地址`, `datetime`) VALUES (NULL, '"+a+"', '"+b+"', '"+c+"', '"+d1+"', '"+e+"', '"+f+"', '"+g+"', '"+h+"', '"+i+"', '"+j+"', '"+k+"', '"+l+"', '"+m+"', '"+n+"', now());"

                print(sql)
                cursor.execute(sql)     # 執行
                db.commit()             # 送出
                #exit()


except:                                         #  處理網路連線異常
        print("error")






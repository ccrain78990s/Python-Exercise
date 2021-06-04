#!/usr/bin/env python
# -*- coding=utf-8 -*-
             #  pip install MySQLdb

import json
import sys

try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

import pymysql as MySQLdb
db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

import ssl
context = ssl._create_unverified_context()


url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=b3abedf0-aeae-4523-a804-6e807cbad589&rid=bf55b21a-2b7c-4ede-8048-f75420344aed"
url="http://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json"
url="https://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json&offset=100" # 由第幾筆開始
url="https://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json&limit=800" # 最大資料量800筆
url="https://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json&limit=6000" # 最大資料量6000筆
req=httplib.Request(url)
try:
    reponse = httplib.urlopen(req, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read()
        else:
            contents = reponse.read()
        data = json.loads(contents)
        print(data)

        sql = "DELETE  FROM `rubbishcartable` "
        cursor.execute(sql)
        db.commit()

        length=len(data["result"]["records"])
        x=0
        while x<length:
            a=data["result"]["records"][x]["項次"]
            b=data["result"]["records"][x]["清運序"]
            c=data["result"]["records"][x]["行政區"]
            d=data["result"]["records"][x]["清運路線名稱"]
            e=data["result"]["records"][x]["清運點名稱"]
            f=data["result"]["records"][x]["一般垃圾清運時間"]
            g=data["result"]["records"][x]["廚餘回收清運時間"]
            h=data["result"]["records"][x]["資源回收清運時間"]

            sql = "INSERT INTO `rubbishcartable` (`id`, `Item`, `Preface`, `District`, `ClearRoute`, `SpotName`, `GeneralGarbageTime`, `FoodWasteTime`, `GarbageRecycleTime`) VALUES (NULL, '" + a + "', '" + b + "', '" + c + "', '" + d + "', '" + e + "', '" + f + "', '" + g + "', '" + h + "');"
            cursor.execute(sql)
            db.commit()

            x=x+1

except:
  print("error")
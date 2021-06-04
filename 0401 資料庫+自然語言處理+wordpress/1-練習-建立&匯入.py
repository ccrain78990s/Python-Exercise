#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import json
import sys
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x
    import ssl
    import urllib.request

try:
 import MySQLdb                         # pip install MySQL-python
except:
 import pymysql as MySQLdb             #  pip install MySQLdb
db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

import matplotlib.pyplot as plt

"""
資料來源:
公園基本資料
https://data.taipei/#/dataset/detail?id=ea732fb5-4bec-4be7-93f2-8ab91e74a6c6

pm_name(公園名稱)、pm_overview(公園概述)、pm_lon (經度)、pm_lat( 緯度)、pm_unit(管理單位)、
pm_construction(建造年度)、pm_location(公園位置)、pm_area(公園面積)、pm_opening_s(開放時間-開始)、
pm_opening_e(開放時間-結束)、pm_libie(里別)、pm_phone(聯絡電話)、pm_sports(體健設施)、
pm_recreation(遊樂設施)、pm_service(服務設施)、pm_other(古蹟設施)、pm_transit(交通資訊)、
pm_name_eng(公園英文名稱)、pm_ecology(是否為生態公園)、pm_type(類別)

"""

url="https://parks.taipei/parks/api/"

req=httplib.Request(url)
try:
    context = ssl._create_unverified_context()  #<----
    reponse = httplib.urlopen(url, context=context)  #<----
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
                #contents=reponse.read().decode(reponse.headers.get_content_charset())
                contents=reponse.read().decode("utf-8")
                print(contents)
                #contents=contents.replace("\r\n", "")
                #print(contents)
        else:
                contents=reponse.read()
        data = json.loads(contents)
        #print(data[0]["pm_name"])
        #print(data[3]["pm_name"])


        for data2 in data:
            str1 = "INSERT INTO `park`(`id`, `pm_name`, `pm_overview`, `pm_location`, `pm_lon`, `pm_lat`)" + \
                   " VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]')"
            str1 = str1.replace("[value-1]", "null")
            str1 = str1.replace("[value-2]", str(data2["pm_name"]))
            str1 = str1.replace("[value-3]", str(data2["pm_overview"]))
            str1 = str1.replace("[value-4]", str(data2["pm_location"]))
            str1 = str1.replace("[value-5]", str(data2["pm_lon"]))
            str1 = str1.replace("[value-6]", str(data2["pm_lat"]))
            #print(str1)
            cursor.execute(str1)
            # print("公園名稱:",data2['pm_name'],"公園介紹:",data2['pm_overview'],"公園地址:",data2['pm_location'],"經度:",data2['pm_lon'],"緯度:",data2['pm_lat'])
        db.commit()
        db.close()



except:     #  處理網路連線異常
    print("error")







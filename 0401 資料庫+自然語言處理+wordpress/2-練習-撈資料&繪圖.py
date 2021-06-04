#!/usr/bin/env
# -*- coding: utf-8 -*-
__author__ = "Chen"

import pymysql as MySQLdb             #  pip install MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()
# 從SQL撈資料畫圖
import matplotlib.pyplot as plt

list1=[]
list2=[]
list3=[]


sql2 = "SELECT * FROM `park`  "  # 不准用SQL的 max() ,不能用　order by
cursor.execute(sql2)
result = cursor.fetchall()

print(len(result))
for record in result:
    print("id:",record[0],"名稱:",record[1],"簡介:" ,record[2],"地址:" ,record[3],
          "經度:" ,record[4],"緯度:" ,record[5])
    list1.append(record[0])  # id
    list2.append(float(record[4]))  # 經度
    list3.append(float(record[5]))  # 緯度


#做圖
plt.scatter(list2, list3, alpha=0.6)
#設定圖示的
plt.legend(scatterpoints=1, markerscale=0.2)
#視覺化標題跟xy軸名稱
plt.title('Park Location', fontsize = 25)
plt.xlabel('Lon')
plt.ylabel('Lat')
plt.xlim(121.45,121.63)
plt.ylim(24.95,25.2)
plt.show()
#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
try:
 import MySQLdb                         # pip install MySQL-python
except:
 import pymysql as MySQLdb             #  pip install MySQLdb


db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

#sql="INSERT INTO mytable (value01, value02, value03,value04) VALUES ('1','1','1','1');"
#cursor.execute(sql)
#db.commit()

#
cursor.execute("SELECT * FROM ubiketaoyuan ")
result = cursor.fetchall()
print(result[1][1],result[1][2],result[1][3])

for record in result:
    print("sna=%s tot=%s" %(record[1],record[2]))

total=0
for record in result:
    total=total+record[2]

print("total=",total)

#
cursor.execute("SELECT * FROM `ubiketaoyuan` WHERE `sarea中文場站區域`='中壢區' ")
result2 = cursor.fetchall()
for record in result2:
    print("sna=%s sarea=%s" %(record[1],record[9]))

total=0
for record in result2:
    total=total+record[2]

print("中壢區total=",total)

#
cursor.execute("SELECT * FROM `ubiketaoyuan` WHERE `ar中文地址` LIKE '健行%' ")
result3 = cursor.fetchall()
for record in result3:
    print("sna=%s ar=%s" %(record[1],record[11]))
#
cursor.execute("SELECT DISTINCT `sarea中文場站區域` FROM `ubiketaoyuan` ")
result4 = cursor.fetchall()
for record in result4:
    print("每一區名稱=%s" % record[0])

# ****
print("======第4題======")
cursor.execute("SELECT DISTINCT `sarea中文場站區域` FROM `ubiketaoyuan` ")
result5 = cursor.fetchall()
for record in result5:
    print("每一區名稱=%s" % record[0])
    sql ="SELECT * FROM `ubiketaoyuan` WHERE `tot場站總停車格` > 10 and `sarea中文場站區域`='"+record[0]+"'"
    cursor.execute(sql)
    result6 = cursor.fetchall()
    for record2 in result6:
        print("站名:",record2[1],"總數量:",record2[2])
# ****
print("======第5題======")
cursor.execute("SELECT DISTINCT `sarea中文場站區域` FROM `ubiketaoyuan` ")
result5 = cursor.fetchall()
for record in result5:
    print("區名稱=%s" % record[0])
    sql ="SELECT * FROM `ubiketaoyuan` WHERE `sarea中文場站區域`='"+record[0]+"'"
    maxtot=0
    maxData=0
    cursor.execute(sql)
    result6 = cursor.fetchall()
    for record2 in result6:
        if record2[2] > maxtot:  #找最大
            maxData=record2
            maxtot=record2[2]
    print("數量最多站名:",maxData[1],"總數量:",maxData[2])

# **** ORDER BY 寫法  垃圾車
print("====垃圾車====")
cursor.execute("SELECT DISTINCT `District` FROM `rubbishcartable` ")
result = cursor.fetchall()
for record in result:
    print("區名稱=%s" % record[0])
    sql ="SELECT * FROM `rubbishcartable` WHERE `District`='"+record[0]+"' ORDER BY `Item` DESC"
    cursor.execute(sql)
    result2 = cursor.fetchall()
    for record2 in result2:
        print("數量最多站名:",record2[5],"ITEM:",record2[2])
        break;
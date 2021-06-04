#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
try:
 import MySQLdb                         # pip install MySQL-python
except:
 import pymysql as MySQLdb             #  pip install MySQLdb


db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
#db = MySQLdb.connect(host="172.19.107.140", user="powenko", passwd="powenko", db="mydatabase")   # 寫進別人的
cursor = db.cursor()

#INSERT
#sql="INSERT INTO mytable (value01, value02, value03,value04) VALUES ('2','2','2','2');"
#sql2="INSERT INTO `mytable` (`id`, `value01`, `value02`, `value03`, `value04`) VALUES (NULL, 'a', 'b', 'c', 'd');"
sql3="INSERT INTO `ubiketaoyuan` (`id`, `sna中文場站名稱`, `tot場站總停車格`, `sbi可借車位數`, `lat緯度`, `lng經度`, `bemp可還空位數`, `act場站是否暫停營運`, `sno站點代號`, `sarea中文場站區域`, `mday資料更新時間`, `ar中文地址`, `sareaen英文場站區域`, `snaen英文場站名稱`, `aren英文地址`, `datetime`) VALUES (NULL, '皮癢癢', '', '', '', '', '', '', '', '', '', '', '', '', '', '2021-03-31 05:13:33.000000');"
#cursor.execute(sql)  #執行新增資料
#cursor.execute(sql2)
cursor.execute(sql3)
db.commit()         #送出
#update
sql4="UPDATE `ubiketaoyuan` SET `sna中文場站名稱`='ChuChu' WHERE `sna中文場站名稱`='皮癢癢'"
cursor.execute(sql4)
db.commit()
#delete
sql5="DELETE FROM `ubiketaoyuan` WHERE `sna中文場站名稱`='柯南'"
cursor.execute(sql5)
db.commit()


db.close()  #斷線
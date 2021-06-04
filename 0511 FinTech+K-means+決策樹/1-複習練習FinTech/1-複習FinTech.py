try:
 import MySQLdb                         # pip install MySQL-python
except:
 import pymysql as MySQLdb             #  pip install MySQLdb


import sys
#import urllib.request as httplib  # 3.x
#import ssl

# 資料庫連結
db = MySQLdb.connect(host="172.19.107.140", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

"""
DataType=""
level="優"
# print(len(sys.argv))
if len(sys.argv)>1:
    level=sys.argv[1]
if len(sys.argv)>2:
    DataType=sys.argv[2]
"""


print("======第1題======")
cursor.execute("SELECT * FROM 行情報價 ")
result = cursor.fetchall()
#print(result[1][1],result[1][2],result[1][3])

for record in result:
    print("id=%s 股票代碼=%s 股票名稱=%s 成交價=%s" %(record[0],record[1],record[2],record[3]))

print("======第2題======")
cursor.execute("SELECT * FROM 行情報價 ORDER BY `id` DESC LIMIT 5")
result = cursor.fetchall()
#print(result[1][1],result[1][2],result[1][3])

for record in result:
    print("id=%s 股票代碼=%s 股票名稱=%s 成交價=%s" %(record[0],record[1],record[2],record[3]))
print("======第3題======")
cursor.execute("SELECT * FROM 行情報價 ORDER BY `id` DESC LIMIT 10")
result = cursor.fetchall()
#print(result[1][1],result[1][2],result[1][3])

for record in result:
    print("id=%s 股票代碼=%s 股票名稱=%s 成交價=%s" %(record[0],record[1],record[2],record[3]))

print("======第4題======")
cursor.execute("SELECT `成交價` FROM `行情報價` ")
result2 = cursor.fetchall()

for record in result2:
    print("成交價=%s " %(record[0]))
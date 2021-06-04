# import requests
from bs4 import BeautifulSoup
import os.path
from os import path
import urllib.request as httplib  # 3.x
import json

target="成交量前二十名證券"
date=20210416


filename=str(target)+str(date)+'.jason'
url = "https://www.twse.com.tw/exchangeReport/MI_INDEX20?response=json&date="+str(date)+"&_=1618561308607"
if path.exists(filename)==False:    # 是否有  'workfile.txt'檔案

    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
    # req = requests.get(url, headers=headers)
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    req=httplib.Request(url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
    })
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        contents = reponse.read().decode(reponse.headers.get_content_charset())
        # contents = reponse.read().decode("utf-8")
        # contents = reponse.read()
        print(contents)
        fr = open(filename, 'w',encoding="UTF-8")
        fr.write(contents)
        fr.close()

with open(filename, mode='r',encoding="UTF-8") as f:
    # str1=f.read()
    data = json.load(f)
    
#print(data)
#print(data['title'])
#print(data['data'])
print(str(date)+"成交量前二十名證券")
for x in data['data']:
    print("排名",x[0])
    print("證券代號",x[1],"證券名稱", x[2])
    print("成交股數", x[3],"成交筆數",x[4])
    print("開盤價", x[5], "最高價", x[6], "最低價", x[7], "收盤價", x[8])
    x[9]=x[9].replace("<span style='color:green'>","")
    x[9] = x[9].replace("<span style='color:red'>", "")
    x[9]=x[9].replace("</span>","")
    print("+/-", x[9], "漲跌價差", x[10])
    print("最後揭示買價", x[11],  "最後揭示賣價", x[12])
    print(" ")

"""
soup=BeautifulSoup(all_of_it.encode('utf-8'), "html.parser")
t1=soup.select('.listBlk') # class="listBlk horizontal"
t2=t1[0].select(".txt") # class="txt"
print(t2)
for listRight in t2:
     print("標題:",listRight.contents[1].contents[0]) 
     print("內容:",listRight.contents[3].contents[0])
"""
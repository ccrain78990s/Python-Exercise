# import requests
from bs4 import BeautifulSoup
import os.path
from os import path
import urllib.request as httplib  # 3.x
import json

target="三大法人買賣超日報"
date=20210415
selectType=24

filename=str(target)+str(date)+str(selectType)+'.jason'
url = "https://www.twse.com.tw/fund/T86?response=json&date="+str(date)+"&selectType="+str(selectType)+"&_=1618556546771"
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
for x in data['data']:
    print("證券代號",x[0])
    print("證券名稱", x[1])
    print("三大法人買賣超股數", x[18])
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
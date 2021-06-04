# -*- coding: UTF-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

# pip install beautifulsoup4

import requests                     # 有別種寫法
from bs4 import BeautifulSoup       #

#req=requests.get('http://www.powenko.com/wordpress/')
req=requests.get('https://forum.gamer.com.tw/B.php?bsn=34173')
print(req.text)                     #先印出來確認有沒有抓到資料
print(req.text.encode('utf-8'))

soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")
print(soup.title)
print(soup.title.string)
print(soup.p)
print(soup.a)
print(soup.find_all('a'))

t1=soup.find_all('a')
print(t1[0])


# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
import sys 

import urllib.request as httplib  # 3.x
try:
    url="https://www.facebook.com/animategamer/"
    req=httplib.Request(url)        #連線需求
    reponse = httplib.urlopen(req)  #打開網頁連結
    if reponse.code==200:
        #contents=reponse.read().decode(reponse.headers.get_content_charset())
        contents=reponse.read()     #取得網頁資料
        #contents=reponse.read().decode("utf-8")     # bytes 轉成 str

        print(contents)             #顯示網頁資料
except:
    print("error")
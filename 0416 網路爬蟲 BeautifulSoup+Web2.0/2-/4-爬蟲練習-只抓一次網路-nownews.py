import requests
from bs4 import BeautifulSoup
import os.path
from os import path
filename='nownews_cat_sport_nba.txt'
if path.exists(filename)==False:    # 是否有  'workfile.txt'檔案
    url = "https://www.nownews.com/cat/sport/nba/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
    req = requests.get(url, headers=headers)

    print(req.text)
    fr = open(filename, 'w',encoding="UTF-8")
    t1=req.text.encode("UTF-8")
    fr.write(req.text)
    fr.close()

file = open(filename, mode='r',encoding="UTF-8")
all_of_it = file.read()
file.close()


soup=BeautifulSoup(all_of_it.encode('utf-8'), "html.parser")
t1=soup.select('.blk')
#print(t1)
t2=t1[0].select('li')
#print(t2)

print("===今日新聞-運動-NBA===")
y=1
for x in t2:
    t3=x.select('a')
    t4=t3[0].select(".txt")
    t5=t4[0].select("h2")
    print("新聞"+str(y),t5[0].string)
    print("網址",t3[0]['href'])
    print(" ")
    y=y+1
"""
for listRight in soup.select('.focus-news'):
   for line in listRight.select('.title'):
     print(line.select('a')[0].text)
"""
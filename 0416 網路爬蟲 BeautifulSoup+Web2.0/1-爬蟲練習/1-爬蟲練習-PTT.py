import requests
from bs4 import BeautifulSoup

#req=requests.get("http://www.powenko.com/wordpress")
req=requests.get("https://www.ptt.cc/bbs/movie/index.html")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")

print("===第一階段===")
t1=soup.select(".title")
print(t1)
print("===第二階段===")
t2=t1[0].select('a')
#print(t2)
print("↓ movie版最新張貼文章 ↓")
for x in soup.select(".title"):
    t3=x.select('a')
    print(t3[0].contents[0])
print("===第三階段===")
t4=t2[0]['href']
#print(t4)
for x in soup.select(".title"):
    t3 = x.select('a')
    print("標題:",t3[0].contents[0])
    t4=t3[0]['href']
    print("網址:",t4)
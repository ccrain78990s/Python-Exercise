import requests
from bs4 import BeautifulSoup

def PTTGetContent(iurl="https://www.ptt.cc/bbs/movie/M.1597242609.A.606.html"):

    req = requests.get(iurl)
    soup = BeautifulSoup(req.text.encode('utf-8'), "html.parser")
    t1 = soup.select("#main-content")
    t2 = t1[0].select(".article-metaline")
    t3 = t2[1].contents[1]
    t4 = t3.string
    print("標題:", t4)
    t5 = t2[2].contents[1]
    t6 = t5.string
    print("時間:", t6)
    t5 = soup.select("#main-content")
    t6 = t5[0]
    t7 = t6.contents[4]
    print("內容:", t7)



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
    url="https://www.ptt.cc/"+t4
    print("網址:",url)
    PTTGetContent(iurl=url)
import requests
from bs4 import BeautifulSoup

req=requests.get("http://www.powenko.com/wordpress")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")

largefeaturepowenA2=soup.select('.largefeaturepowenA2')
largefeature0=largefeaturepowenA2[0]

print("====t1====")
t1=largefeature0.select('.area')
print(t1)
print("====t2====")
t2=t1[0].select('a')
print(t2)
print("====t3====")
t3=t2[1]
print(t3)
print("====t4====")
t4=t3.select('font')
print(t4)
print("====t5====")
t5=t4[0].string
print(t5)
"""
print("====全部====")
for x in largefeature0.select('.area'):
  t1=x.select('.area')
  t2=t1[x].select('a')
  t3=t2[1]
  t4=t3.select('font')
  t5=t4[0].string
  print(t5)
"""
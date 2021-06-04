#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"
import requests
from bs4 import BeautifulSoup

text1="""
<head>
    <title>柯博文老師</title>
</head>
<body>
    <p class="title"><b>The test</b></p>
    <a class="redcolor" href="http://powenko.com/1.html" id="link1">test1</a>
    <a class="bluecolor" href="http://powenko.com/2.html" id="link2">test2</a>
    <a class="redcolor"  href="http://powenko.com/3.html" id="link3">test3</a>
    <div id="data1">
        Fruit
    	<ul class="data2">
        	<li> Apple </li>
        	<li> Banana </li>
        </ul>
    </div>
    <div>
        Food
        <h1 class="data3"> 餐點</h1>
    	<ul class="data4">
        	<li> 魯肉販 </li>
        	<li> 雞排 </li>
        </ul>
    </div>
</body>
"""
"""
第一題:
  顯示 [餐點]
第二題:
  顯示 [魯肉販 ]  和  [雞排]
第三題:
  顯示 [Apple]和 [Banana ]  和 [魯肉販 ]  和  [雞排]
  
第4題:
  顯示 [Fruit]
       
第5題:
  顯示 [Food]

第6題:
  顯示 [data2]

第7題:
  顯示 [data3]   
"""





soup=BeautifulSoup(text1, "html.parser")
print("===第1題===")
x1=soup.select('.data3')
print(x1)
print(x1[0].string)
print("===第2題===")
x2=soup.select('.data4')
print(x2)
for d in x2[0].find_all('li'):
	print(d.string)
print("===第3題===")
x3=soup.select('li')
print(x3)
for d in x3:
	print(d.string)
print("===第4題===")
x4=soup.select('#data1')
print(x4)
print(x4[0].contents[0])
print("===第5題===")
x5=soup.select('div')
print(x5)
print(x5[1].contents[0])
print("===第6題===")
x6=soup.select('.data2')
print(x6)
print(x6[0]['class'])
print("===第7題===")
x7=soup.select('.data3')
print(x7)
print(x7[0].get('class'))
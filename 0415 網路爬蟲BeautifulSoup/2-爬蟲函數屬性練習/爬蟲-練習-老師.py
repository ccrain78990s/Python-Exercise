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
soup=BeautifulSoup(text1, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
t1=soup.find_all('a')
print(soup.find_all('a'))
for link in soup.find_all('a'):
	print(link.get('href'))
t2=soup.select('a')
print(soup.select('a'))

print(soup.select('.redcolor'))   # class="redcolor"
print(soup.select('#link3'))     # id="link3"
print(soup.select('#link3')[0].string)     # id="link3" test3
for link in soup.select('a'):
	print(link.string)

#
#class ="bluecolor" href="http://powenko.com/2.html" id="link2"
# test2
t1=soup.select('.bluecolor')  # class ="bluecolor"
t2=soup.select('#link2')  # id="link2"
"""
<a class="bluecolor" href="http://powenko.com/2.html" id="link2">test2</a>
"""
print("-----")
print(t1[0].string)
print(t1[0].contents[0])
print(t2[0].string)
print(t2[0].contents[0])
"""
<a class="redcolor"  href="http://powenko.com/1.html" id="link1">test1</a>
<a class="redcolor"  href="http://powenko.com/3.html" id="link3">test3</a>
"""
# test1 和 test3
# 方法一
print("-----方法一")
t1=soup.select('#link1')  # id="link1"
print(t1[0].string)
t1=soup.select('#link3')  # id="link3"
print(t1[0].string)
# 方法二
print("-----方法二")
t1=soup.select('.redcolor')  # class="redcolor"
print(t1)
print(t1[0])
print(t1[0].string)
print(t1[0].contents[0])
print(t1[1].contents[0])
# 方法三
print("-----方法三")
t1=soup.select('.redcolor')  # class="redcolor"
for d in t1:
	print(d)
	print(d.string)
	print(d.contents[0])

#  http://powenko.com/1.html 和 http://powenko.com/3.html
# link.get('href')
print("-----方法一")
t1=soup.select('#link1')  # id="link1"
print(t1[0].get('href'))
t1=soup.select('#link3')  # id="link3"
print(t1[0].get('href'))

# 方法二
print("-----方法二")
t1=soup.select('.redcolor')  # class="redcolor"
print(t1)
print(t1[0])
print(t1[0].get('href'))
print(t1[1].get('href'))

# 方法三
print("-----方法三")
t1=soup.select('.redcolor')  # class="redcolor"
for d in t1:
	print(d)
	print(d.get('href'))

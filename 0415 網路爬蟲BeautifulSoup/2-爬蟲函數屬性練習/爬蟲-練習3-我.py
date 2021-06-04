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
    <div class="data1">
        	<li> Apple </li>
        	<li> Banana </li>
    </div>
    <div  class="data2">
        	<li> 魯肉販 </li>
        	<li> 雞排 </li>
    </div>
</body>
"""
"""
第一題:
  顯示 [魯肉販 ]  和  [雞排]  用兩個select
"""
soup=BeautifulSoup(text1, "html.parser")
x1=soup.select('.data2')
print(x1)
x2=x1[0].select('li')
print(x2)
for d in x2:
    print(d.string)

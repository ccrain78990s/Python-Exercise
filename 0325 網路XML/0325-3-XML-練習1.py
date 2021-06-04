#!/usr/bin/env python
# -*- coding=utf-8 -*-
# 0325 練習
from xml.etree import ElementTree
import sys



xml2text="""<?xml version="1.0" encoding="utf-8"?>
<root>
 <student>
    <name age="18">Powen Ko</name> 
    <address>
        <city>桃園市</city>
        <area>中壢區</area>
    </address>
    <id>1</id> 
 </student>
 <student des="hello">
     <name age="19">kiki</name> 
     <address>
        <city>桃園市</city>
        <area>桃園區</area>
    </address>
    <id>2</id> 
 </student>
</root>"""
# 加载XML文件（2种方法,一是加载指定字符串，二是加载指定文件）
root = ElementTree.fromstring(xml2text)   #文字轉XML
# 2
# 19
# 中壢區
print(root.findall("student/id")[1].text)   #<--
print(root.findall("student/name")[1].attrib['age'])   #<--
print(root.findall("student/address/area")[0].text)   #<--
##kiki
t1=root.findall("student/name")
t2=t1[1]
t3=t2.text
print(t3)


"""
t1=root.findall("person/name")
t2=t1[1]
t3=t2.text
print(t3)
##########
t1=root.findall("person")
t2=t1[1].attrib
print(t2["age"])
print(root.findall("person")[1].attrib["age"])   # 19
t3=root.findall("person")[1].attrib
print(t3["age"])                                 # 19
"""

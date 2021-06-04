#!/usr/bin/env python
# -*- coding=utf-8 -*-
from xml.etree import ElementTree   #<----



xml2text="""<?xml version="1.0" encoding="utf-8"?>
<root>
 <person age="18">
    <name>Powen Ko</name>
    <sex>man</sex>
 </person>
 <person age="19" des="hello">
    <name>kiki</name>
    <sex>female</sex>
 </person>
</root>"""
# 加载XML文件（2种方法,一是加载指定字符串，二是加载指定文件）
root = ElementTree.fromstring(xml2text)   #文字轉XML

#print內容
print(root.findall("person/name")[1].text)   #<--
print(root.findall("person/sex")[0].text)   # man
t1=root.findall("person/name")
t2=t1[1]
t3=t2.text
print(t3)

# age=19
t1=root.findall("person")
t2=t1[1].attrib
print(t2['age'])

print(root.findall("person")[1].attrib['age'])   # man


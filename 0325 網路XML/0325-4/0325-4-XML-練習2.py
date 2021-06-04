#!/usr/bin/env python
# -*- coding=utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse('doswTaipei.xml')       #網路上下載來的檔案
root = tree.getroot()

print(root.findall("MAP/ADDRESS")[0].text)

t1=root.findall("MAP")
t2=t1[0].findall("ADDRESS")
print(t2[0].text)

t1=root.findall("MAP/ADDRESS")
t2=t1[0].text
print(t2)

print(root.findall("MAP/PERSON_IN_CHARGE")[0].text)
print("===資料長度===")
t1=root.findall("MAP/ADDRESS")
print(len(t1))
t2=root.findall("MAP")
print(len(t2))
print("  ")
print("======印出所有地址資料1======")
#while
#for in
x=0
while x < len(t1):
    print(t1[x].text)
    x=x+1
print("  ")
print("======印出所有地址資料2======")
for y in range(0,len(t1)):
    print(t1[y].text)
print("  ")
print("======印出所有地址資料3======")
t1=root.findall("MAP/ADDRESS")
for y in t1:
    print(y.text)
print("  ")
print("======印出所有地址資料+負責人======")
# 注意 ↓↓↓
t0=root.findall("MAP")
t1=root.findall("MAP/ADDRESS")
t2=root.findall("MAP/PERSON_IN_CHARGE")
for y in range(0,len(t0)):      #<---選擇資料長度的位置 萬一 某個資料沒有怎麼辦
    print("負責人:",t2[y].text,"地址:",t1[y].text)

# one specific item attribute
print('Item #2 attribute:')
print(root[0][1].attrib)

# all item attributes
print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

# one specific item's data
print('\nItem #2 data:')
print(root[0][1].text)

# all items data
print('\nAll item data:')
for elem in root:
    for subelem in elem:
        print(subelem.text)
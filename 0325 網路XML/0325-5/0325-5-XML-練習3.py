#!/usr/bin/env python
# -*- coding=utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse('StationTimeTable.xml')       #網路上下載來的檔案
root = tree.getroot()


print("===資料長度===")

t1=root.findall("StationTimeTable")
print(len(t1))
print("  ")


print("======印出所有站別資料======")
#while

t1=root.findall("StationTimeTable")
t2=root.findall("StationTimeTable/StationName/Zh_tw")
t3=root.findall("StationTimeTable/DestinStationName/Zh_tw")

t4=root.findall("StationTimeTable/Timetables")
t5=root.findall("StationTimeTable/Timetables/Timetable/Sequence")
t6=root.findall("StationTimeTable/Timetables/Timetable/ArrivalTime")

#t7=root.findall("StationTimeTable/ServiceDay/ServiceTag")

x=0
while x < len(t1):
    y=0
    while y < len(t4):
        #print("班次別:",t7[x].text)
        print("起始站:",t2[x].text,"終點站:",t3[x].text)
        print("班次:",t5[y].text,"到達時間:",t6[y].text)
        print("   ")
        y=y+1
    x=x+1
print("  ")

"""
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

"""
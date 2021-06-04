#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
"""
Mac 的使用者　如果出現　SSL Certificate Error
請執行以下的程式，HTTPS 就能工作
/Applications/python 3.6/Install Certificates.command
"""

import json
import sys 
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x

import ssl
context = ssl._create_unverified_context()

url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=b3abedf0-aeae-4523-a804-6e807cbad589&rid=bf55b21a-2b7c-4ede-8048-f75420344aed"
req=httplib.Request(url)

try:
    reponse = httplib.urlopen(req, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read();
        else:
            contents = reponse.read()
        data = json.loads(contents)


except:                                                                 #  處理網路連線異常
    print("error")

"""
參考資料:
https://data.tycg.gov.tw/opendata/datalist/datasetMeta?oid=b3abedf0-aeae-4523-a804-6e807cbad589
https://data.gov.tw/dataset/43963
"""
# 取的

#　BusID(車號),DutyStatus(營運狀態[0=執勤,1=開始,2=結束,90=不明])
print("車號:",data['datas'][0]['BusID'],
      "行駛路線:",data['datas'][0]['RouteID'],
      "去返程:",data['datas'][0]['GoBack'],
      "所在位置緯度:",data['datas'][0]['Longitude'],
      "所在位置精度:",data['datas'][0]['Latitude'],
      "車速:",data['datas'][0]['Speed'])

print("===所有公車輛數===")
t1=len(data['datas'])
print(t1)

print("===全部公車資料===")
x=0
while x < t1:
    print("車號:", data['datas'][x]['BusID'],
          "行駛路線:", data['datas'][x]['RouteID'],
          "去返程:", data['datas'][x]['GoBack'],
          "所在位置緯度:", data['datas'][x]['Longitude'],
          "所在位置精度:", data['datas'][x]['Latitude'],
          "車速:", data['datas'][x]['Speed'])
    x=x+1

print("===行駛中公車 speed > 0 ===")
x=0
while x < t1:
    if float(data['datas'][x]['Speed']) > 0 :
        print("車號:", data['datas'][x]['BusID'],
          "行駛路線:", data['datas'][x]['RouteID'],
          "去返程:", data['datas'][x]['GoBack'],
          "所在位置緯度:", data['datas'][x]['Longitude'],
          "所在位置精度:", data['datas'][x]['Latitude'],
          "車速:", data['datas'][x]['Speed'])
    x=x+1

print("===行駛中公車 路線715 ===")
x=0
while x < t1:
    if float(data['datas'][x]['Speed']) > 0 :
        if data['datas'][x]['RouteID'] == "715":
            print("車號:", data['datas'][x]['BusID'],
              "行駛路線:", data['datas'][x]['RouteID'],
              "去返程:", data['datas'][x]['GoBack'],
              "所在位置緯度:", data['datas'][x]['Longitude'],
              "所在位置精度:", data['datas'][x]['Latitude'],
              "車速:", data['datas'][x]['Speed'])
    x=x+1


# ,RouteID(行駛路線),GoBack(去返程[1=去程,2=返程]),
# Longitude(所在位置緯度),Latitude(所在位置經度),Speed(車速)


"""
ProviderID(業者代碼),BusID(車號),DutyStatus(營運狀態[0=執勤,1=開始,2=結束,90=不明]),
BusStatus(車輛狀態[0=正常,1=車禍,2=故障,3=塞車,4=求援,5=加油,90=不明或長時間無到離站]),
RouteID(行駛路線),GoBack(去返程[1=去程,2=返程]),Longitude(所在位置緯度),Latitude(所在位置經度),
Speed(車速),Azimuth(方位角),DataTime(系統時間),ledstate(保留用),sections(保留用),carType(保留用),rectime(保留用),driverid(保留用)

"""
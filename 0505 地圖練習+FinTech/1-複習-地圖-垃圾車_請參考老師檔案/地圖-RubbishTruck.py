#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"

"""
參考資料:
https://data.tycg.gov.tw/opendata/datalist/datasetMeta?oid=b3abedf0-aeae-4523-a804-6e807cbad589
https://data.gov.tw/dataset/43963
"""
"""
資料欄位

項次(項次)、清運序(清運序)、行政區(行政區)、清運路線名稱(清運路線名稱)、清運點名稱(清運點名稱)、
一般垃圾清運時間(一般垃圾清運時間)、廚餘回收清運時間(廚餘回收清運時間)、資源回收清運時間(資源回收清運時間)

範例
'項次' = {str} '1'
'清運序' = {str} '1'
'行政區' = {str} '蘆竹區'
'清運路線名稱' = {str} '山腳區1線'
'清運點名稱' = {str} '山林路一段與山腳街口'
'一般垃圾清運時間' = {str} '星期一二四五六:16:55'
'廚餘回收清運時間' = {str} '星期一二四五六:16:55'
'資源回收清運時間' = {str} '星期一二四五六:16:55'

"""




import json
import sys 
import urllib.request as httplib  # 3.x

import ssl
context = ssl._create_unverified_context()



#url="http://data.taipei/opendata/datalist/datasetMeta/download?id=ea732fb5-4bec-4be7-93f2-8ab91e74a6c6&rid=bf073841-c734-49bf-a97f-3757a6013812"
#url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
#url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=b3abedf0-aeae-4523-a804-6e807cbad589&rid=bf55b21a-2b7c-4ede-8048-f75420344aed"
url="http://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json"
url="https://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json&offset=100" # 由第幾筆開始
url="https://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json&limit=800" # 最大資料量800筆
url="https://data.tycg.gov.tw/api/v1/rest/datastore/0c7bcfbf-b151-4411-b888-9ff685ff7a75?format=json&limit=6000" # 最大資料量6000筆
req=httplib.Request(url)
try:
    reponse = httplib.urlopen(req, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read()
        else:
            contents = reponse.read()
        data = json.loads(contents)
        #print(data)


        ## 第二題：　顯示全部的
        print("===== 顯示全部的 =====")
        length=len(data["result"]["records"])   # 有幾台的資料
        x=0
        while x<length:
            print("項次:", data["result"]["records"][x]["項次"],
                  ",清運序:", data["result"]["records"][x]["清運序"],
                  ",行政區", data["result"]["records"][x]["行政區"],
                  ",清運路線名稱:", data["result"]["records"][x]["清運路線名稱"],
                  ",清運點名稱:", data["result"]["records"][x]["清運點名稱"],
                  ",一般垃圾清運時間:", data["result"]["records"][x]["一般垃圾清運時間"],
                  ",廚餘回收清運時間:", data["result"]["records"][x]["廚餘回收清運時間"],
                  ",資源回收清運時間:", data["result"]["records"][x]["資源回收清運時間"])
            x=x+1

        ## 第三題：　今天()可以到垃圾的地點

        print("=====第三題：　今天()可以到垃圾的地點=======")
        import time, datetime
        def get_week_day(date):
            week_day_dict = {
                0: '一',
                1: '二',
                2: '三',
                3: '四',
                4: '五',
                5: '六',
                6: '天',
            }
            day = date.weekday()
            return week_day_dict[day]
        from datetime import datetime
        now = datetime.now()    # 現在時間
        week = get_week_day(now)    # 找星期幾

        length=len(data["result"]["records"])   # 有幾台的資料
        x=0
        while x<length:
            txt = data["result"]["records"][x]["一般垃圾清運時間"]
            position = txt.find(week)
            # print(txt,week)
            # print("該字的位置:",x)
            if position>0 and data["result"]["records"][x]["行政區"]=="中壢區" :
                print("今天有垃圾出的地點有-項次:", data["result"]["records"][x]["項次"],
                      ",清運序:", data["result"]["records"][x]["清運序"],
                      ",行政區", data["result"]["records"][x]["行政區"],
                      ",清運路線名稱:", data["result"]["records"][x]["清運路線名稱"],
                      ",清運點名稱:", data["result"]["records"][x]["清運點名稱"],
                      ",一般垃圾清運時間:", data["result"]["records"][x]["一般垃圾清運時間"],
                      ",廚餘回收清運時間:", data["result"]["records"][x]["廚餘回收清運時間"],
                      ",資源回收清運時間:", data["result"]["records"][x]["資源回收清運時間"])

            x=x+1

        """
        ## 第三題：　今天()可以到垃圾的地點

        print("=====第三題：　今天 本小時()可以到垃圾的地點=======")

        now = datetime.now()    # 現在時間
        week = get_week_day(now)    # 找星期幾
        current_H = now.strftime("%H")  # 印出時間的格式
        print("現在時間小時 =", current_H)

        length=len(data["result"]["records"])   # 有幾台的資料
        x=0
        while x<length:
            txt = data["result"]["records"][x]["一般垃圾清運時間"]
            position = txt.find(week)
            positionH = txt.find(":"+current_H+":")            # 星期一二四五六:10:18
            if position>0  and positionH>0 and data["result"]["records"][x]["行政區"]=="中壢區" :
                print("此時可倒垃圾的地點有-項次:", data["result"]["records"][x]["項次"],
                      ",清運序:", data["result"]["records"][x]["清運序"],
                      ",行政區", data["result"]["records"][x]["行政區"],
                      ",清運路線名稱:", data["result"]["records"][x]["清運路線名稱"],
                      ",清運點名稱:", data["result"]["records"][x]["清運點名稱"],
                      ",一般垃圾清運時間:", data["result"]["records"][x]["一般垃圾清運時間"],
                      ",廚餘回收清運時間:", data["result"]["records"][x]["廚餘回收清運時間"],
                      ",資源回收清運時間:", data["result"]["records"][x]["資源回收清運時間"])
            x=x+1
        """
        UBike = []
        latitude = []
        longitude = []
        magnitude = []
        for retVal in data["result"]["records"]:
            # print(retVal)
            sna = data["retVal"][retVal]["sna"]
            tot = data["retVal"][retVal]["tot"]
            sbi = data["retVal"][retVal]["sbi"]
            lat = float(data["retVal"][retVal]["lat"])
            lng = float(data["retVal"][retVal]["lng"])
            latitude.append(lat)
            longitude.append(lng)
            magnitude.append(sbi)
            ## 第二層
            dict1 = {}
            dict1["name"] = sna
            dict1["location"] = (lat, lng)
            dict1["active_reactors"] = sbi
            UBike.append(dict1)

        df = pd.DataFrame({'latitude': latitude,
                           'longitude': longitude,
                           'magnitude': magnitude})

        print(df['magnitude'])
        print(df['magnitude'].max())

        api_key = 'AIzaSyDoktG9CKKy09FlZr6SIlqiXMZi3W_At74'

        import gmaps
        import gmaps.datasets

        # Use google maps api
        gmaps.configure(api_key=api_key)  # Fill in with your API key

        # dataframe with columns ('latitude', 'longitude', 'magnitude')
        fig = gmaps.figure()
        heatmap_layer = gmaps.heatmap_layer(df[['latitude', 'longitude']], weights=df['magnitude'],
                                            max_intensity=30, point_radius=30.0)
        fig.add_layer(heatmap_layer)

        ###第二層####

        plant_locations = [plant['location'] for plant in UBike]
        info_box_template = """
        名稱:{name}<br>
        經緯度:{location}<br>
        可借車位數:{active_reactors}<br>
        """
        plant_info = [info_box_template.format(**plant) for plant in UBike]
        marker_layer = gmaps.marker_layer(plant_locations, info_box_content=plant_info)
        fig.add_layer(marker_layer)

        ## 輸出到  export.html
        from ipywidgets.embed import embed_minimal_html

        embed_minimal_html('export.html', views=[fig])







except:                                                                 #  處理網路連線異常
    print("error")


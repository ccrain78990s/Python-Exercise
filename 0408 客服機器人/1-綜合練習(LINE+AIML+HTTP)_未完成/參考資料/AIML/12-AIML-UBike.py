# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
"""
請給我 1 份 草莓蛋糕
我要開發票
我要刷卡
結帳

桃園市 的天氣
健行 ubike資訊
圖書館 ubike資訊
健行 資訊

"""
import aiml
import json
import os
# {"exe":"python 11-UbikeData.py <star index = "1"/>"}
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("12-AIML-UBike.xml")
while True:   # Press CTRL-C to break this loop
    t1=input("請輸入 >> ")
    contents=kernel.respond(t1)

    if(contents.find('exe')>0):
        data = json.loads(contents)
        print(data)
        exe2=data["exe"]
        #exe2="python 11-UbikeData.py"
        os.system(exe2)

    elif(contents.find('items')>0):
            data = json.loads(contents)
            print(data)
            price=0
            meat=data["meat"]
            items=data["items"]
            tax=data["tax"]
            VISA=data["VISA"]
            if(meat==' 草莓蛋糕' or  meat=='草莓蛋糕'):
                price=100*int(items)
                if(tax=="True"):
                    price =price*1.05
                if(VISA=="True"):
                    price =price*1.02
            contents="一共是"+str(price)
    #except:
    #    print("")
    print(contents)
    #print(input(ernel.respond("Enter your message >> ")))


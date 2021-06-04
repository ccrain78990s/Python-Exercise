# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
"""
請給我 1 份 草莓蛋糕
我要開發票
我要刷卡
結帳
"""
import aiml
import json

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("03-AIML-公司服務簡介系統.xml")
while True:   # Press CTRL-C to break this loop
    t1=input("請輸入 >> ")
    contents=kernel.respond(t1)
    print(contents)
    #print(input(ernel.respond("Enter your message >> ")))


#!/usr/bin/env python
# coding: utf-8

# mac 安裝方法
# https://medium.com/@brettlin_78528/%E7%94%A8-python-%E5%8C%AF%E5%85%A5-selenium-%E7%9A%84%E6%96%B9%E5%BC%8F-%E4%BB%A5%E5%8F%8A%E5%A6%82%E4%BD%95%E7%94%A8mac-%E5%AE%89%E8%A3%9D-chromedriver-5d92121c02d7
# In[1]:


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import os
print(os.name)
if(os.name=="posix"):   # mac 作業系統的處理方法
    chromedriver='/Users/powenko/Desktop/powenko/2020Working/20201119-學生問題/chromedriver'
    chromedriver='chromedriver'
    driver =webdriver.Chrome(chromedriver)
else:                   # Windows OS
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
driver.get("https://www.railway.gov.tw/tra-tip-web/tip")

time.sleep(2)  # DELAY 4 sec


time.sleep(1)               # 停個 1 sec
continue_link = driver.find_element_by_link_text('線上訂票')
continue_link.click()
time.sleep(4)


continue_link = driver.find_element_by_link_text('個人訂票')
continue_link.click()
time.sleep(1)

context = driver.find_element_by_id('pid')   # 身分證字號
context.send_keys("H124XXXXX")
context = driver.find_element_by_id('startStation')   # 出發站
context.send_keys("1100")   # 中壢
time.sleep(2)
context = driver.find_element_by_id('endStation')   # 抵達站
context.send_keys("3300")   # 台中
time.sleep(2)
context = driver.find_element_by_id('trainNoList1')   # 車次
context.send_keys("125")   # 13:42-15:19
time.sleep(2)
# 行程類型>>點選 去回票
element = driver.find_element_by_id('tripType1')
driver.execute_script("$(arguments[0]).click();", element)
time.sleep(2)
# 訂票方式>>點選 依時段
element = driver.find_element_by_id('orderType2')
driver.execute_script("$(arguments[0]).click();", element)
time.sleep(2)

# 增加座票數
button=driver.find_element_by_xpath("//button[@class='add']")
button.click()

#ontext.send_keys(Keys.RETURN)   #訂票送出

"""
#輸入keyword
# <input type="text" class="inputtext _55r1 _6luy" name="email" id="email" data-testid="royal_email" placeholder="電子郵件地址或手機號碼" autofocus="1" aria-label="電子郵件地址或手機號碼">
context = driver.find_element_by_id('keyword')   # id="keyword"
context.send_keys("android")
context.send_keys(Keys.RETURN)   # 下 ARROW_DOWN)

time.sleep(2)    # 5sec
"""

"""
# 移動到下一頁
for i in range(2):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)

time.sleep(4)
# 取的網頁內容
html=driver.page_source
print(html)


soupA=BeautifulSoup(html.encode('utf-8'), "html.parser")

HTML_ItemContainer=soupA.select("#ItemContainer") # id="ItemContainer"

HTML_col3f=HTML_ItemContainer[0].select(".col3f") # class=col3f
for d in HTML_col3f:
    # class="prod_name"    標題
    # class="nick"     內容
    # class="price" 價格
    prod_name=d.select(".prod_name")
    nick=d.select(".nick")
    price=d.select(".price")
    print("標題:"+prod_name[0].text)
    print("內容:" + nick[0].text)
    print("價格:" + price[0].text)
    print("-------------")
"""

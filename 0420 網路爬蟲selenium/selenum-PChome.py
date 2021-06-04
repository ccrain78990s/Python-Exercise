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
driver.get("https://24h.pchome.com.tw/")

time.sleep(2)  # DELAY 4 sec

#輸入keyword
# <input type="text" class="inputtext _55r1 _6luy" name="email" id="email" data-testid="royal_email" placeholder="電子郵件地址或手機號碼" autofocus="1" aria-label="電子郵件地址或手機號碼">
context = driver.find_element_by_id('keyword')   # id="keyword"
context.send_keys("android")
context.send_keys(Keys.RETURN)   # 下 ARROW_DOWN)

time.sleep(2)               # 5sec

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
    print(price)


print(HTML_col3f)


HTML_pages_msite_body_contents=HTML_root[0].select("#pages_msite_body_contents")
#t1=HTML_pages_msite_body_contents[0].contents[0].contents[3]
t2=HTML_pages_msite_body_contents[0].select("header")
print(t2)



#soupA=BeautifulSoup(html,'lxml')


# In[10]:


"""
A=soupA.find(class_='k4urcfbm dp1hu0rb d2edcug0 cbu4d94t j83agx80 bp9cbjyn')
B=A.find_all(class_='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0')
print(len(B))
for i in range(len(B)):
    C=B[i].find(class_='o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q').getText()
    print(C)

# In[11]:
print(len(B))  #抓到幾篇文章
# In[ ]:
"""




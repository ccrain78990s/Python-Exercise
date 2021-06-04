
"""
資料來源:
https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# driver = webdriver.Firefox()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver.exe',chrome_options=option)
driver.get('https://www.ruten.com.tw/')

time.sleep(5)               # 停個 5 sec

"""
<input id="keyword" name="k" value="" accesskey="4" data-type="search-input" autocomplete="off" class="rt-header-search-input">
"""
# element = driver.find_element_by_id("keyword")  # id="keyword"
# element = driver.find_element_by_name("k")   # name="k"
element = driver.find_element_by_xpath("//input[@id='keyword']")   # <input id="keyword"
element.send_keys("android")
element.send_keys(Keys.RETURN)   # 下 ARROW_DOWN)

time.sleep(5)               # 5sec
html=driver.page_source
print(html)


soup=BeautifulSoup(html.encode('utf-8'), "html.parser")
t1=soup.select('.content')  # class="content"
t2=t1[1].select('dd')     #<dd
for dd in t2:
    try:
        prod_name = dd.select('.prod_name')    # class="price"
        print(prod_name[0].contents[1].contents[0])
        price = dd.select('.price')  # class="price"
        print(price[0].contents[0])
    except:
        print("error")




"""
elem = driver.find_element_by_name("q")
elem.clear()                  # 清空
elem.send_keys("powenko")
elem.send_keys(Keys.RETURN)   # 輸入Enter
# assert "No results found." not in driver.page_source
print(driver.page_source)
"""
time.sleep(5)               # 5sec
driver.close()              # 視窗關閉

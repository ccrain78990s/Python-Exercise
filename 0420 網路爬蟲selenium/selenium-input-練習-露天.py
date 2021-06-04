
"""
資料來源:
https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# driver = webdriver.Firefox()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver.exe',chrome_options=option)
driver.get('https://www.ruten.com.tw/')

time.sleep(5)               # 停個 5 sec
element = driver.find_element_by_id("keyword")  # id="searchbox"
# element = driver.find_element_by_name("k")   # name="s"
# element = driver.find_element_by_xpath("//input[@id='keyword']")   #  <input id="searchbox"
element.send_keys("茶几")
element.send_keys(Keys.RETURN)   # 下 ARROW_DOWN)
#element.send_keys("android",Keys.ARROW_DOWN)

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

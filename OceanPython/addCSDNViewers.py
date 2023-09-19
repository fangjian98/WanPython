import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# 页面下滑
# browser.execute_script("window.scrollBy(0,1080)")

# weixin_44008788 为 CSDN User ID
BASE_URL = 'https://blog.csdn.net/weixin_44008788/article/list/'
circle = []
for i in range(1, 6):
    circle.append(BASE_URL + str(i))

for j in range(1, 200):
    print("循环次数："+str(j))
    for r in circle:
        url = r
        print(url)
        browser = webdriver.Chrome()
        browser.get(url)
        for i in range(1, 2):
            print(i)
            # for lib selenium:v4.4.2
            # for link in browser.find_elements_by_xpath('//h4[@class=""]/a'):
            # for lib selenium the latest version
            for link in browser.find_elements(By.XPATH, r'//h4[@class=""]/a'):
                link.click()
                time.sleep(random.randrange(0, 6))
            time.sleep(random.randrange(0, 9))
        browser.quit()


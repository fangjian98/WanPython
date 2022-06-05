import random
import time
from selenium import webdriver

browser = webdriver.Chrome()

# weixin_44008788 为 CSDN User ID
BASE_URL = 'https://blog.csdn.net/weixin_44008788/article/list/'
circle = []
for i in range(1, 6):
    circle.append(BASE_URL + str(i))

for r in circle:
    url = r
    print(url)
    browser.get(url)
    for i in range(1, 4):
        print(i)
        for link in browser.find_elements_by_xpath('//h4[@class=""]/a'):
            link.click()
            time.sleep(random.randrange(0, 6))
        time.sleep(random.randrange(0, 9))

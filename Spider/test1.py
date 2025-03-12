from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import base64
import io

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
#chromedriver = "/usr/bin/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get("https://bsy-cdn-zhgame.yunyungquan.com/pengpengqiu/index.html?openid=opua_jgFjDMnz7ufTn4M3I-BmMsE&activeid=243&_t=12")
time.sleep(10)
ActionChains(driver).move_by_offset(400, 270).click().perform()#开始
time.sleep(25)
ActionChains(driver).move_by_offset(1, 0).click().perform()#25分
time.sleep(26)
ActionChains(driver).move_by_offset(1, 0).click().perform()#25分
time.sleep(26)
ActionChains(driver).move_by_offset(1, 0).click().perform()#25分
time.sleep(27)
ActionChains(driver).move_by_offset(1, 0).click().perform()#25分
#print(driver.title)
time.sleep(38)
#x = driver.get_screenshot_as_base64()#打印64图片
#image = base64.b64decode(x)#看是否点击对了
#print(x)
time.sleep(2)
driver.quit()
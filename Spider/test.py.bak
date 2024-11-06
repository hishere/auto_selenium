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
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
driver.get("https://bsy-cdn-zhgame.yunyungquan.com/pengpengqiu/index.html?openid=opua_jrbKwEGa4xESBuQMqUnOhUw&activeid=232&_t=12")
#ActionChains(driver).move_by_offset(200, 100).click().perform() 
#print(driver.title)
x = driver.get_screenshot_as_base64()
image = base64.b64decode(x)
im=io.BytesIO(image)
print(im)
time.sleep(20)
driver.quit()
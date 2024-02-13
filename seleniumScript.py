from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)

browser.get("https://www.amazon.in/")
#browser.navigate().forward()
browser.maximize_window()
time.sleep(5)
ele = browser.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[3]')
assert ele.text == 'Best Sellers'
print(ele.value_of_css_property('background-color'))

time.sleep(5)




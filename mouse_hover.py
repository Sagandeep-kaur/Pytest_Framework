from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
browser= webdriver.Chrome('C:\\chromedriver_win32\\chromedriver')
browser.get("https://www.yatra.com/")
assert browser.title == "yatra"
#assert "yatra" in browser.title
time.sleep(3)
mainMenu= browser.find_element(By.XPATH, '//*[@id="bEnginePos"]/ul/li[7]/span')
action = ActionChains(browser)
action.move_to_element(mainMenu)
action.perform()
subMenu= browser.find_element(By.XPATH, '//*[@id="booking_engine_adventures"]/span')
action.move_to_element(subMenu)
action.click().perform()
time.sleep(6)
browser.close()



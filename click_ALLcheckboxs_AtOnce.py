from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser= webdriver.Chrome('C:\\chromedriver_win32\\chromedriver')
browser.get("https://demo.automationtesting.in/Register.html")
browser.maximize_window()
check_boxes= browser.find_elements(By.XPATH, '//*[@type="checkbox"]')
print(len(check_boxes))

for box in check_boxes:

    box.click()

time.sleep(6)
browser.close()


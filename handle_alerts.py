from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
#option = Options()
#option.add_argument("--disable-notifications")
browser = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver')
browser.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
browser.maximize_window()
browser.switch_to.frame("iframeResult")
browser.find_element(By.XPATH,'/html/body/button').click()
time.sleep(2)
WebDriverWait(browser, 20).until(EC.alert_is_present())
browser.switch_to.alert.accept()
time.sleep(3)
browser.close()
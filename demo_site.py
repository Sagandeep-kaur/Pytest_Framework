from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
browser= webdriver.Chrome('C:\\chromedriver_win32\\chromedriver')
browser.get("https://www.yatra.com/")

time.sleep(3)
# selecting login from account button_down
main_menu= browser.find_element(By.XPATH, '//html/body/div[2]/div/div/div/div[4]/div[2]/div/ul/li[1]')
action = ActionChains(browser)
subMenu = browser.find_element(By.XPATH, '//*[@id="signInBtn"]')
action.move_to_element(main_menu)
action.perform()
action.move_to_element(subMenu)
action.click().perform()

# clicking on signin button using gmail
browser.find_element(By.XPATH, '//*[@id="google-login-btn"]').click()
time.sleep(10)
# clicking on username
browser.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys("sagandeepk@gmail.com")
#time.sleep(5)




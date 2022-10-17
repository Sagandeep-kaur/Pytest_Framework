from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
#from selenium.webdriver.common.keys import Keys
browser= webdriver.Chrome('C:\\chromedriver_win32\\chromedriver')
browser.get("https://learn-automation.com")
# we have copied  this browser title from page source
assert browser.title == "Automation - Selenium WebDriver tutorial Step by Step"
try:
    assert browser.title == "Automation-Selenium WebDriver tutorial Step by Step"
except:
    print("its an error")
element = browser.find_element(By.XPATH, ('//*[@id="genesis-content"]/article[1]/header/h2/a')).text
print(element)
assert element == "Handle Authentication Pop Up in Selenium 4 using Chrome DevTools Protocols API"

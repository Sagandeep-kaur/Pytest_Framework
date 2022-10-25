from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

option= Options()
# this is for disabling notifications
option.add_argument("--disable-notifications")
# the below code is written if you get access denied on website
option.add_argument( '--disable-blink-features=AutomationControlled' )

browser= webdriver.Chrome('C:\\chromedriver_win32\\chromedriver', chrome_options = option)
browser.get("https://www.yatra.com/")
browser.maximize_window()

browser.find_element(By.XPATH, '//*[@id="themeSnipe"]/div/div/div[1]/button').click()
depart_from = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="BE_flight_origin_city"]')))
depart_from.click()
time.sleep(4)
depart_from.send_keys("Chennai")
time.sleep(4)
depart_from.send_keys(Keys.ENTER)
depart_to = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BE_flight_arrival_city"]')))
depart_to.click()
time.sleep(6)
depart_to.send_keys("New York")
time.sleep(4)
depart_to.send_keys(Keys.ENTER)
time.sleep(3)
browser.find_element(By.XPATH,'//*[@id="BE_flight_flsearch_btn"]').click()
depart_date = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="03/11/2022"]'))).click()
browser.find_element(By.XPATH, '//*[@id="BE_flight_flsearch_btn"]').click()
time.sleep(10)
WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flightSRP"]/section/section[2]/div/div[1]/div[2]/div[2]/label[2]/p'))).click()
# handling dynamic scrolling
SCROLL_PAUSE_TIME = 3
last_height = browser.execute_script("return document.body.scrollHeight")
#WebDriverWait(browser, 20).until(
        #EC.element_to_be_clickable((By.XPATH, "//div[contains(text() ,'More Flights')]"))).click()


while True:


    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

elems = browser.find_elements(By.XPATH,  "//div[contains(text() ,'More Flights') or contains(text() ,'1 More Flight')]")
for elem in elems:

    browser.execute_script("arguments[0].scrollIntoView();", elem)
    browser.execute_script("arguments[0].click();", elem)
    #time.sleep(4)

search_results = browser.find_elements(By.XPATH, "//span[contains(text() ,'1 Stop')] ")

print(len(search_results))

time.sleep(3)
# checking whether the filter "1 stop" has been applied successfully
for stop in search_results:
    #print(stop.text)
    assert (stop.text) == "1 Stop"
    print("passed")
time.sleep(5)


#browser.close()
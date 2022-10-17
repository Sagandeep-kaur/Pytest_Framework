from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

option= Options()
option.add_argument("--disable-notifications")
browser= webdriver.Chrome('C:\\chromedriver_win32\\chromedriver', chrome_options = option)
browser.get("https://www.yatra.com/")
browser.maximize_window()
browser.find_element(By.XPATH, '//*[@id="themeSnipe"]/div/div/div[1]/button').click()


# selecting login from account button_down
main_menu= browser.find_element(By.XPATH, '//html/body/div[2]/div/div/div/div[3]/div[2]/div/ul/li[1]/a')
action = ActionChains(browser)
subMenu = browser.find_element(By.XPATH, '//*[@id="signInBtn"]')
action.move_to_element(main_menu)
action.perform()
action.move_to_element(subMenu)
action.click().perform()

# clicking on signin button using gmail
browser.find_element(By.XPATH, '//*[@id="google-login-btn"]').click()
time.sleep(6)
browser.switch_to.window(browser.window_handles[1])
browser.maximize_window()
# entering username
user_name= input("enter username")
username= browser.find_element(By.XPATH,'//input[@id="identifierId"]')
username.send_keys(user_name)
browser.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()
time.sleep(6)
# entering password
pass_word = browser.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')
password= input("enter your password")
pass_word.send_keys(password)
time.sleep(7)
browser.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()

browser.switch_to.window(browser.window_handles[0])
time.sleep(6)
# selecting dates
browser.find_element(By.XPATH,'//*[@id="booking_engine_hotels"]/span').click()
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="BE_hotel_checkin_date"]').click()
time.sleep(2)
browser.find_element(By.XPATH,'//*[@id="19/10/2022"]').click()
browser.find_element(By.XPATH,'//*[@id="BE_hotel_checkout_date"]').click()
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="20/10/2022"]').click()
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_info"]/span').click()
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/div[2]/div[3]/div/div/span[2]').click()
browser.find_element(By.XPATH,'//*[@id="BE_hotel_htsearch_btn"]').click()
browser.find_element(By.XPATH , '//*[@id="themeSnipe"]/section/div[2]/section[3]/div/div[2]/div/div[1]/div/a[1]/div/img').click()

select = Select(browser.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/ul/li[2]/div/select'))

select.select_by_value('8')
# searching hotel
browser.find_element(By.XPATH, '//*[@id="BE_hotel_htsearch_btn"]').click()
WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="img_00001793"]'))).click()
# selecting room
# switched to new tab to find the element
time.sleep(6)
browser.switch_to.window(browser.window_handles[1])
element2= browser.find_element(By.XPATH, '//*[@id="roomWrapper0000344669"]/div[2]/div[5]/button').click()
time.sleep(2)




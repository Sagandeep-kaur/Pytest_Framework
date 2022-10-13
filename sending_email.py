from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser= webdriver.Chrome('C:\\chromedriver_win32\\chromedriver')
browser.get("https://www.google.com/")
browser.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a').click()
browser.find_element(By.XPATH, '//html/body/header/div/div/div/a[2]').click()
ele= browser.find_element(By.NAME, "identifier")
ele_one= input("enter your username")
ele.send_keys(ele_one)
browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()

wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
ele_two=browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
ele_three= input("enter password")
ele_two.send_keys(ele_three)
browser.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()
wait = WebDriverWait(browser, 30)
wait.until(EC.element_to_be_clickable((By.XPATH, '//html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div'))).click()
wait.until(EC.presence_of_element_located((By.ID , ":v3")))

ele_four = browser.find_element(By.XPATH, '//*[@id=":v3"]')
email= input("type email of recipient")
ele_four.send_keys(email)
wait.until(EC.presence_of_element_located((By.ID , ":r8"))).send_keys("Incubyte Deliverables:1")
wait.until(EC.presence_of_element_located((By.ID, ":se"))).send_keys("Automation QA test for Incubyte")
browser.find_element(By.XPATH,'//*[@id=":qy"]').click()
time.sleep(5)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=":mv"]/div/div[2]/span/a'))).click()
time.sleep(10)
browser.close()







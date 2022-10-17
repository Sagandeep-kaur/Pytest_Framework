from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
browser= webdriver.Chrome('C:\\chromedriver_win32\\chromedriver')
browser.get("https://qavbox.github.io/demo/webtable/")
assert browser.title == "Home"
webtable = browser.find_element(By.ID, "table01")
header = webtable.find_elements(By.TAG_NAME,"th")
#print(len(header))
for header_el in header:
    print(header_el.text)
# using body to print rows
body= webtable.find_element(By.TAG_NAME,"tbody")
row= body.find_elements(By.TAG_NAME, "tr")
print(len(row))

column= body.find_elements(By.TAG_NAME, "td")
print(len(column))

for row_el in row:
    print(row_el.text)
# fetching individual element using for loop on rows and column
"""
for i in range(len(row)):
    column= row[i].find_elements(By.TAG_NAME, "td")
    for j in range(len(column)):
        if column[j].text== "TFS":
          # column[0].click()
"""
time.sleep(3)
# fetching individual element using only xpath
ele= browser.find_element(By.XPATH,('//*[@id="table01"]/tbody/tr[3]/td[2]'))
assert ele.text == "Performanc"




time.sleep(3)


browser.quit()
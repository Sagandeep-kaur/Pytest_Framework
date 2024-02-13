from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.wait import WebDriverWait

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://bulwarkprod.abacasys.com/raqprod/bulwark/r/bulwark-health/login?session=3307821441692")
driver.maximize_window()
Username = '//*[@id="P9999_USERNAME"]'
time.sleep(2)
driver.find_element(By.XPATH, Username).send_keys('raghav_aegis')
time.sleep(9)
Password = '//*[@id="P9999_PASSWORD"]'
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, Password))).send_keys('Raghav1@')
#driver.find_element(By.XPATH, 'Password').send_keys('Raghav1@')
time.sleep(8)
LoginButton = '//*[@id="loginBtn"]'
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, LoginButton))).click()
time.sleep(15)
# clicking on query bank tab
queryBank = '//*[@id="t_TreeNav_19"]/div[2]/a'

js_code = "arguments[0].scrollIntoView()"
element = driver.find_element(By.XPATH, queryBank)
driver.execute_script(js_code, element)
element.click()

time.sleep(6)

Rows = driver.find_elements(By.XPATH,'//*[@id="query_bank_report_data_panel"]/div[2]/div/div[3]/table/tbody/tr')
for row in Rows[1:]:
    name = row.find_element(By.XPATH, 'td[2]').text

    if name == 'Nolan Scott':
        print(name)
        row.find_element(By.XPATH, 'td[1]').click()
        break

time.sleep(5)

Pending_Queries = '//*[@id="P86_UN_RESPN_HEADING_CONTAINER"]/div[2]/div'
Rows = driver.find_element(By.XPATH,'//*[@id="unresponded_id_data_panel"]/div[2]/table/tbody/tr')

for row in Rows:
    ICC_Code = row.find_element(By.XPATH, 'td[2]')
    if ICC_Code == 'E11.00':
       print('test case passed')
    else:
        print('test case failed')

time.sleep(6)


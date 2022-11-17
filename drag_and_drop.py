from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from Base_Driver.Base_driver import Baseclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class action_one:


    def initial(self):
        self.option= Options()
        self.option.add_argument("--disable-notifications")
        self.browser= webdriver.Chrome('C:\\chromedriver_win32\\chromedriver', options = self.option)
        self.browser.get("https://demoqa.com/droppable/")
        self.browser.maximize_window()

    def drag_one(self):
       action = ActionChains(self.browser)
       time.sleep(7)

       #from_elem = WebDriverWait(self.browser, 10).until(EC.element_to_be_selected((By.XPATH, '//*[@id="draggable"]')))
       from_elem = self.browser.find_element(By.XPATH, '//*[@id="draggable"]')
       to_elem = self.browser.find_element(By.XPATH, '//*[@id="droppable"]')
       action.drag_and_drop(from_elem,to_elem).perform()
       text_check = to_elem.text
       assert text_check == "Dropped!"
       print("passed")
       from_location = from_elem.location
       print(from_location)

obj = action_one()
obj.initial()
obj.drag_one()
#action.drag_and_drop_by_offset(from_elem, 210,150).perform()









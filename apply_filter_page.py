
from Base_Driver.Base_driver import Baseclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

class flight_results(Baseclass):

      filter_button= "//p[@class='font-lightgrey bold'][normalize-space()='1']"
      one_stop_list = "//span[contains(text() ,'1 Stop')]"
      hidden_elem_in_results = "//div[contains(text() ,'More Flights') or contains(text() , '1 More Flight')]"

      def __init__(self,browser,wait):
          super().__init__(browser, wait)



      def  get_hidden_elems_in_searchresults(self):
           return self.browser.find_elements(By.XPATH, self.hidden_elem_in_results)


      def  get_one_stop_results(self):
           return self.browser.find_elements(By.XPATH, self.one_stop_list)


      def  select_filter_flightsButton(self):
           return self.wait_until_element_is_clickable(By.XPATH, self.filter_button)

      def  filter_flights(self):
           self.select_filter_flightsButton().click()






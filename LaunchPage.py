from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Base_Driver.Base_driver import Baseclass
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.apply_filter_page import flight_results
import time
class Launchpage(Baseclass):

      departFromField = '//*[@id="BE_flight_origin_city"]'
      goingToField = '//*[@id="BE_flight_arrival_city"]'
      departDateField = '//*[@id="BE_flight_origin_date"]'
      flight_search_button = '//*[@id="BE_flight_flsearch_btn"]'
      departDate = '//*[@id="03/11/2022"]'


      def __init__(self,browser,wait):
          super().__init__(browser,wait)
          self.browser = browser
          #self.wait = wait

      def get_depart_fromField(self):
            return self.wait_until_element_is_clickable(By.XPATH, self.departFromField)

      def enterDepartFromLocation(self, depart_location):
            self.get_depart_fromField().click()
            time.sleep(5)
            self.get_depart_fromField().send_keys(depart_location)
            time.sleep(6)
            self.get_depart_fromField().send_keys(Keys.ENTER)

      def get_going_toField(self):

            return self.wait_until_element_is_clickable(By.XPATH, self.goingToField)

      def entergoing_toLocation(self,going_to_location):

            self.get_going_toField().click()
            self.get_going_toField().send_keys(going_to_location)
            time.sleep(6)
            self.get_going_toField().send_keys(Keys.ENTER)
            time.sleep(5)


      def get_depart_date(self):
          return self.wait_until_element_is_clickable(By.XPATH, self.departDateField)

      def enter_depart_date(self):
          self.get_depart_date().click()
          time.sleep(5)
          self.select_depart_date().click()
          time.sleep(5)

      def select_depart_date(self):
          return self.wait_until_element_is_clickable(By.XPATH, self.departDate)


      def get_searchFlightButton(self):
         return self.browser.find_element(By.XPATH, self.flight_search_button)

      def click_searchFlightButton(self):
          self.get_searchFlightButton().click()
          time.sleep(10)

      def SearchFlights(self,depart_location,going_to_location):
          self.enterDepartFromLocation(depart_location)
          time.sleep(4)
          self.entergoing_toLocation(going_to_location)
          time.sleep(4)
          self.enter_depart_date()
          time.sleep(4)
          self.click_searchFlightButton()
          time.sleep(8)
          search_flights_result = flight_results(self.browser,self.wait)
          return search_flights_result


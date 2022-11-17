import pytest
from PageObjects.LaunchPage import Launchpage
from Utilities.utils import Utils
#import softest
from ddt import ddt, data, unpack
import unittest


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(unittest.TestCase):
    #softest.TestCase
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Launchpage(self.browser,self.wait)
        self.ut = Utils(self.browser)

    @data(*Utils.read_data_from_excel("C:\\Users\\Lenovo\\Documents\\Book1.xlsx","Sheet1"))
    @unpack
    def test_search_flights(self,depart_location, going_to_location):

        search_flights_result = self.lp.SearchFlights(depart_location,going_to_location)
        #search_flights_result = self.lp.SearchFlights("Chennai","Pune")

        search_flights_result.filter_flights()

        self.lp.page_scroll()

        stop1_list = search_flights_result.get_one_stop_results()
        elems = search_flights_result.get_hidden_elems_in_searchresults()
        self.ut.scroll_to_elemInList_AndClick(elems)
        self.ut.assert_list_items(stop1_list , "1 Stop")










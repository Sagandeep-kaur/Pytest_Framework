import pytest
from PageObjects.LaunchPage import Launchpage
from Utilities.utils import Utils
#import softest
#from Utilities.Baseclass import baseclass


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Launchpage(self.browser,self.wait)
        self.ut = Utils(self.browser)

    def test_search_flights(self):

        search_flights_result = self.lp.SearchFlights("Chennai", "New York")

        search_flights_result.filter_flights()

        self.lp.page_scroll()

        stop1_list = search_flights_result.get_one_stop_results()

        elems = search_flights_result.get_hidden_elems_in_searchresults()
        self.ut.scroll_to_elemInList_AndClick(elems)

        self.ut.assert_list_items(stop1_list , "1 Stop")










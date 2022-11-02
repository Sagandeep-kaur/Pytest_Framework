
class Utils():
      def __init__(self,browser):
         self.browser= browser

      def assert_list_items(self,list, value):

          for stop in list:
              assert (stop.text) == value
              print("assert passed")

      def scroll_to_elemInList_AndClick(self,list):

          for elem in list:
              self.browser.execute_script("arguments[0].scrollIntoView();", elem)
              self.browser.execute_script("arguments[0].click();", elem)
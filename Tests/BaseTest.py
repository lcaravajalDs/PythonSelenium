import unittest

from Config.ConfigParser import parser
from selenium import webdriver
from Page.SearchResultsPage import SearchResultsPage
from Page.MainPage import MainPage



class BaseTest(unittest.TestCase):
    configfile=parser()
    def setUp(self):
        print ('algo')
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.python.org")
        main_page = MainPage(self.driver)
        main_page.search_field="pycon"
        main_page.click_go_button()
        search_results_page = SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), "No results found."
    def test_lala(self):
        print ('lala')

    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()

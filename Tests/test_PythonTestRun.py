from Page.SearchResultsPage import SearchResultsPage
from Page.MainPage import MainPage
import datetime
from Config.ConfigParser import parser
import unittest

class PythonOrgSearch(unittest.TestCase):
    configfile=parser()
    def test_search_in_python_org(self):
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())
        driver = self.configfile.getBrowser('1')
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())
        driver.implicitly_wait(10)
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())
        env=self.configfile.get_url()
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())
        driver.get(env)
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        
        main_page = MainPage(driver)
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())
        main_page.search_field="pycon"
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        
        main_page.click_go_button()
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        
        search_results_page = SearchResultsPage(driver)
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        
        assert search_results_page.is_results_found(), "No results found."
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        

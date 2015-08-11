from Tests.BaseTest import BaseTest
from Page.SearchResultsPage import SearchResultsPage
from Page.MainPage import MainPage
import datetime

class PythonOrgSearch(BaseTest):

    def test_search_in_python_org(self):
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        
        main_page = MainPage(self.driver)
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())
        main_page.search_field="pycon"
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        
        main_page.click_go_button()
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        
        search_results_page = SearchResultsPage(self.driver)
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        
        assert search_results_page.is_results_found(), "No results found."
        current_time = datetime.datetime.now().time()
        print (current_time.isoformat())        

'''
Created on 7/8/2015

@author: Luciano
'''
from Tests.BaseTest import BaseTest
from Page.MainPage import MainPage
from Page.SearchResultsPage import SearchResultsPage

class AnotherTest(BaseTest):

    def test_search_in_python_org_Another(self):
        
        main_page = MainPage(self.driver)
        main_page.search_field="#invalid@search*"
        main_page.click_go_button()
        search_results_page = SearchResultsPage(self.driver)
        assert -(search_results_page.is_results_found())


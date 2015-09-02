from Tests.BaseTest import BaseTest
from Page.SearchResultsPage import SearchResultsPage
from Page.MainPage import MainPage

class PythonOrgSearch(BaseTest):

    def test_search_in_python_org(self):
        
        main_page = MainPage(self.driver)
        main_page.search_field="#invalid@search*"
        main_page.click_go_button()
        search_results_page = SearchResultsPage(self.driver)
        assert -(search_results_page.is_results_found())
        
    def test_search_in_python_org_valid(self):
        
        main_page = MainPage(self.driver)
        main_page.search_field="python"
        main_page.click_go_button()
        search_results_page = SearchResultsPage(self.driver)
        assert search_results_page.is_results_found()
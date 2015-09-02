from Page.PageBase import BasePage
class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No results found." in self.driver.page_source

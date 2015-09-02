from Page.PageBase import BasePage
class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No resultsX found." not in self.driver.page_source
from Page.PageBase import BasePage
class SearchResultsPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def is_results_found(self):
        return "No results found." not in self.driver.page_source
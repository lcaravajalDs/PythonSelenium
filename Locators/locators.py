from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')
    SEARCH_FIELD=(By.NAME,'q')

class SearchResultsPageLocators(object):
    pass
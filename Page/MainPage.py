from Page.PageBase import BasePage
from Elements.element import BasePageElement
from Locators.locators import MainPageLocators
 
class MainPage(BasePage):
    
    class Search_Field(BasePageElement):
        locator=MainPageLocators.SEARCH_FIELD
     
    search_field=Search_Field()
     
    def is_title_matches(self):
        return "Python" in self.driver.title
 
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

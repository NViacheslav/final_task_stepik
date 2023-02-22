from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.NT_EMPTY), "The notification about empy basket is not presented"
        
    def nt_about_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "The product in basket is presented"
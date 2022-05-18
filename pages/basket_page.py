from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import *

class BasketPage(BasePage):    
    def basket_is_not_have_product(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_IS_NOT_HAVE_PRODUCT), 'Basket is have product'

    def message_about_basket_is_empty(self):
        message_for_basket = self.browser.find_element(*MainPageLocators.MESSAGE_ABOUT_BASKET_IS_EMPTY)
        assert "Your basket is empty. Continue shopping" == message_for_basket.text , "basket not have message about 'basket empty'"      
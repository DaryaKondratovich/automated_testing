from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import AddInBasket

class ProductPage(BasePage):
    def add_in_basket(self):
        basket = self.browser.find_element(*AddInBasket.ADD_IN_BASKET)
        basket.click()

    def message_about_add_in_basket(self):
        assert self.is_element_present(*AddInBasket.MESSAGE_ABOUT_ADD_IN_BASKET)

    def name_book(self):
        name_in_message = self.browser.find_element(*AddInBasket.MESSAGE_NAME_BOOK)
        main_name_book = self.browser.find_element(*AddInBasket.NAME_BOOK)
        assert name_in_message.text == main_name_book.text, 'Name a book in message != name main a book'  

    def price(self):
        price_in_basket = self.browser.find_element(*AddInBasket.PRICE_BASKET)
        main_price = self.browser.find_element(*AddInBasket.PRICE_BOOK)
        assert price_in_basket.text == main_price.text, 'Price in a basket != main a price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AddInBasket.MESSAGE_ABOUT_ADD_IN_BASKET), "Success message is presented, but should not be"     

    def should_disappeared(self):
        assert self.is_disappeared(*AddInBasket.MESSAGE_ABOUT_ADD_IN_BASKET), "Message is not disappeared"      

  

            











from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")   

class AddInBasket():
    ADD_IN_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_ABOUT_ADD_IN_BASKET = (By.CSS_SELECTOR, '[style="visibility: visible;"] :nth-child(1)')
    MESSAGE_NAME_BOOK = (By.CSS_SELECTOR, '[style="visibility: visible;"] :nth-child(1) :nth-child(2) :nth-child(1)')
    NAME_BOOK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main :nth-child(1)')
    PRICE_BASKET = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info :nth-child(2) :nth-child(1) :nth-child(1)")
    PRICE_BOOK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main :nth-child(2)')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


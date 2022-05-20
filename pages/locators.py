from selenium.webdriver.common.by import By


class MainPageLocators():
    GO_TO_BASKET = (By.CSS_SELECTOR, "span.btn-group" )
    BASKET_IS_NOT_HAVE_PRODUCT = (By.CSS_SELECTOR, "form.basket_summary")
    MESSAGE_ABOUT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div.content")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, '[name="registration-email"]')
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '[name="registration-password1"]') 
    COFIRM_PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '[name="registration-password2"]')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[name="registration_submit"]')
class AddInBasket():
    ADD_IN_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_ABOUT_ADD_IN_BASKET = (By.CSS_SELECTOR, '[style="visibility: visible;"] :nth-child(1)')
    MESSAGE_NAME_BOOK = (By.CSS_SELECTOR, '[style="visibility: visible;"] :nth-child(1) :nth-child(2) :nth-child(1)')
    NAME_BOOK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main :nth-child(1)')
    PRICE_BASKET = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info :nth-child(2) :nth-child(1) :nth-child(1)")
    PRICE_BOOK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main :nth-child(2)')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

   


    



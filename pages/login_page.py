from .base_page import BasePage
from .locators import LoginPageLocators
import time
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login URL is not True"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Log In form is False"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is False"

    def register_new_user(self):
        email = str(time.time()) + "hjg@fakemail.org"
        password = str(time.time()) + "ghkzdfg1235"
        email_registration = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        email_registration.send_keys(email)
        password_registration  = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION)
        password_registration.send_keys(password)
        password2_registration  = self.browser.find_element(*LoginPageLocators.COFIRM_PASSWORD_REGISTRATION)
        password2_registration.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()

        
  

        
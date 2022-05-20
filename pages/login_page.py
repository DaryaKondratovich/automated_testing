from .base_page import BasePage
from .locators import LoginPageLocators
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

    def register_new_user(self, email, password):
        self.email = str(time.time()) + "@fakemail.org"
        self.password = str(time.time()) + "ghkzdfg"
        email_registration = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION).send_keys(email)
        password_registration  = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION).send_keys(password)
        password2_registration  = self.browser.find_element(*LoginPageLocators.COFIRM_PASSWORD_REGISTRATION).send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()
        
  

        
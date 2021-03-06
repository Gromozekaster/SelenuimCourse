from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "http://selenium1py.pythonanywhere.com/ru/accounts/login/" == self.url

    def should_be_login_form(self):
        assert self.browser.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.browser.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM)

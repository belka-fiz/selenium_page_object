from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Page Object class for Login page"""

    def should_be_login_page(self):
        """Makes sure the page is login page by verifying url and presence of forms"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Verify that URL contains 'login'"""
        assert self.url_contains('login'), "Login page URL is wrong"

    def should_be_login_form(self):
        """Verify the presence of login form"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LOCATOR), "No login form"

    def should_be_register_form(self):
        """Verify the presence of registration form"""
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_LOCATOR), "No registration form"

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

    def register_new_user(self, email, password, password_confirmation=""):
        """Register a new user with given email and password"""
        password_confirmation = password_confirmation or password
        self.enter_registration_login(email)
        self.enter_registration_password(password)
        self.enter_registration_password_confirmation(password_confirmation)
        self.submit_registration()

    def enter_registration_login(self, login):
        """Enter login for registration"""
        self.browser.find_element(*LoginPageLocators.REGISTRATION_LOGIN).send_keys(login)

    def enter_registration_password(self, password):
        """Enter login for registration"""
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)

    def enter_registration_password_confirmation(self, password):
        """Enter login for registration"""
        self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD).send_keys(password)

    def submit_registration(self):
        """Submit registration form"""
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()

    def should_be_registered(self):
        """
        Verify the user is registered by checking the success message
        This method is not added to registration method as long as there may be a negative scenario test,
        where we should verify the opposite
        """
        self.is_element_present(*LoginPageLocators.REGISTRATION_SUCCESS)

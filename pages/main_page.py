from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """Class for Main page of the store"""

    def go_to_login_page(self):
        """Click login link"""
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """Find login link on the main page"""
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not found on the page"

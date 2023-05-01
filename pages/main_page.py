from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    """Class for Main page of the store"""

    def go_to_login_page(self):
        """Click login link"""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        """Find login link on the main page"""
        try:
            self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        except NoSuchElementException:
            return False
        return True

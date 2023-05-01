from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    """Class for Main page of the store"""

    def go_to_login_page(self):
        """Click login link"""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

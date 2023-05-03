from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """Base class for Page Object pattern"""

    def __init__(self, browser: WebDriver, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Opens the page in the browser"""
        self.browser.get(self.url)

    def is_element_present(self, by: By, locator: str):
        """Indicates if the element is present"""
        try:
            self.browser.find_element(by, locator)
        except NoSuchElementException:
            return False
        return True

    def url_contains(self, substring):
        """Indicates if url matches the expected one"""
        return substring in self.browser.current_url

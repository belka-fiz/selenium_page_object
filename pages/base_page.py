from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Base class for Page Object pattern"""

    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        """Open the page in the browser"""
        self.browser.get(self.url)

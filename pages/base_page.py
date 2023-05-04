import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver

from data.constants import HEADER_TOTAL_PRICE, HEADER_VIEW_BASKET_BUTTON_TEXT
from .locators import BasePageLocators


class BasePage:
    """Base class for Page Object pattern"""

    def __init__(self, browser: WebDriver, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        if browser.current_url != self.url:
            self.open()

    def open(self):
        """Opens the page in the browser"""
        self.browser.get(self.url)

    def is_element_present(self, by: By, locator: str):
        """Indicates if the element is present on the page"""
        try:
            self.browser.find_element(by, locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Indicates if element is absent on the page"""
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """Check whether element has disappeared from the page"""
        try:
            WebDriverWait(self.browser,
                          timeout,
                          1,
                          TimeoutException).until_not(ec.presence_of_element_located((how, what)))  # noqa
        except TimeoutException:
            return False

        return True

    def url_contains(self, substring):
        """Indicates if url contains the expected substring"""
        return substring in self.browser.current_url

    def solve_quiz_and_get_code(self):
        """
        Stepik quiz solver for the course
        https://stepik.org/lesson/201964/step/2?unit=176022
        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        """Click login link"""
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """Find login link on the main page"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not found on the page"

    def get_header_basket_total(self):
        """Get total price of the basket"""
        text = self.browser.find_element(*BasePageLocators.BASKET_TOTAL).text
        return text[len(HEADER_TOTAL_PRICE):-(len(HEADER_VIEW_BASKET_BUTTON_TEXT))].strip()

    def go_to_basket_page(self):
        """Go to Basket page"""
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

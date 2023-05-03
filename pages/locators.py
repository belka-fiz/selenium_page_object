from typing import TypeAlias

from selenium.webdriver.common.by import By


Locator: TypeAlias = tuple[By, str]


class MainPageLocators:
    """Locators for the main page"""

    LOGIN_LINK: Locator = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    """Locators for the login page"""

    LOGIN_FORM_LOCATOR: Locator = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM_LOCATOR: Locator = (By.CSS_SELECTOR, "#register_form")

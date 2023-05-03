from typing import TypeAlias

from selenium.webdriver.common.by import By

Locator: TypeAlias = tuple[By, str]


class BasePageLocators:
    """Common locators"""

    BASKET_TOTAL: Locator = (By.CSS_SELECTOR, "div.basket-mini")


class MainPageLocators:
    """Locators for the main page"""

    LOGIN_LINK: Locator = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    """Locators for the login page"""

    LOGIN_FORM_LOCATOR: Locator = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM_LOCATOR: Locator = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    """Locators for product page"""

    ADD_TO_BASKET_BUTTON: Locator = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME: Locator = (By.CSS_SELECTOR, "div.product_main > h1")
    PRICE: Locator = (By.CSS_SELECTOR, "p.price_color")

    UPDATED_BASKET_TOTAL_ALERT: Locator = (By.CSS_SELECTOR, "#messages>div.alert-info>div.alertinner>p>strong")
    ADDED_ITEM_NAME: Locator = (By.CSS_SELECTOR, "#messages>div.alert-success:nth-of-type(1)>div.alertinner>strong")

from typing import TypeAlias

from selenium.webdriver.common.by import By

Locator: TypeAlias = tuple[By, str]


class BasePageLocators:
    """Common locators"""

    BASKET_TOTAL: Locator = (By.CSS_SELECTOR, "div.basket-mini")
    BASKET_LINK: Locator = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    LOGIN_LINK: Locator = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID: Locator = (By.CSS_SELECTOR, "#login_link_invalid")
    USER_ICON: Locator = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    """Basket locators"""

    EMPTY_BASKET_LABEL = (By.XPATH, "//*[contains (text(), 'Your basket is empty')]")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")


class MainPageLocators:
    """Locators for the main page"""


class LoginPageLocators:
    """Locators for the login page"""

    LOGIN_FORM_LOCATOR: Locator = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM_LOCATOR: Locator = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_LOGIN: Locator = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD: Locator = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD: Locator = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT: Locator = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")
    success_xpath = "// div[contains(@class,\"alertinner\")and contains(text(), \"Thanks for registering!\")]"
    REGISTRATION_SUCCESS: Locator = (By.XPATH, success_xpath)


class ProductPageLocators:
    """Locators for product page"""

    ADD_TO_BASKET_BUTTON: Locator = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME: Locator = (By.CSS_SELECTOR, "div.product_main > h1")
    PRICE: Locator = (By.CSS_SELECTOR, "p.price_color")

    UPDATED_BASKET_TOTAL_ALERT: Locator = (By.CSS_SELECTOR, "#messages>div.alert-info>div.alertinner>p>strong")
    ADDED_ITEM_NAME: Locator = (By.CSS_SELECTOR, "#messages>div.alert-success:nth-of-type(1)>div.alertinner>strong")

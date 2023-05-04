from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    """Page Object class for Basket page"""

    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_LABEL), "No label that basket is empty"
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are items in the basket"

    def should_be_basket_page(self):
        assert self.url_contains("basket"), f"It is not basket page. Actual URL: {self.browser.current_url}"

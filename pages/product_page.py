from .base_page import BasePage, WebDriver
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Representation of a product page"""

    def __init__(self, browser: WebDriver, url: str):
        super().__init__(browser, url)
        self.price: str = self.get_price()
        self.product_name: str = self.get_name()

    def get_price(self) -> str:
        """Get the price of the product"""
        return self.browser.find_element(*ProductPageLocators.PRICE).text.strip()

    def get_name(self) -> str:
        """get product name"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()

    def add_to_basket(self) -> None:
        """Add an item to basket"""
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_added_item_name(self) -> str:
        """Get name of the added to basket item"""
        return self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text.strip()

    def get_updated_basket_total(self) -> str:
        """Get the price of added to basket item"""
        return self.browser.find_element(*ProductPageLocators.UPDATED_BASKET_TOTAL_ALERT).text.strip()

    def check_product_is_added(self) -> None:
        """Check basket price and name of added items"""
        assert self.get_updated_basket_total() == self.price, "New total does not match product price"
        assert self.get_added_item_name() == self.product_name, "Added item name does not match with product name"
        header_total = self.get_header_basket_total()
        assert header_total == self.price, f"Header total mismatch. Expected \"{self.price}\", got \"{header_total}\"."

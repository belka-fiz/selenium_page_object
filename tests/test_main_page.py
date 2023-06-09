import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    """Test for finding login page as a guest"""

    def test_guest_can_go_to_login_page(self, browser, browser_name):
        """Ensure a user can go from Main page to login page"""
        page = MainPage(browser, link)
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser, browser_name):
        """Ensure the login link is present on the main page"""
        page = MainPage(browser, link)
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, browser_name):
    """Ensure the basket for a new user is empty"""
    page = MainPage(browser, link)
    page.go_to_basket_page()
    basket_page = BasketPage(browser, page.browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty()

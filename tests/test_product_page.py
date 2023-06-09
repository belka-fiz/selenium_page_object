import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
no_promo_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
promo_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


@pytest.mark.guest_product_to_basket
class TestGuestProductPageBasketActions:
    """Test set for guest user action on/from product page related to adding/not adding an item to basket"""

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [
        'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    ], ids=str)
    def test_guest_can_add_product_to_basket(self, browser, browser_name, link):
        """Add to basket, verify the price and solve quiz"""
        page = ProductPage(browser, link)
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_product_is_added()

    @pytest.mark.xfail(reason="Originally failing test", strict=True)
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, browser_name):
        """Failing test that customer can't see success message after adding to basket"""
        page = ProductPage(browser, promo_link)
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, browser_name):
        """Test that customer doesn't see success message right after opening the page"""
        page = ProductPage(browser, promo_link)
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="Originally failing test", strict=True)
    def test_message_disappeared_after_adding_product_to_basket(self, browser, browser_name):
        """Failing test that customer can't see success message after adding to basket"""
        page = ProductPage(browser, promo_link)
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_disappear_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, browser_name):
        """Ensure the basket for a new user is empty is opened from product page"""
        page = ProductPage(browser, no_promo_link)
        page.go_to_basket_page()
        basket_page = BasketPage(browser, page.browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_be_empty()


@pytest.mark.login_guest
class TestGuestProductPageLoginActions:
    """Guest user can see login link and go to login page"""

    def test_guest_should_see_login_link_on_product_page(self, browser, browser_name):
        """Ensure a user can see login link from Product page"""
        page = ProductPage(browser, no_promo_link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, browser_name):
        """Ensure a user can go from Product page to login page"""
        page = ProductPage(browser, no_promo_link)
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


# Setup actions in browser and pre-test in-browser verification
# are additional dependencies and possible points of failure.
# It is better when setup, like user registration, is performed via API or database,
# but in this project we have no API access, and this way is better than nothing.
class TestUserAddToBasketFromProductPage:
    """Tests authorized user to add products to basket"""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, browser_name, email, password):
        """Fixture for user authorization"""
        login_page = LoginPage(browser, login_link)
        login_page.register_new_user(email, password)
        login_page.should_be_registered()
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, browser_name):
        """Add to basket, verify the price and solve quiz"""
        page = ProductPage(browser, promo_link)
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_product_is_added()

    def test_user_cant_see_success_message(self, browser, browser_name):
        """Test that customer doesn't see success message right after opening the page"""
        page = ProductPage(browser, promo_link)
        page.should_not_be_success_message()

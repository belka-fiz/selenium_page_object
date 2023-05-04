import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage, ProductPageLocators

no_promo_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
promo_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
], ids=str)
def test_guest_can_add_product_to_basket(browser, browser_name, link):
    """Add to basket, verify the price and solve quiz"""
    page = ProductPage(browser, link)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_is_added()


@pytest.mark.xfail(reason="Originally failing test", strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, browser_name):
    """Failing test that customer can't see success message after adding to basket"""
    page = ProductPage(browser, promo_link)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.ADDED_ITEM_NAME), \
        "There is a success message with product name. Expected not to be"
    assert page.is_not_element_present(*ProductPageLocators.UPDATED_BASKET_TOTAL_ALERT), \
        "There is a success message with price. Expected not to be"


def test_guest_cant_see_success_message(browser, browser_name):
    """Test that customer don't success message right after oppening the page"""
    page = ProductPage(browser, promo_link)
    assert page.is_not_element_present(*ProductPageLocators.ADDED_ITEM_NAME), \
        "There is a success message with product name. Expected not to be"
    assert page.is_not_element_present(*ProductPageLocators.UPDATED_BASKET_TOTAL_ALERT), \
        "There is a success message with price. Expected not to be"


@pytest.mark.xfail(reason="Originally failing test", strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser, browser_name):
    """Failing test that customer can't see success message after adding to basket"""
    page = ProductPage(browser, promo_link)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_element_present(*ProductPageLocators.ADDED_ITEM_NAME), \
        "There is no success message with product name"
    assert page.is_element_present(*ProductPageLocators.UPDATED_BASKET_TOTAL_ALERT), \
        "There is no success message with price"
    assert page.is_disappeared(*ProductPageLocators.ADDED_ITEM_NAME), \
        "There is a success message with product name. Expected not to be"
    assert page.is_disappeared(*ProductPageLocators.UPDATED_BASKET_TOTAL_ALERT), \
        "There is a success message with price. Expected not to be"


def test_guest_should_see_login_link_on_product_page(browser, browser_name):
    """Ensure a user can see login link from Product page"""
    page = ProductPage(browser, no_promo_link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser, browser_name):
    """Ensure a user can go from Product page to login page"""
    page = ProductPage(browser, no_promo_link)
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, browser_name):
    """Ensure the basket for a new user is empty is opened from product page"""
    page = ProductPage(browser, no_promo_link)
    page.go_to_basket_page()
    basket_page = BasketPage(browser, page.browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty()

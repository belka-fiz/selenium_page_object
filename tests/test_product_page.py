import pytest

from pages.product_page import ProductPage


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

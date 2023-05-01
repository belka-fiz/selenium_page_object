from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser, browser_name):
    """Ensure a user can go from Main page to login page"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser, browser_name):
    """Ensure the login link is present on the main page"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    assert page.should_be_login_link(), "Login link is not found on the page"

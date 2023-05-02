from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser, browser_name):
    """Ensure a user can go from Main page to login page"""
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser, browser_name):
    """Ensure the login link is present on the main page"""
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
